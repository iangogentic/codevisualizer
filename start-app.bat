@echo off
echo ========================================
echo Starting CodeMapper Frontend
echo ========================================
cd frontend
echo.
echo Installing dependencies...
call npm install --silent
echo.
echo Starting development server...
echo Frontend will open at: http://localhost:3000
echo.
call npm start

