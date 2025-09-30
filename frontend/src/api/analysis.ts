/**
 * Analysis API methods
 * 
 * PRD Reference: PRD.md p.44-46
 * TASK: TASK-402
 */

import apiClient from './client';

export interface AnalyzeRequest {
  github_url: string;
  options?: {
    detect_duplicates?: boolean;
    detect_dead_code?: boolean;
    max_files?: number;
  };
}

export interface AnalyzeResponse {
  analysis_id: string;
  status: string;
  estimated_time: number;
  message: string;
}

export interface AnalysisStatus {
  id: string;
  status: 'pending' | 'processing' | 'completed' | 'failed';
  github_url: string;
  repository_name: string;
  commit_sha?: string;
  created_at: string;
  completed_at?: string;
  error_message?: string;
  
  // Metadata
  total_files?: number;
  total_loc?: number;
  primary_language?: string;
  languages?: Record<string, number>;
  
  // Results
  metrics?: any;
  graph_data?: {
    nodes: any[];
    edges: any[];
  };
  health_scores?: any;
  dead_code?: any;
  duplicates?: any;
}

/**
 * Start analysis of a GitHub repository
 * PRD Reference: PRD.md p.44
 */
export const startAnalysis = async (
  request: AnalyzeRequest
): Promise<AnalyzeResponse> => {
  const response = await apiClient.post<AnalyzeResponse>('/api/analyze', request);
  return response.data;
};

/**
 * Get analysis status and results
 * PRD Reference: PRD.md p.45
 */
export const getAnalysis = async (
  analysisId: string
): Promise<AnalysisStatus> => {
  const response = await apiClient.get<AnalysisStatus>(`/api/analysis/${analysisId}`);
  return response.data;
};

/**
 * Poll for analysis completion
 * 
 * @param analysisId - UUID of analysis
 * @param onProgress - Callback for progress updates
 * @param interval - Polling interval in ms (default: 2000)
 */
export const pollAnalysis = async (
  analysisId: string,
  onProgress: (status: AnalysisStatus) => void,
  interval: number = 2000
): Promise<AnalysisStatus> => {
  return new Promise((resolve, reject) => {
    const poll = async () => {
      try {
        const status = await getAnalysis(analysisId);
        onProgress(status);
        
        if (status.status === 'completed') {
          resolve(status);
        } else if (status.status === 'failed') {
          reject(new Error(status.error_message || 'Analysis failed'));
        } else {
          // Continue polling
          setTimeout(poll, interval);
        }
      } catch (error) {
        reject(error);
      }
    };
    
    poll();
  });
};

