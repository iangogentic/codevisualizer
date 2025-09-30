/**
 * Home Page - GitHub URL Input
 * 
 * PRD Reference: PRD.md p.52, Main Screen Wireframe
 * TASK: TASK-403
 */

import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { startAnalysis } from '../api/analysis';

const Home: React.FC = () => {
  const [url, setUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  const validateUrl = (url: string): boolean => {
    const githubRegex = /^https:\/\/github\.com\/[\w-]+\/[\w.-]+\/?$/;
    return githubRegex.test(url.trim());
  };

  const handleAnalyze = async () => {
    setError(null);
    
    if (!url.trim()) {
      setError('Please enter a GitHub URL');
      return;
    }
    
    if (!validateUrl(url)) {
      setError('Invalid GitHub URL format. Expected: https://github.com/org/repo');
      return;
    }
    
    setLoading(true);
    
    try {
      const response = await startAnalysis({ github_url: url.trim() });
      navigate(`/analysis/${response.analysis_id}`);
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Failed to start analysis');
      setLoading(false);
    }
  };

  const tryExample = (exampleUrl: string) => {
    setUrl(exampleUrl);
    setError(null);
  };

  return (
    <div style={{ 
      minHeight: '100vh',
      background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      padding: '2rem'
    }}>
      <div style={{
        maxWidth: '800px',
        width: '100%',
        background: 'white',
        borderRadius: '16px',
        padding: '3rem',
        boxShadow: '0 20px 60px rgba(0,0,0,0.3)'
      }}>
        <h1 style={{
          fontSize: '3rem',
          fontWeight: 'bold',
          background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
          WebkitBackgroundClip: 'text',
          WebkitTextFillColor: 'transparent',
          marginBottom: '1rem',
          textAlign: 'center'
        }}>
          🎨 CodeMapper
        </h1>
        
        <p style={{
          fontSize: '1.2rem',
          color: '#6B7280',
          textAlign: 'center',
          marginBottom: '2rem'
        }}>
          Visualize and analyze any GitHub repository
        </p>

        <div style={{ marginBottom: '1.5rem' }}>
          <label style={{
            display: 'block',
            fontSize: '0.9rem',
            fontWeight: '600',
            color: '#374151',
            marginBottom: '0.5rem'
          }}>
            GitHub Repository URL
          </label>
          
          <input
            type="text"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleAnalyze()}
            placeholder="https://github.com/facebook/react"
            disabled={loading}
            style={{
              width: '100%',
              padding: '0.75rem 1rem',
              fontSize: '1rem',
              border: error ? '2px solid #EF4444' : '2px solid #E5E7EB',
              borderRadius: '8px',
              outline: 'none',
              transition: 'border-color 0.2s'
            }}
            onFocus={(e) => e.target.style.borderColor = '#667eea'}
            onBlur={(e) => e.target.style.borderColor = error ? '#EF4444' : '#E5E7EB'}
          />
          
          {error && (
            <div style={{
              marginTop: '0.5rem',
              color: '#EF4444',
              fontSize: '0.9rem'
            }}>
              ⚠️ {error}
            </div>
          )}
        </div>

        <button
          onClick={handleAnalyze}
          disabled={loading}
          style={{
            width: '100%',
            padding: '0.75rem 1.5rem',
            fontSize: '1.1rem',
            fontWeight: '600',
            color: 'white',
            background: loading ? '#9CA3AF' : 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
            border: 'none',
            borderRadius: '8px',
            cursor: loading ? 'not-allowed' : 'pointer',
            transition: 'transform 0.1s',
          }}
          onMouseDown={(e) => !loading && (e.currentTarget.style.transform = 'scale(0.98)')}
          onMouseUp={(e) => e.currentTarget.style.transform = 'scale(1)'}
        >
          {loading ? '🔄 Analyzing...' : '🔍 Analyze Repository'}
        </button>

        <div style={{
          marginTop: '2rem',
          paddingTop: '2rem',
          borderTop: '1px solid #E5E7EB'
        }}>
          <p style={{
            fontSize: '0.9rem',
            color: '#6B7280',
            marginBottom: '1rem',
            fontWeight: '600'
          }}>
            Try examples:
          </p>
          
          <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
            <ExampleButton onClick={() => tryExample('https://github.com/pallets/flask')}>
              Flask
            </ExampleButton>
            <ExampleButton onClick={() => tryExample('https://github.com/expressjs/express')}>
              Express.js
            </ExampleButton>
            <ExampleButton onClick={() => tryExample('https://github.com/spring-projects/spring-boot')}>
              Spring Boot
            </ExampleButton>
          </div>
        </div>

        <div style={{
          marginTop: '2rem',
          padding: '1rem',
          background: '#F3F4F6',
          borderRadius: '8px',
          fontSize: '0.85rem',
          color: '#6B7280'
        }}>
          <strong>Features:</strong> Interactive code maps • Health indicators • Dead code detection • Multi-language support
        </div>
      </div>
    </div>
  );
};

const ExampleButton: React.FC<{ onClick: () => void; children: React.ReactNode }> = ({ onClick, children }) => (
  <button
    onClick={onClick}
    style={{
      padding: '0.5rem 1rem',
      fontSize: '0.9rem',
      color: '#667eea',
      background: 'white',
      border: '2px solid #E5E7EB',
      borderRadius: '6px',
      cursor: 'pointer',
      transition: 'all 0.2s',
    }}
    onMouseEnter={(e) => {
      e.currentTarget.style.borderColor = '#667eea';
      e.currentTarget.style.background = '#F3F4F6';
    }}
    onMouseLeave={(e) => {
      e.currentTarget.style.borderColor = '#E5E7EB';
      e.currentTarget.style.background = 'white';
    }}
  >
    {children}
  </button>
);

export default Home;

