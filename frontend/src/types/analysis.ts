/**
 * Type definitions for analysis data
 * 
 * PRD Reference: PRD.md p.45
 */

export interface NodeData {
  label: string;
  path: string;
  loc: number;
  methods: number;
  complexity: number;
  health: 'green' | 'yellow' | 'red';
  language: string;
}

export interface GraphData {
  nodes: Array<{
    id: string;
    label: string;
    type: string;
    data: NodeData;
  }>;
  edges: Array<{
    id: string;
    source: string;
    target: string;
    type: string;
  }>;
}

export interface AnalysisMetrics {
  'avg-number-of-methods-in-file'?: number;
  'avg-sloc-in-file'?: number;
  'total-sloc-in-files'?: number;
}

export interface AnalysisResult {
  id: string;
  status: 'pending' | 'processing' | 'completed' | 'failed';
  github_url: string;
  repository_name: string;
  total_files?: number;
  total_loc?: number;
  primary_language?: string;
  graph_data?: GraphData;
  metrics?: AnalysisMetrics;
  error_message?: string;
}

