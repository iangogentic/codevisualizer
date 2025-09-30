"""
Pydantic schemas for analysis endpoints

PRD Reference: PRD.md p.44-46 (API Specifications)
"""

from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, Dict, Any
from datetime import datetime
from uuid import UUID


class AnalyzeRequest(BaseModel):
    """
    Request to start repository analysis
    
    PRD Reference: PRD.md p.44
    """
    github_url: str = Field(..., description="GitHub repository URL", examples=["https://github.com/facebook/react"])
    options: Optional[Dict[str, Any]] = Field(default_factory=lambda: {
        "detect_duplicates": True,
        "detect_dead_code": True,
        "max_files": 10000
    })


class AnalyzeResponse(BaseModel):
    """
    Response when analysis is started
    
    PRD Reference: PRD.md p.44
    """
    analysis_id: UUID = Field(..., description="Unique analysis ID")
    status: str = Field(..., description="Analysis status", examples=["pending"])
    estimated_time: int = Field(..., description="Estimated completion time in seconds")
    message: str = Field(default="Analysis queued successfully")


class AnalysisStatus(BaseModel):
    """
    Analysis status and results
    
    PRD Reference: PRD.md p.45
    """
    id: UUID
    status: str  # pending, processing, completed, failed
    github_url: str
    repository_name: str
    commit_sha: Optional[str] = None
    created_at: datetime
    completed_at: Optional[datetime] = None
    error_message: Optional[str] = None
    
    # Metadata
    total_files: Optional[int] = None
    total_loc: Optional[int] = None
    primary_language: Optional[str] = None
    languages: Optional[Dict[str, float]] = None
    
    # Metrics
    metrics: Optional[Dict[str, Any]] = None
    graph_data: Optional[Dict[str, Any]] = None
    health_scores: Optional[Dict[str, Any]] = None
    dead_code: Optional[Dict[str, Any]] = None
    duplicates: Optional[Dict[str, Any]] = None
    
    class Config:
        from_attributes = True

