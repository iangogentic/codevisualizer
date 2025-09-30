"""
GitHub client for repository operations

PRD Reference: PRD.md p.41
TASK: TASK-202
"""

from git import Repo
import os
import tempfile
import shutil
from pathlib import Path
from typing import Optional


class GitHubClient:
    """Handle GitHub repository operations"""
    
    @staticmethod
    def clone_repository(github_url: str, timeout: int = 300) -> str:
        """
        Clone a GitHub repository to a temporary directory.
        
        Args:
            github_url: GitHub repository URL (HTTPS or SSH)
            timeout: Clone timeout in seconds (default: 5 minutes)
            
        Returns:
            str: Path to cloned repository
            
        Raises:
            Exception: If cloning fails
            
        PRD Reference: PRD.md p.41
        """
        temp_dir = tempfile.mkdtemp(prefix='codemapper_')
        
        try:
            # Clone with depth=1 for faster cloning
            Repo.clone_from(
                github_url,
                temp_dir,
                depth=1,
                single_branch=True
            )
            return temp_dir
        except Exception as e:
            # Clean up on failure
            GitHubClient.cleanup(temp_dir)
            raise Exception(f"Failed to clone repository: {str(e)}")
    
    @staticmethod
    def cleanup(directory: str) -> None:
        """
        Clean up temporary directory.
        
        Args:
            directory: Directory path to remove
        """
        if os.path.exists(directory):
            try:
                shutil.rmtree(directory)
            except Exception as e:
                print(f"Warning: Failed to clean up {directory}: {e}")
    
    @staticmethod
    def get_commit_sha(repo_path: str) -> Optional[str]:
        """
        Get current commit SHA from cloned repository.
        
        Args:
            repo_path: Path to git repository
            
        Returns:
            str: Commit SHA or None if failed
        """
        try:
            repo = Repo(repo_path)
            return repo.head.commit.hexsha
        except Exception:
            return None

