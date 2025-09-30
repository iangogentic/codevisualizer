"""Initial database schema

Revision ID: 001
Revises: 
Create Date: 2025-09-30

PRD Reference: PRD.md p.42 (Database Schema)
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSONB

# revision identifiers
revision = '001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create analyses table
    op.create_table('analyses',
        sa.Column('id', UUID(as_uuid=True), primary_key=True),
        sa.Column('github_url', sa.String(500), nullable=False),
        sa.Column('repository_name', sa.String(255), nullable=False),
        sa.Column('commit_sha', sa.String(40)),
        sa.Column('status', sa.String(50), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP, server_default=sa.func.now()),
        sa.Column('completed_at', sa.TIMESTAMP),
        sa.Column('error_message', sa.Text),
        
        # Metadata
        sa.Column('total_files', sa.Integer),
        sa.Column('total_loc', sa.Integer),
        sa.Column('primary_language', sa.String(50)),
        sa.Column('languages', JSONB),
        
        # Results
        sa.Column('graph_data', JSONB),
        sa.Column('metrics', JSONB),
        sa.Column('health_scores', JSONB),
        sa.Column('dead_code', JSONB),
        sa.Column('duplicates', JSONB),
        
        sa.CheckConstraint("status IN ('pending', 'processing', 'completed', 'failed')", name='valid_status'),
    )
    
    # Create indexes
    op.create_index('idx_analyses_status', 'analyses', ['status'])
    op.create_index('idx_analyses_created_at', 'analyses', ['created_at'])
    op.create_index('idx_analyses_github_url', 'analyses', ['github_url'])


def downgrade() -> None:
    op.drop_index('idx_analyses_github_url', table_name='analyses')
    op.drop_index('idx_analyses_created_at', table_name='analyses')
    op.drop_index('idx_analyses_status', table_name='analyses')
    op.drop_table('analyses')

