"""
Database models

PRD Reference: PRD.md p.42 (Database Schema)
"""

from sqlalchemy import Column, String, Integer, Text, TIMESTAMP, CheckConstraint, Index
from sqlalchemy.sql import func
import uuid

from .db import Base

# For SQLite compatibility, use String for UUID and JSON for JSONB
try:
    from sqlalchemy.dialects.postgresql import UUID, JSONB
    UUID_TYPE = UUID(as_uuid=True)
    JSON_TYPE = JSONB
except:
    UUID_TYPE = String(36)
    from sqlalchemy import JSON
    JSON_TYPE = JSON


class Analysis(Base):
    """
    Stores analysis results for repositories
    
    PRD Reference: PRD.md p.42
    """
    __tablename__ = "analyses"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    github_url = Column(String(500), nullable=False)
    repository_name = Column(String(255), nullable=False)
    commit_sha = Column(String(40))
    status = Column(String(50), nullable=False)  # pending, processing, completed, failed
    created_at = Column(TIMESTAMP, server_default=func.now())
    completed_at = Column(TIMESTAMP)
    error_message = Column(Text)
    
    # Metadata
    total_files = Column(Integer)
    total_loc = Column(Integer)
    primary_language = Column(String(50))
    languages = Column(JSON_TYPE)
    
    # Results
    graph_data = Column(JSON_TYPE)
    metrics = Column(JSON_TYPE)
    health_scores = Column(JSON_TYPE)
    dead_code = Column(JSON_TYPE)
    duplicates = Column(JSON_TYPE)
    
    __table_args__ = (
        CheckConstraint("status IN ('pending', 'processing', 'completed', 'failed')", name='valid_status'),
        Index('idx_analyses_status', 'status'),
        Index('idx_analyses_created_at', 'created_at'),
        Index('idx_analyses_github_url', 'github_url'),
    )

