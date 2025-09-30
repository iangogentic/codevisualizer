"""
CodeMapper Backend API
Main FastAPI application

PRD Reference: PRD.md p.44-46 (API Specifications)
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import analysis
from database.db import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CodeMapper API",
    description="Code Visualization and Analysis Platform",
    version="0.1.0"
)

# CORS - allow frontend to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(analysis.router)


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "service": "CodeMapper API",
        "status": "healthy",
        "version": "0.1.0"
    }


@app.get("/api/health")
async def health_check():
    """
    Health check endpoint
    Returns API status
    """
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

