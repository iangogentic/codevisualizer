import { Node, Edge } from 'reactflow';

export interface EmergeMetrics {
  'number-of-methods-in-file': number;
  'sloc-in-file': number;
}

export interface EmergeData {
  'analysis-name': string;
  statistics: {
    'scanned_files': number;
    'total_runtime': string;
  };
  'overall-metrics': {
    'avg-number-of-methods-in-file': number;
    'avg-sloc-in-file': number;
    'total-sloc-in-files': number;
  };
  'local-metrics': {
    [filePath: string]: EmergeMetrics;
  };
}

/**
 * Calculate health status based on code metrics
 * PRD Reference: PRD.md p.47 - Health Calculation Algorithm
 */
function calculateHealth(metrics: EmergeMetrics): 'green' | 'yellow' | 'red' {
  let score = 100;
  
  // Reduce for high method count (complexity indicator)
  if (metrics['number-of-methods-in-file'] > 30) score -= 30;
  else if (metrics['number-of-methods-in-file'] > 15) score -= 15;
  
  // Reduce for high LOC
  if (metrics['sloc-in-file'] > 500) score -= 25;
  else if (metrics['sloc-in-file'] > 300) score -= 10;
  
  if (score >= 80) return 'green';
  else if (score >= 60) return 'yellow';
  else return 'red';
}

/**
 * Get color styling based on health status
 */
function getHealthStyle(health: 'green' | 'yellow' | 'red') {
  const styles = {
    green: { background: '#ECFDF5', border: '2px solid #10B981' },
    yellow: { background: '#FFFBEB', border: '2px solid #F59E0B' },
    red: { background: '#FEF2F2', border: '2px solid #EF4444' },
  };
  return styles[health];
}

/**
 * Extract file name from full path
 */
function getFileName(filePath: string): string {
  return filePath.split(/[\\/]/).pop() || filePath;
}

/**
 * Calculate node position in a simple grid layout
 */
function calculatePosition(index: number, totalNodes: number): { x: number; y: number } {
  const nodesPerRow = Math.ceil(Math.sqrt(totalNodes));
  const row = Math.floor(index / nodesPerRow);
  const col = index % nodesPerRow;
  
  return {
    x: col * 250,
    y: row * 150,
  };
}

/**
 * Parse Emerge JSON output and convert to React Flow format
 * 
 * @param emergeData - The JSON data from Emerge analysis
 * @returns Object containing nodes and edges for React Flow
 */
export function parseEmergeOutput(emergeData: EmergeData): { nodes: Node[]; edges: Edge[] } {
  const nodes: Node[] = [];
  const edges: Edge[] = [];
  
  const filePaths = Object.keys(emergeData['local-metrics']);
  
  // Create nodes from files
  filePaths.forEach((filePath, index) => {
    const metrics = emergeData['local-metrics'][filePath];
    const fileName = getFileName(filePath);
    const health = calculateHealth(metrics);
    const style = getHealthStyle(health);
    
    nodes.push({
      id: filePath,
      position: calculatePosition(index, filePaths.length),
      data: {
        label: `📄 ${fileName}`,
        filePath,
        methods: metrics['number-of-methods-in-file'],
        loc: metrics['sloc-in-file'],
        health,
      },
      style: {
        ...style,
        padding: 10,
        borderRadius: 5,
        fontSize: 12,
        minWidth: 150,
      },
    });
  });
  
  // Note: Emerge's simple output doesn't include dependency edges
  // We'll add a note about this and use the GraphML file for full dependencies
  // For now, we're just visualizing the files with health indicators
  
  return { nodes, edges };
}

/**
 * Load Emerge JSON file
 */
export async function loadEmergeData(jsonPath: string): Promise<EmergeData> {
  const response = await fetch(jsonPath);
  if (!response.ok) {
    throw new Error(`Failed to load Emerge data: ${response.statusText}`);
  }
  return response.json();
}

