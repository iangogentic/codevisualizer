"""
Celery task for repository analysis

PRD Reference: PRD.md p.41, Analysis Engine Flow
TASK: TASK-302
"""

from celery import Task
from tasks.celery_app import celery_app
from github.client import GitHubClient
from analysis.emerge_wrapper import EmergeAnalyzer
from database.db import SessionLocal
from database.models import Analysis
import logging
from uuid import UUID
from datetime import datetime

logger = logging.getLogger(__name__)


class AnalysisTask(Task):
    """Base task with error handling and database updates"""
    
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        """Handle task failure"""
        logger.error(f"Task {task_id} failed: {exc}")
        
        # Update database
        analysis_id = args[0] if args else None
        if analysis_id:
            self._update_status(analysis_id, 'failed', error=str(exc))
    
    def on_success(self, retval, task_id, args, kwargs):
        """Handle task success"""
        logger.info(f"Task {task_id} completed successfully")
    
    def _update_status(self, analysis_id: str, status: str, error: str = None):
        """Update analysis status in database"""
        db = SessionLocal()
        try:
            analysis = db.query(Analysis).filter(Analysis.id == UUID(analysis_id)).first()
            if analysis:
                analysis.status = status
                if status == 'failed':
                    analysis.error_message = error
                    analysis.completed_at = datetime.utcnow()
                db.commit()
        finally:
            db.close()


@celery_app.task(base=AnalysisTask, bind=True, name='tasks.analyze_repository')
def analyze_repository_task(self, analysis_id: str, github_url: str):
    """
    Analyze a GitHub repository (async task)
    
    PRD Reference: PRD.md p.41
    
    Flow:
    1. Clone repository
    2. Detect language
    3. Run Emerge analysis
    4. Parse results
    5. Store in database
    6. Cleanup
    
    Args:
        analysis_id: UUID of analysis record
        github_url: GitHub repository URL
        
    Returns:
        dict: Analysis results
    """
    logger.info(f"Starting analysis {analysis_id} for {github_url}")
    
    repo_path = None
    db = SessionLocal()
    
    try:
        # Update status to 'processing'
        analysis = db.query(Analysis).filter(Analysis.id == UUID(analysis_id)).first()
        if not analysis:
            raise ValueError(f"Analysis {analysis_id} not found")
        
        analysis.status = 'processing'
        db.commit()
        logger.info(f"Status updated to 'processing'")
        
        # Step 1: Clone repository
        logger.info(f"Cloning repository: {github_url}")
        repo_path = GitHubClient.clone_repository(github_url)
        logger.info(f"Repository cloned to: {repo_path}")
        
        # Step 2: Get commit SHA
        commit_sha = GitHubClient.get_commit_sha(repo_path)
        logger.info(f"Commit SHA: {commit_sha}")
        analysis.commit_sha = commit_sha
        db.commit()
        
        # Step 3: Detect language
        emerge_analyzer = EmergeAnalyzer()
        language = emerge_analyzer.detect_language(repo_path)
        logger.info(f"Detected language: {language}")
        analysis.primary_language = language
        db.commit()
        
        # Step 4: Run Emerge analysis
        logger.info("Running Emerge analysis...")
        results = emerge_analyzer.run_analysis(repo_path, language)
        logger.info(f"Analysis complete")
        
        # Step 5: Store results
        from analysis.graph_builder import GraphBuilder
        
        analysis.total_files = results['statistics'].get('scanned_files', 0)
        analysis.total_loc = results['overall_metrics'].get('total-sloc-in-files', 0)
        analysis.metrics = results['overall_metrics']
        
        # Transform to graph format
        graph_data = GraphBuilder.build_graph_from_emerge(results['file_metrics'])
        analysis.graph_data = graph_data
        
        analysis.status = 'completed'
        analysis.completed_at = datetime.utcnow()
        db.commit()
        
        logger.info(f"Analysis {analysis_id} completed successfully")
        
        return {
            'status': 'completed',
            'analysis_id': analysis_id,
            'total_files': analysis.total_files,
            'total_loc': analysis.total_loc
        }
        
    except Exception as e:
        logger.error(f"Analysis {analysis_id} failed: {str(e)}")
        
        # Update database
        if db:
            try:
                analysis = db.query(Analysis).filter(Analysis.id == UUID(analysis_id)).first()
                if analysis:
                    analysis.status = 'failed'
                    analysis.error_message = str(e)
                    analysis.completed_at = datetime.utcnow()
                    db.commit()
            except Exception as db_error:
                logger.error(f"Failed to update database: {db_error}")
        
        raise
    
    finally:
        # Always cleanup
        if repo_path:
            GitHubClient.cleanup(repo_path)
            logger.info(f"Cleaned up: {repo_path}")
        
        if db:
            db.close()

