"""
Analysis API endpoints

PRD Reference: PRD.md p.44-46
TASK: TASK-203, TASK-204
"""

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from uuid import UUID
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
        id=uuid.uuid4(),
        github_url=request.github_url,
        repository_name=repository_name,
        status='pending'
    )
    
    db.add(analysis)
    db.commit()
    db.refresh(analysis)
    
    # TODO: Queue Celery task (TASK-205)
    # For now, just return the ID
    
    return AnalyzeResponse(
        analysis_id=analysis.id,
        status='pending',
        estimated_time=45,  # Estimated seconds
        message="Analysis queued successfully"
    )


@router.get("/analysis/{analysis_id}", response_model=AnalysisStatus)
async def get_analysis(
    analysis_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Get analysis status and results
    
    PRD Reference: PRD.md p.45
    TASK: TASK-204
    
    Args:
        analysis_id: UUID of the analysis
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

