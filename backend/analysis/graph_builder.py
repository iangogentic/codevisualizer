"""
Graph data structure builder

PRD Reference: PRD.md p.45, Graph Data
TASK: TASK-303
"""

from typing import Dict, List, Any


class GraphBuilder:
    """Build graph data structure for frontend visualization"""
    
    @staticmethod
    def build_graph_from_emerge(
        file_metrics: Dict[str, Dict[str, int]],
        dependencies: Dict[str, List[str]] = None
    ) -> Dict[str, Any]:
        """
        Transform Emerge output to React Flow graph format
        
        PRD Reference: PRD.md p.45
        
        Args:
            file_metrics: File-level metrics from Emerge
            dependencies: File dependencies (optional)
            
        Returns:
            dict: Graph data with nodes and edges
        """
        nodes = []
        edges = []
        
        # Create nodes from files
        for file_path, metrics in file_metrics.items():
            node = GraphBuilder._create_node(file_path, metrics)
            nodes.append(node)
        
        # Create edges from dependencies (if available)
        if dependencies:
            for source, targets in dependencies.items():
                for target in targets:
                    edge = GraphBuilder._create_edge(source, target)
                    edges.append(edge)
        
        return {
            'nodes': nodes,
            'edges': edges
        }
    
    @staticmethod
    def _create_node(file_path: str, metrics: Dict[str, int]) -> Dict[str, Any]:
        """
        Create a single node from file metrics
        
        Args:
            file_path: Full file path
            metrics: File metrics (LOC, methods, etc.)
            
        Returns:
            dict: Node data
        """
        # Extract file name
        file_name = file_path.split('\\')[-1].split('/')[-1]
        
        # Calculate health
        health = GraphBuilder._calculate_health(metrics)
        
        return {
            'id': file_path,
            'label': file_name,
            'type': 'file',
            'data': {
                'path': file_path,
                'loc': metrics.get('sloc-in-file', 0),
                'methods': metrics.get('number-of-methods-in-file', 0),
                'complexity': metrics.get('number-of-methods-in-file', 0),  # Proxy for complexity
                'health': health,
                'language': GraphBuilder._detect_language_from_extension(file_name)
            }
        }
    
    @staticmethod
    def _create_edge(source: str, target: str) -> Dict[str, Any]:
        """
        Create an edge between two files
        
        Args:
            source: Source file path
            target: Target file path
            
        Returns:
            dict: Edge data
        """
        return {
            'id': f"{source}___{target}",
            'source': source,
            'target': target,
            'type': 'imports'
        }
    
    @staticmethod
    def _calculate_health(metrics: Dict[str, int]) -> str:
        """
        Calculate health status based on metrics
        
        PRD Reference: PRD.md p.47, Health Calculation
        
        Args:
            metrics: File metrics
            
        Returns:
            str: 'green', 'yellow', or 'red'
        """
        score = 100
        
        methods = metrics.get('number-of-methods-in-file', 0)
        loc = metrics.get('sloc-in-file', 0)
        
        # Reduce for high method count
        if methods > 30:
            score -= 30
        elif methods > 15:
            score -= 15
        
        # Reduce for high LOC
        if loc > 500:
            score -= 25
        elif loc > 300:
            score -= 10
        
        if score >= 80:
            return 'green'
        elif score >= 60:
            return 'yellow'
        else:
            return 'red'
    
    @staticmethod
    def _detect_language_from_extension(filename: str) -> str:
        """Detect language from file extension"""
        ext_map = {
            '.py': 'Python',
            '.js': 'JavaScript',
            '.ts': 'TypeScript',
            '.java': 'Java',
            '.cpp': 'C++',
            '.c': 'C',
            '.go': 'Go',
            '.rb': 'Ruby',
            '.kt': 'Kotlin',
            '.swift': 'Swift',
        }
        
        for ext, lang in ext_map.items():
            if filename.endswith(ext):
                return lang
        
        return 'Unknown'

