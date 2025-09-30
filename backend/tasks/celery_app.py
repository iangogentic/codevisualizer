"""
Celery application configuration

PRD Reference: PRD.md p.37
TASK: TASK-205
"""

from celery import Celery
import os

# Get Redis URL from environment
REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')

# Create Celery app
celery_app = Celery(
    'codemapper',
    broker=REDIS_URL,
    backend=REDIS_URL,
    include=['tasks.analyze_repository']
)

# Celery configuration
celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    task_track_started=True,
    task_time_limit=600,  # 10 minutes max
    task_soft_time_limit=540,  # 9 minutes warning
    worker_prefetch_multiplier=1,
    worker_max_tasks_per_child=50,
)

