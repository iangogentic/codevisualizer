"""
GitHub URL validation

PRD Reference: PRD.md p.23, F1.0
TASK: TASK-201
"""

import re
from typing import Tuple


class GitHubURLError(Exception):
    """Raised when GitHub URL is invalid"""
    pass


def validate_github_url(url: str) -> Tuple[str, str]:
    """
    Validate GitHub URL and extract org/repo.
    
    Accepts:
    - HTTPS: https://github.com/{org}/{repo}
    - HTTPS with .git: https://github.com/{org}/{repo}.git
    - SSH: git@github.com:{org}/{repo}.git
    
    Args:
        url: GitHub repository URL
        
    Returns:
        tuple: (organization, repository)
        
    Raises:
        GitHubURLError: If URL format is invalid
        
    Examples:
        >>> validate_github_url("https://github.com/facebook/react")
        ('facebook', 'react')
        >>> validate_github_url("git@github.com:torvalds/linux.git")
        ('torvalds', 'linux')
    """
    if not url or not isinstance(url, str):
        raise GitHubURLError("URL must be a non-empty string")
    
    url = url.strip()
    
    # HTTPS pattern
    https_pattern = r'^https://github\.com/([a-zA-Z0-9_-]+)/([a-zA-Z0-9_.-]+?)(\.git)?/?$'
    # SSH pattern  
    ssh_pattern = r'^git@github\.com:([a-zA-Z0-9_-]+)/([a-zA-Z0-9_.-]+?)(\.git)?$'
    
    match = re.match(https_pattern, url) or re.match(ssh_pattern, url)
    
    if not match:
        raise GitHubURLError(
            f"Invalid GitHub URL format. Expected:\n"
            f"  - https://github.com/org/repo\n"
            f"  - git@github.com:org/repo.git\n"
            f"Got: {url}"
        )
    
    org, repo = match.group(1), match.group(2)
    
    # Remove .git suffix if present
    if repo.endswith('.git'):
        repo = repo[:-4]
    
    return (org, repo)


def is_valid_github_url(url: str) -> bool:
    """
    Check if URL is a valid GitHub URL without raising exception.
    
    Args:
        url: GitHub repository URL
        
    Returns:
        bool: True if valid, False otherwise
    """
    try:
        validate_github_url(url)
        return True
    except GitHubURLError:
        return False

