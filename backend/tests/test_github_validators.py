"""
Tests for GitHub URL validation

PRD Reference: PRD.md p.23
TASK: TASK-201
"""

import pytest
from github.validators import validate_github_url, is_valid_github_url, GitHubURLError


class TestValidateGitHubURL:
    """Test GitHub URL validation function"""
    
    def test_valid_https_url(self):
        """Test valid HTTPS URL"""
        org, repo = validate_github_url("https://github.com/facebook/react")
        assert org == "facebook"
        assert repo == "react"
    
    def test_valid_https_url_with_git_suffix(self):
        """Test HTTPS URL with .git suffix"""
        org, repo = validate_github_url("https://github.com/microsoft/vscode.git")
        assert org == "microsoft"
        assert repo == "vscode"
    
    def test_valid_https_url_with_trailing_slash(self):
        """Test HTTPS URL with trailing slash"""
        org, repo = validate_github_url("https://github.com/torvalds/linux/")
        assert org == "torvalds"
        assert repo == "linux"
    
    def test_valid_ssh_url(self):
        """Test valid SSH URL"""
        org, repo = validate_github_url("git@github.com:nodejs/node.git")
        assert org == "nodejs"
        assert repo == "node"
    
    def test_org_with_dash(self):
        """Test organization name with dash"""
        org, repo = validate_github_url("https://github.com/some-org/some-repo")
        assert org == "some-org"
        assert repo == "some-repo"
    
    def test_org_with_underscore(self):
        """Test organization name with underscore"""
        org, repo = validate_github_url("https://github.com/some_org/some_repo")
        assert org == "some_org"
        assert repo == "some_repo"
    
    def test_repo_with_dots(self):
        """Test repository name with dots"""
        org, repo = validate_github_url("https://github.com/user/my.repo.name")
        assert org == "user"
        assert repo == "my.repo.name"
    
    def test_invalid_url_empty(self):
        """Test empty URL"""
        with pytest.raises(GitHubURLError):
            validate_github_url("")
    
    def test_invalid_url_not_github(self):
        """Test non-GitHub URL"""
        with pytest.raises(GitHubURLError):
            validate_github_url("https://gitlab.com/user/repo")
    
    def test_invalid_url_missing_repo(self):
        """Test URL without repository"""
        with pytest.raises(GitHubURLError):
            validate_github_url("https://github.com/facebook")
    
    def test_invalid_url_wrong_format(self):
        """Test completely wrong format"""
        with pytest.raises(GitHubURLError):
            validate_github_url("not a url")
    
    def test_invalid_url_none(self):
        """Test None value"""
        with pytest.raises(GitHubURLError):
            validate_github_url(None)


class TestIsValidGitHubURL:
    """Test is_valid_github_url helper function"""
    
    def test_valid_url_returns_true(self):
        """Test valid URL returns True"""
        assert is_valid_github_url("https://github.com/facebook/react") is True
    
    def test_invalid_url_returns_false(self):
        """Test invalid URL returns False"""
        assert is_valid_github_url("not a url") is False
        assert is_valid_github_url("https://gitlab.com/user/repo") is False
        assert is_valid_github_url("") is False

