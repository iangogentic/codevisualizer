"""
Emerge analysis wrapper

PRD Reference: PRD.md p.24, F2.0
TASK: TASK-301
"""

import sys
import os
import json
from pathlib import Path
from typing import Dict, Any, Optional
import tempfile
import yaml


class EmergeAnalyzer:
    """Wrapper for Emerge code analysis engine"""
    
    def __init__(self, emerge_path: Optional[str] = None):
        """
        Initialize Emerge analyzer
        
        Args:
            emerge_path: Path to Emerge installation (auto-detect if None)
        """
        if emerge_path is None:
            # Auto-detect emerge directory (relative to backend)
            current_dir = Path(__file__).parent.parent.parent
            emerge_path = current_dir / 'emerge'
        
        self.emerge_path = Path(emerge_path)
        
        if not self.emerge_path.exists():
            raise FileNotFoundError(f"Emerge not found at: {self.emerge_path}")
        
        # Add emerge to Python path
        if str(self.emerge_path) not in sys.path:
            sys.path.insert(0, str(self.emerge_path))
    
    def create_config(self, repo_path: str, language: str = 'py') -> str:
        """
        Create Emerge config file for analysis
        
        Args:
            repo_path: Path to repository to analyze
            language: Primary language (py, javascript, java, etc.)
            
        Returns:
            str: Path to config file
        """
        output_dir = tempfile.mkdtemp(prefix='emerge_output_')
        
        config = {
            'project_name': 'analysis',
            'loglevel': 'info',
            'analyses': [
                {
                    'analysis_name': 'code_analysis',
                    'source_directory': str(repo_path),
                    'only_permit_languages': [language],
                    'file_scan': [
                        'number_of_methods',
                        'source_lines_of_code',
                        'dependency_graph',
                    ],
                    'export': [
                        {'directory': output_dir},
                        'json',
                        'graphml',
                    ]
                }
            ]
        }
        
        config_file = tempfile.NamedTemporaryFile(
            mode='w',
            suffix='.yaml',
            delete=False
        )
        yaml.dump(config, config_file)
        config_file.close()
        
        return config_file.name
    
    def run_analysis(self, repo_path: str, language: str = 'py') -> Dict[str, Any]:
        """
        Run Emerge analysis on repository
        
        Args:
            repo_path: Path to repository
            language: Primary language
            
        Returns:
            dict: Analysis results with metrics and graph data
        """
        # Create config
        config_file = self.create_config(repo_path, language)
        
        try:
            # Import Emerge
            from emerge.appear import Emerge
            
            # Run analysis
            emerge = Emerge(config_file)
            emerge.start()
            
            # Parse output
            output_dir = self._get_output_dir(config_file)
            results = self._parse_output(output_dir)
            
            return results
            
        finally:
            # Cleanup config file
            if os.path.exists(config_file):
                os.unlink(config_file)
    
    def _get_output_dir(self, config_file: str) -> str:
        """Extract output directory from config"""
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
        return config['analyses'][0]['export'][0]['directory']
    
    def _parse_output(self, output_dir: str) -> Dict[str, Any]:
        """
        Parse Emerge output files
        
        Args:
            output_dir: Directory containing Emerge output
            
        Returns:
            dict: Parsed analysis results
        """
        # Find JSON output file
        output_path = Path(output_dir)
        json_files = list(output_path.glob('*.json'))
        
        if not json_files:
            raise FileNotFoundError(f"No JSON output found in {output_dir}")
        
        # Load JSON
        with open(json_files[0], 'r') as f:
            data = json.load(f)
        
        # Transform to our format
        result = {
            'statistics': data.get('statistics', {}),
            'overall_metrics': data.get('overall-metrics', {}),
            'file_metrics': data.get('local-metrics', {}),
            'analysis_name': data.get('analysis-name', ''),
        }
        
        return result
    
    def detect_language(self, repo_path: str) -> str:
        """
        Auto-detect primary language in repository
        
        Args:
            repo_path: Path to repository
            
        Returns:
            str: Detected language (py, javascript, java, etc.)
        """
        # Simple detection based on file extensions
        path = Path(repo_path)
        
        extensions = {
            '.py': 'py',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.java': 'java',
            '.cpp': 'cpp',
            '.c': 'c',
            '.go': 'go',
            '.rb': 'ruby',
        }
        
        counts = {}
        for ext, lang in extensions.items():
            count = len(list(path.rglob(f'*{ext}')))
            if count > 0:
                counts[lang] = count
        
        if not counts:
            return 'py'  # Default
        
        # Return language with most files
        return max(counts, key=counts.get)

