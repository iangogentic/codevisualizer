# Quick Start Guide: Forking Emerge for Code Visualization

## Option 1: Fork Emerge (RECOMMENDED)

### Prerequisites
- Python 3.8+
- Node.js 18+
- Git
- GitHub account
- Code editor (VS Code recommended)

---

## Phase 1: Validation (This Weekend - 8 hours)

### Step 1.1: Test Emerge Locally (2 hours)

```bash
# Clone Emerge
git clone https://github.com/glato/emerge.git
cd emerge

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate
# Or (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Test on a sample repository
# Clone any GitHub repo locally first
cd ..
git clone https://github.com/facebook/react.git
cd emerge

# Run analysis
python -m emerge --config-file ./configs/python_analysis.yaml ../react

# Check output (should generate files in output/)
```

**Expected Output:**
- Dependency graph files
- JSON data
- GraphML file
- HTML visualization (basic)

**Validation Checklist:**
- [ ] Emerge runs without errors
- [ ] Output files are generated
- [ ] Dependencies are detected
- [ ] Code is readable and understandable
- [ ] You can see where to add features

**If this fails → Consider CodeCharta or Hybrid approach**

---

### Step 1.2: Create React Prototype (4 hours)

```bash
# In a new directory
npx create-react-app code-visualizer-frontend --template typescript
cd code-visualizer-frontend

# Install React Flow and dependencies
npm install reactflow
npm install @xyflow/react
npm install tailwindcss postcss autoprefixer
npx tailwindcss init -p

# Install utilities
npm install axios
npm install zustand  # state management
```

**Create a quick prototype:**

`src/App.tsx`:
```typescript
import React, { useCallback } from 'react';
import ReactFlow, {
  Node,
  Edge,
  addEdge,
  Connection,
  useNodesState,
  useEdgesState,
  Controls,
  Background,
} from 'reactflow';
import 'reactflow/dist/style.css';

// Sample data (replace with Emerge output parser)
const initialNodes: Node[] = [
  { id: '1', position: { x: 0, y: 0 }, data: { label: 'Module A' } },
  { id: '2', position: { x: 200, y: 0 }, data: { label: 'Module B' } },
  { id: '3', position: { x: 100, y: 100 }, data: { label: 'Module C' } },
];

const initialEdges: Edge[] = [
  { id: 'e1-2', source: '1', target: '2', animated: true },
  { id: 'e1-3', source: '1', target: '3' },
];

function App() {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  const onConnect = useCallback(
    (params: Connection) => setEdges((eds) => addEdge(params, eds)),
    [setEdges]
  );

  return (
    <div style={{ width: '100vw', height: '100vh' }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        fitView
      >
        <Controls />
        <Background />
      </ReactFlow>
    </div>
  );
}

export default App;
```

```bash
# Run the prototype
npm start
```

**Expected Result:**
- Interactive graph with nodes and edges
- Can drag nodes
- Can zoom/pan
- Professional looking UI

**Validation Checklist:**
- [ ] React Flow renders correctly
- [ ] Interactions work (drag, zoom, pan)
- [ ] You can customize node appearance
- [ ] Performance is acceptable
- [ ] You understand how to integrate Emerge data

**If this works → You're ready to proceed!**

---

### Step 1.3: Integration Test (2 hours)

**Goal:** Parse Emerge's JSON output and display in React Flow

```typescript
// src/utils/emergeParser.ts
export interface EmergeNode {
  entity_name: string;
  dependencies: string[];
  scanned_file_name: string;
  // Add more fields as needed
}

export function parseEmergeOutput(jsonData: any): { nodes: Node[], edges: Edge[] } {
  const nodes: Node[] = [];
  const edges: Edge[] = [];
  
  // Parse Emerge JSON and create React Flow nodes/edges
  // This is a simplified example
  jsonData.entities?.forEach((entity: EmergeNode, index: number) => {
    nodes.push({
      id: entity.entity_name,
      position: { x: index * 100, y: index * 50 }, // Temporary layout
      data: { 
        label: entity.entity_name,
        file: entity.scanned_file_name,
      },
    });
    
    entity.dependencies?.forEach((dep: string) => {
      edges.push({
        id: `${entity.entity_name}-${dep}`,
        source: entity.entity_name,
        target: dep,
      });
    });
  });
  
  return { nodes, edges };
}
```

**Test with real Emerge output:**
1. Run Emerge on a small project
2. Load the JSON output
3. Parse and visualize in React Flow
4. Verify all connections are correct

**Validation Checklist:**
- [ ] Can parse Emerge JSON
- [ ] Nodes appear correctly
- [ ] Edges show dependencies accurately
- [ ] No missing connections
- [ ] Layout is reasonable

**If this works → Green light to proceed with full development!**

---

## Phase 2: Full Development Setup (Week 1)

### Step 2.1: Fork and Setup Repository

```bash
# Fork Emerge on GitHub (via web interface)
# Then clone your fork
git clone https://github.com/YOUR_USERNAME/emerge.git
cd emerge

# Add upstream remote
git remote add upstream https://github.com/glato/emerge.git

# Create development branch
git checkout -b feature/web-ui-integration

# Set up project structure
mkdir -p web-ui
mkdir -p api
```

### Step 2.2: Backend API Setup

```bash
# In project root
pip install fastapi uvicorn python-multipart gitpython

# Create API directory
mkdir api
touch api/__init__.py
touch api/main.py
touch api/github.py
touch api/analyzer.py
```

**`api/main.py`:**
```python
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import subprocess
import json
import os

app = FastAPI()

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    github_url: str
    language: str = "python"

@app.post("/api/analyze")
async def analyze_repository(request: AnalyzeRequest):
    """Analyze a GitHub repository."""
    try:
        # TODO: Clone repo
        # TODO: Run Emerge analysis
        # TODO: Return JSON results
        return {"status": "success", "data": {}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

**`api/github.py`:**
```python
from git import Repo
import os
import tempfile
from pathlib import Path

class GitHubClient:
    """Handle GitHub repository operations."""
    
    @staticmethod
    def clone_repository(github_url: str) -> str:
        """Clone a GitHub repository to a temporary directory."""
        temp_dir = tempfile.mkdtemp()
        try:
            Repo.clone_from(github_url, temp_dir)
            return temp_dir
        except Exception as e:
            raise Exception(f"Failed to clone repository: {e}")
    
    @staticmethod
    def cleanup(directory: str):
        """Clean up temporary directory."""
        import shutil
        if os.path.exists(directory):
            shutil.rmtree(directory)
```

**`api/analyzer.py`:**
```python
import subprocess
import json
from pathlib import Path

class CodeAnalyzer:
    """Wrapper for Emerge analysis."""
    
    @staticmethod
    def analyze(repo_path: str, language: str = "python") -> dict:
        """Run Emerge analysis on a repository."""
        # TODO: Call Emerge's analysis functions directly
        # instead of subprocess for better integration
        
        config_file = f"./configs/{language}_analysis.yaml"
        output_dir = "./temp_output"
        
        # Run Emerge (simplified)
        result = subprocess.run(
            ["python", "-m", "emerge", 
             "--config-file", config_file,
             repo_path],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            raise Exception(f"Analysis failed: {result.stderr}")
        
        # Parse output
        output_file = Path(output_dir) / "analysis.json"
        with open(output_file, 'r') as f:
            data = json.load(f)
        
        return data
```

### Step 2.3: Frontend Integration

```bash
cd web-ui
# (Your React app from Step 1.2)

# Add API client
npm install axios
```

**`src/api/client.ts`:**
```typescript
import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

export interface AnalyzeResponse {
  status: string;
  data: {
    entities: any[];
    dependencies: any[];
  };
}

export const analyzeRepository = async (
  githubUrl: string,
  language: string = 'python'
): Promise<AnalyzeResponse> => {
  const response = await axios.post(`${API_BASE_URL}/api/analyze`, {
    github_url: githubUrl,
    language,
  });
  return response.data;
};
```

---

## Phase 3: Core Features (Weeks 2-6)

### Week 2: GitHub Integration
- [ ] Implement repository cloning
- [ ] Add authentication (GitHub OAuth)
- [ ] Handle public/private repos
- [ ] Add progress indicators

### Week 3: Visualization Enhancement
- [ ] Custom node styling
- [ ] Color coding by file type
- [ ] Size nodes by LOC
- [ ] Add tooltips with file info
- [ ] Implement smart layout algorithms

### Week 4: Code Quality Indicators
- [ ] Integrate jscpd for duplicates
- [ ] Add complexity metrics
- [ ] Implement red/green indicators
- [ ] Show health scores

### Week 5: Dead Code Detection
- [ ] Build call graph analyzer
- [ ] Detect unused exports
- [ ] Find orphaned files
- [ ] Highlight in visualization

### Week 6: Polish & Optimization
- [ ] Performance tuning
- [ ] Caching system
- [ ] Error handling
- [ ] Loading states
- [ ] Responsive design

---

## Useful Code Snippets

### Custom Node Component

```typescript
// src/components/CodeNode.tsx
import React from 'react';
import { Handle, Position } from 'reactflow';

interface CodeNodeData {
  label: string;
  file: string;
  health: 'good' | 'warning' | 'error';
  loc: number;
  hasDuplicates: boolean;
}

export function CodeNode({ data }: { data: CodeNodeData }) {
  const healthColor = {
    good: 'bg-green-100 border-green-500',
    warning: 'bg-yellow-100 border-yellow-500',
    error: 'bg-red-100 border-red-500',
  };

  return (
    <div className={`px-4 py-2 shadow-md rounded-md border-2 ${healthColor[data.health]}`}>
      <Handle type="target" position={Position.Top} />
      <div>
        <div className="font-bold text-sm">{data.label}</div>
        <div className="text-xs text-gray-600">{data.file}</div>
        <div className="text-xs mt-1">
          {data.loc} LOC
          {data.hasDuplicates && ' ⚠️ Duplicates'}
        </div>
      </div>
      <Handle type="source" position={Position.Bottom} />
    </div>
  );
}
```

### Layout Algorithm

```typescript
// src/utils/layout.ts
import { Node, Edge } from 'reactflow';
import dagre from 'dagre';

export function getLayoutedElements(
  nodes: Node[],
  edges: Edge[],
  direction = 'TB'
) {
  const dagreGraph = new dagre.graphlib.Graph();
  dagreGraph.setDefaultEdgeLabel(() => ({}));
  dagreGraph.setGraph({ rankdir: direction });

  nodes.forEach((node) => {
    dagreGraph.setNode(node.id, { width: 150, height: 50 });
  });

  edges.forEach((edge) => {
    dagreGraph.setEdge(edge.source, edge.target);
  });

  dagre.layout(dagreGraph);

  const layoutedNodes = nodes.map((node) => {
    const nodeWithPosition = dagreGraph.node(node.id);
    return {
      ...node,
      position: {
        x: nodeWithPosition.x,
        y: nodeWithPosition.y,
      },
    };
  });

  return { nodes: layoutedNodes, edges };
}
```

---

## Testing Strategy

### Unit Tests
```bash
# Backend
pip install pytest pytest-cov
pytest tests/ --cov=api

# Frontend
npm test -- --coverage
```

### Integration Tests
```bash
# Test full flow: GitHub URL → Analysis → Visualization
npm run test:e2e
```

### Performance Tests
```bash
# Test with large repositories
python scripts/performance_test.py
```

---

## Deployment Checklist

### Development
- [ ] Local development works
- [ ] Can analyze test repositories
- [ ] Visualization renders correctly
- [ ] All features functional

### Staging
- [ ] Deploy to test server
- [ ] Test with real GitHub repos
- [ ] Performance acceptable
- [ ] Error handling works

### Production
- [ ] Set up CI/CD pipeline
- [ ] Configure domain and SSL
- [ ] Set up monitoring
- [ ] Documentation complete
- [ ] User onboarding flow

---

## Common Issues & Solutions

### Issue: Emerge analysis is slow
**Solution:** 
- Run analysis in background worker
- Use Redis queue
- Show progress indicators
- Cache results

### Issue: React Flow performance with large graphs
**Solution:**
- Implement virtualization
- Use clustering for large graphs
- Lazy load node details
- Optimize edge rendering

### Issue: GitHub API rate limits
**Solution:**
- Implement caching
- Use GitHub PAT
- Show rate limit status
- Batch requests

---

## Resources

### Documentation
- Emerge: https://github.com/glato/emerge
- React Flow: https://reactflow.dev/
- FastAPI: https://fastapi.tiangolo.com/
- TailwindCSS: https://tailwindcss.com/

### Communities
- Emerge Issues: https://github.com/glato/emerge/issues
- React Flow Discord: https://discord.gg/Bqt6xrs
- Stack Overflow: Tag your questions appropriately

### Example Projects
- Look at CodeCharta for 3D inspiration
- Check React Flow examples gallery
- Study Sourcegraph's UI patterns

---

## Timeline Checklist

### Week 1: ✅ Setup & Validation
- [x] Test Emerge
- [x] Build React prototype
- [x] Integration test successful
- [ ] Fork repository
- [ ] Set up development environment

### Week 2: GitHub Integration
- [ ] Clone repositories
- [ ] OAuth authentication
- [ ] Error handling
- [ ] Progress indicators

### Week 3-4: Core Visualization
- [ ] Parse Emerge output
- [ ] Render interactive graph
- [ ] Custom node components
- [ ] Layout algorithms
- [ ] UI polish

### Week 5-6: Code Quality Features
- [ ] Integrate jscpd
- [ ] Dead code detection
- [ ] Health indicators
- [ ] Metrics dashboard

### Week 7-8: Polish & Deploy
- [ ] Performance optimization
- [ ] Testing
- [ ] Documentation
- [ ] Deployment
- [ ] User testing

---

## Success Metrics

### Technical
- [ ] Analyzes repos in < 30 seconds (small repos)
- [ ] Renders graphs with 100+ nodes smoothly
- [ ] 95%+ uptime
- [ ] < 500ms API response times

### User Experience
- [ ] Intuitive UI (no tutorial needed)
- [ ] Clear visualizations
- [ ] Helpful error messages
- [ ] Mobile responsive

### Business
- [ ] 10+ test users
- [ ] Positive feedback
- [ ] Working prototype deployed
- [ ] Documentation complete

---

## Next Steps

1. ✅ **Right now:** Run the validation tests (Phase 1)
2. ⏭️ **This week:** If validation passes, fork Emerge and set up project
3. ⏭️ **Week 2:** Start building GitHub integration
4. ⏭️ **Week 3-8:** Follow the development roadmap
5. ⏭️ **Week 10:** Launch MVP!

---

**Remember:** 
- Start small, iterate quickly
- Test with real repositories early
- Get user feedback continuously
- Don't over-engineer initially
- You can always refactor later

**Good luck! 🚀**

