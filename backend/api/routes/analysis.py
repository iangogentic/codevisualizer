"""
Analysis API endpoints

PRD Reference: PRD.md p.44-46
TASK: TASK-203, TASK-204
"""

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import uuid

from api.schemas.analysis import AnalyzeRequest, AnalyzeResponse, AnalysisStatus
from database.db import get_db
from database.models import Analysis
from github.validators import validate_github_url, GitHubURLError

router = APIRouter(prefix="/api", tags=["analysis"])


@router.post("/analyze", response_model=AnalyzeResponse, status_code=202)
async def start_analysis(
    request: AnalyzeRequest,
    db: Session = Depends(get_db)
):
    """
    Start analysis of a GitHub repository
    
    PRD Reference: PRD.md p.44
    TASK: TASK-203
    
    Args:
        request: Analysis request with GitHub URL and options
        db: Database session
        
    Returns:
        AnalyzeResponse: Analysis ID and status
        
    Raises:
        HTTPException: 400 if URL invalid, 500 if analysis fails to queue
    """
    # Validate GitHub URL
    try:
        org, repo = validate_github_url(request.github_url)
        repository_name = f"{org}/{repo}"
    except GitHubURLError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    # Create analysis record
    analysis = Analysis(
        id=str(uuid.uuid4()),
        github_url=request.github_url,
        repository_name=repository_name,
        status='pending'
    )
    
    db.add(analysis)
    db.commit()
    db.refresh(analysis)
    
    # Queue Celery task (or run synchronously if Celery not available)
    try:
        from tasks.analyze_repository import analyze_repository_task
        analyze_repository_task.delay(str(analysis.id), request.github_url)
    except (ImportError, Exception) as e:
        # Celery not available, run analysis synchronously for demo
        import logging
        logging.warning(f"Celery not available ({e}), running sync analysis")
        
        # Import analysis functions
        from github.client import GitHubClient
        from analysis.emerge_wrapper import EmergeAnalyzer
        from analysis.graph_builder import GraphBuilder
        from datetime import datetime
        
        # Run analysis inline
        try:
            analysis.status = 'processing'
            db.commit()
            
            # Clone and analyze
            repo_path = GitHubClient.clone_repository(request.github_url)
            commit_sha = GitHubClient.get_commit_sha(repo_path)
            
            analyzer = EmergeAnalyzer()
            language = analyzer.detect_language(repo_path)
            results = analyzer.run_analysis(repo_path, language)
            
            # Store results
            analysis.commit_sha = commit_sha
            analysis.primary_language = language
            analysis.total_files = results['statistics'].get('scanned_files', 0)
            analysis.total_loc = results['overall_metrics'].get('total-sloc-in-files', 0)
            analysis.metrics = results['overall_metrics']
            
            graph_data = GraphBuilder.build_graph_from_emerge(results['file_metrics'])
            analysis.graph_data = graph_data
            
            analysis.status = 'completed'
            analysis.completed_at = datetime.utcnow()
            db.commit()
            
            # Cleanup
            GitHubClient.cleanup(repo_path)
        except Exception as analysis_error:
            analysis.status = 'failed'
            analysis.error_message = str(analysis_error)
            analysis.completed_at = datetime.utcnow()
            db.commit()
    
    return AnalyzeResponse(
        analysis_id=analysis.id,
        status='pending',
        estimated_time=45,  # Estimated seconds
        message="Analysis queued successfully"
    )


@router.get("/analysis/{analysis_id}", response_model=AnalysisStatus)
async def get_analysis(
    analysis_id: str,
    db: Session = Depends(get_db)
):
    """
    Get analysis status and results
    
    PRD Reference: PRD.md p.45
    TASK: TASK-204
    
    Args:
        analysis_id: UUID string of the analysis
        db: Database session
        
    Returns:
        AnalysisStatus: Current status and results (if complete)
        
    Raises:
        HTTPException: 404 if analysis not found
    """
    analysis = db.query(Analysis).filter(Analysis.id == analysis_id).first()
    
    if not analysis:
        raise HTTPException(
            status_code=404,
            detail=f"Analysis {analysis_id} not found"
        )
    
    return AnalysisStatus.model_validate(analysis)

