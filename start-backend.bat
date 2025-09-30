@echo off
echo ========================================
echo Starting CodeMapper Backend
echo ========================================
cd backend
call venv\Scripts\activate
echo.
echo Setting environment variables...
set DATABASE_URL=sqlite:///./codemapper.db
set PYTHONPATH=C:\Users\ianig\Desktop\CodeVisualizer\backend
set USE_CELERY=0
echo.
echo Starting FastAPI server...
echo Backend API will be at: http://localhost:8000
echo API Docs at: http://localhost:8000/docs
echo.
python -m uvicorn api.main:app --reload --host 0.0.0.0 --port 8000

