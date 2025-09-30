/**
 * Visualization Page - Code Map Display
 * 
 * PRD Reference: PRD.md p.53, Visualization Screen
 * TASK: TASK-605
 */

import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import ReactFlow, {
  Controls,
  Background,
  MiniMap,
  useNodesState,
  useEdgesState,
} from 'reactflow';
import 'reactflow/dist/style.css';
import { getAnalysis, pollAnalysis } from '../api/analysis';
import { AnalysisResult } from '../types/analysis';

const Visualization: React.FC = () => {
  const { analysisId } = useParams<{ analysisId: string }>();
  const navigate = useNavigate();
  
  const [nodes, setNodes, onNodesChange] = useNodesState([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);
  const [analysis, setAnalysis] = useState<AnalysisResult | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!analysisId) return;

    // Poll for completion
    pollAnalysis(
      analysisId,
      (status) => {
        // Update analysis state
        setAnalysis(status as AnalysisResult);
        
        // If completed, set graph data
        if (status.status === 'completed' && status.graph_data) {
          setNodes(status.graph_data.nodes.map((node, idx) => ({
            id: node.id,
            position: { x: (idx % 5) * 250, y: Math.floor(idx / 5) * 150 },
            data: node.data,
            style: getNodeStyle(node.data.health)
          })));
          setEdges(status.graph_data.edges);
          setLoading(false);
        }
      }
    ).catch((err) => {
      setError(err.message);
      setLoading(false);
    });
  }, [analysisId, setNodes, setEdges]);

  const getNodeStyle = (health: string) => {
    const styles = {
      green: { background: '#ECFDF5', border: '2px solid #10B981' },
      yellow: { background: '#FFFBEB', border: '2px solid #F59E0B' },
      red: { background: '#FEF2F2', border: '2px solid #EF4444' },
    };
    return {
      ...(styles[health as keyof typeof styles] || styles.green),
      padding: 10,
      borderRadius: 5,
      fontSize: 12,
    };
  };

  if (loading) {
    return (
      <div style={{ height: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center', flexDirection: 'column' }}>
        <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>🔄</div>
        <div style={{ fontSize: '1.5rem', color: '#3B82F6' }}>
          {analysis?.status === 'processing' ? 'Analyzing repository...' : 'Loading analysis...'}
        </div>
        {analysis && (
          <div style={{ marginTop: '1rem', color: '#6B7280' }}>
            {analysis.total_files && `${analysis.total_files} files`}
          </div>
        )}
      </div>
    );
  }

  if (error) {
    return (
      <div style={{ height: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center', flexDirection: 'column' }}>
        <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>❌</div>
        <div style={{ fontSize: '1.5rem', color: '#EF4444', marginBottom: '1rem' }}>Analysis Failed</div>
        <div style={{ color: '#6B7280' }}>{error}</div>
        <button
          onClick={() => navigate('/')}
          style={{
            marginTop: '2rem',
            padding: '0.5rem 1.5rem',
            background: '#3B82F6',
            color: 'white',
            border: 'none',
            borderRadius: '6px',
            cursor: 'pointer'
          }}
        >
          ← Back to Home
        </button>
      </div>
    );
  }

  return (
    <div style={{ height: '100vh', display: 'flex', flexDirection: 'column' }}>
      <div style={{
        padding: '1rem 1.5rem',
        background: '#1E40AF',
        color: 'white',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
          <button
            onClick={() => navigate('/')}
            style={{
              background: 'rgba(255,255,255,0.2)',
              border: 'none',
              color: 'white',
              padding: '0.5rem 1rem',
              borderRadius: '6px',
              cursor: 'pointer',
              fontSize: '0.9rem'
            }}
          >
            ← Back
          </button>
          <h1 style={{ margin: 0, fontSize: '1.5rem' }}>
            {analysis?.repository_name || 'Repository Analysis'}
          </h1>
        </div>
        {analysis && (
          <div style={{ fontSize: '0.9rem', opacity: 0.9 }}>
            {analysis.total_files} files • {analysis.total_loc?.toLocaleString()} LOC
          </div>
        )}
      </div>

      <div style={{
        padding: '0.75rem 1.5rem',
        background: '#3B82F6',
        color: 'white',
        display: 'flex',
        gap: '1.5rem',
        fontSize: '0.9rem'
      }}>
        <span><strong>Legend:</strong></span>
        <span>🟢 Healthy</span>
        <span>🟡 Warning</span>
        <span>🔴 Issues</span>
      </div>

      <div style={{ flex: 1 }}>
        <ReactFlow
          nodes={nodes}
          edges={edges}
          onNodesChange={onNodesChange}
          onEdgesChange={onEdgesChange}
          fitView
          onNodeClick={(event, node) => {
            console.log('Node:', node);
          }}
        >
          <Controls />
          <MiniMap
            nodeColor={(node) => {
              const health = node.data?.health;
              if (health === 'green') return '#10B981';
              if (health === 'yellow') return '#F59E0B';
              if (health === 'red') return '#EF4444';
              return '#gray';
            }}
          />
          <Background color="#aaa" gap={16} />
        </ReactFlow>
      </div>
    </div>
  );
};

export default Visualization;

