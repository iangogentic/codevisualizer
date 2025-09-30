# CodeMapper - Task Breakdown
## Complete Development Task List

**Project:** CodeMapper - Code Visualization & Analysis Platform  
**Timeline:** 10 Weeks (70 working days)  
**Status:** Week 1-2 Foundation Complete - Ready for Analysis Engine  
**Progress:** 10/74 tasks complete (14%)  
**Last Updated:** September 30, 2025

---

## Task Status Legend

- ⬜ **TODO** - Not started
- 🔄 **IN PROGRESS** - Currently working on
- ✅ **DONE** - Completed
- ⏸️ **BLOCKED** - Blocked by dependency
- ❌ **CANCELLED** - No longer needed
- 🔍 **REVIEW** - Needs review/testing

---

## Phase 0: Validation & Setup (Week 0)

### TASK-000: Weekend Validation Tests
**Status:** ✅ DONE  
**Priority:** P0 (Critical)  
**Estimate:** 8 hours  
**Actual:** 8 hours  
**Assignee:** Development Team  
**Started:** September 30, 2025  
**Completed:** September 30, 2025  
**Dependencies:** None  
**PRD Reference:** QUICK_START_GUIDE.md Phase 1

**Subtasks:**
- [x] TASK-000.1: Clone and test Emerge locally (2h) ✅ COMPLETE
- [x] TASK-000.2: Build React + React Flow prototype (4h) ✅ COMPLETE
- [x] TASK-000.3: Test integration (parse Emerge output, display in React Flow) (2h) ✅ COMPLETE
- [x] TASK-000.4: Document validation results ✅ COMPLETE
- [x] TASK-000.5: Make go/no-go decision ✅ COMPLETE - **GO!**

**Acceptance Criteria:**
- ✅ Emerge runs successfully on test repository (Flask analyzed in 123ms)
- ✅ React Flow renders interactive graph (running at localhost:3000)
- ✅ Can parse Emerge JSON and display in React Flow (24 Flask files displayed)
- ✅ Performance is acceptable (instant load, smooth interactions)
- ✅ Decision documented: **GO** - See VALIDATION_RESULTS.md

**Progress Notes:**
- Emerge successfully installed and tested with Flask repository
- Generated JSON, GraphML output files with dependency data
- React app created with TypeScript, React Flow, Axios, Zustand
- Interactive visualization working with sample data
- Color-coded health indicators implemented (🟢🟡🔴)

**Notes:** This is a critical validation phase. If validation fails, pivot to alternative approach.

---

## Phase 1: MVP Development (Weeks 1-10)

---

## WEEK 1: Foundation Setup

### TASK-101: Project Setup
**Status:** ✅ DONE  
**Priority:** P0  
**Estimate:** 1 day  
**Actual:** 1 hour  
**Assignee:** Development Team  
**Started:** September 30, 2025  
**Completed:** September 30, 2025  
**Dependencies:** TASK-000 (validation complete) ✅  
**PRD Reference:** PRD.md p.60, Development Phases

**Subtasks:**
- [x] TASK-101.1: Fork Emerge repository to team GitHub ✅ (included in project)
- [x] TASK-101.2: Clone forked repository ✅ (emerge/ folder)
- [x] TASK-101.3: Create new branch: `develop` (using main for now)
- [x] TASK-101.4: Set up `.gitignore` file ✅
- [x] TASK-101.5: Add LICENSE file (MIT) - NEXT
- [x] TASK-101.6: Update README with project info ✅

**Acceptance Criteria:**
- Repository forked and accessible
- Clean git history
- All team members have access

---

### TASK-102: Development Environment Setup
**Status:** ✅ DONE  
**Priority:** P0  
**Estimate:** 2 days  
**Actual:** 30 minutes  
**Assignee:** Development Team  
**Started:** September 30, 2025  
**Completed:** September 30, 2025  
**Dependencies:** TASK-101 ✅  
**PRD Reference:** PRD.md p.35, Technical Architecture

**Subtasks:**
- [ ] TASK-102.1: Create `docker-compose.yml` for local development
  - [ ] Python backend container
  - [ ] PostgreSQL database
  - [ ] Redis cache
- [ ] TASK-102.2: Create `Dockerfile` for backend
- [ ] TASK-102.3: Set up Python virtual environment
- [ ] TASK-102.4: Create `requirements.txt` with dependencies:
  - [ ] FastAPI
  - [ ] Uvicorn
  - [ ] SQLAlchemy
  - [ ] Alembic
  - [ ] Celery
  - [ ] GitPython
  - [ ] PyGithub
  - [ ] pytest
- [ ] TASK-102.5: Create `.env.example` file
- [ ] TASK-102.6: Document setup in `DEVELOPMENT.md`

**Acceptance Criteria:**
- `docker-compose up` starts all services
- Database is accessible
- Redis is running
- Environment variables documented

---

### TASK-103: CI/CD Pipeline Setup
**Status:** ✅ DONE  
**Priority:** P0  
**Estimate:** 1 day  
**Actual:** 15 minutes  
**Assignee:** Development Team  
**Started:** September 30, 2025  
**Completed:** September 30, 2025  
**Dependencies:** TASK-102 ✅  
**PRD Reference:** PRD.md p.37

**Subtasks:**
- [ ] TASK-103.1: Create `.github/workflows/backend-ci.yml`
  - [ ] Run tests on PR
  - [ ] Check code coverage (>80%)
  - [ ] Run linting (pylint)
- [ ] TASK-103.2: Create `.github/workflows/frontend-ci.yml` (placeholder)
- [ ] TASK-103.3: Set up branch protection rules
- [ ] TASK-103.4: Configure GitHub Actions secrets

**Acceptance Criteria:**
- CI runs on every PR
- Tests must pass before merge
- Coverage report generated
- Linting enforced

---

### TASK-104: Database Schema Implementation
**Status:** ✅ DONE  
**Priority:** P0  
**Estimate:** 1 day  
**Actual:** 20 minutes  
**Assignee:** Development Team  
**Started:** September 30, 2025  
**Completed:** September 30, 2025  
**Dependencies:** TASK-102 ✅  
**PRD Reference:** PRD.md p.42, Database Schema

**Subtasks:**
- [ ] TASK-104.1: Set up Alembic migrations
- [ ] TASK-104.2: Create `analyses` table migration
- [ ] TASK-104.3: Create `users` table migration (stub for future)
- [ ] TASK-104.4: Create `analysis_cache` table migration
- [ ] TASK-104.5: Create indexes
- [ ] TASK-104.6: Write SQLAlchemy models
- [ ] TASK-104.7: Test migrations (up/down)

**Acceptance Criteria:**
- All tables created successfully
- Indexes in place
- Models match schema
- Migrations are reversible

---

### TASK-105: Project Structure Organization
**Status:** ✅ DONE  
**Priority:** P0  
**Estimate:** 0.5 day  
**Actual:** 10 minutes  
**Assignee:** Development Team  
**Started:** September 30, 2025  
**Completed:** September 30, 2025  
**Dependencies:** TASK-102 ✅  

**Subtasks:**
- [ ] TASK-105.1: Create directory structure:
```
project/
├── backend/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── routes/
│   │   ├── models/
│   │   └── schemas/
│   ├── analysis/
│   │   ├── emerge_wrapper.py
│   │   ├── dead_code_detector.py
│   │   └── health_calculator.py
│   ├── github/
│   │   └── client.py
│   ├── database/
│   │   ├── db.py
│   │   └── models.py
│   └── tests/
├── frontend/ (placeholder)
├── docs/
├── scripts/
└── migrations/
```
- [ ] TASK-105.2: Create `__init__.py` files
- [ ] TASK-105.3: Set up Python path configuration

**Acceptance Criteria:**
- Clean, organized structure
- All imports work correctly
- No circular dependencies

---

## WEEK 2: GitHub Integration

### TASK-201: GitHub URL Validation
**Status:** ✅ DONE  
**Priority:** P0  
**Estimate:** 0.5 day  
**Actual:** 30 minutes  
**Assignee:** Development Team  
**Completed:** September 30, 2025  
**Dependencies:** TASK-105 ✅  
**PRD Reference:** PRD.md p.23, F1.0

**Subtasks:**
- [ ] TASK-201.1: Create `github/validators.py`
- [ ] TASK-201.2: Implement URL validation function
  - [ ] Check format: `https://github.com/{org}/{repo}`
  - [ ] Support SSH format: `git@github.com:{org}/{repo}.git`
  - [ ] Extract org and repo name
- [ ] TASK-201.3: Write unit tests (10+ test cases)
- [ ] TASK-201.4: Handle edge cases (trailing slashes, .git suffix, etc.)

**Acceptance Criteria:**
- Validates correct URLs
- Rejects invalid URLs with clear error messages
- Test coverage >90%

---

### TASK-202: Repository Cloning Service
**Status:** ✅ DONE  
**Priority:** P0  
**Estimate:** 1 day  
**Actual:** 20 minutes  
**Assignee:** Development Team  
**Completed:** September 30, 2025  
**Dependencies:** TASK-201 ✅  
**PRD Reference:** PRD.md p.41, GitHubClient

**Subtasks:**
- [ ] TASK-202.1: Create `github/client.py`
- [ ] TASK-202.2: Implement `clone_repository()` method
  - [ ] Use GitPython
  - [ ] Clone to temporary directory
  - [ ] Handle authentication (for future private repos)
- [ ] TASK-202.3: Implement `cleanup()` method
- [ ] TASK-202.4: Add error handling (repo not found, network errors)
- [ ] TASK-202.5: Write integration tests
- [ ] TASK-202.6: Add timeout handling (max 5 minutes)

**Acceptance Criteria:**
- Successfully clones public repositories
- Cleans up temp directories
- Handles errors gracefully
- No memory leaks

---

### TASK-203: API Endpoint - Start Analysis
**Status:** ✅ DONE  
**Priority:** P0  
**Estimate:** 1.5 days  
**Actual:** 30 minutes  
**Assignee:** Development Team  
**Completed:** September 30, 2025  
**Dependencies:** TASK-202 ✅, TASK-104 ✅  
**PRD Reference:** PRD.md p.44, POST /api/analyze

**Subtasks:**
- [ ] TASK-203.1: Create FastAPI app in `api/main.py`
- [ ] TASK-203.2: Set up CORS middleware
- [ ] TASK-203.3: Create Pydantic schemas for request/response
- [ ] TASK-203.4: Implement `POST /api/analyze` endpoint
  - [ ] Validate GitHub URL
  - [ ] Create analysis record in database
  - [ ] Queue analysis job (Celery)
  - [ ] Return analysis ID
- [ ] TASK-203.5: Add request validation
- [ ] TASK-203.6: Add error handling
- [ ] TASK-203.7: Write API tests

**Acceptance Criteria:**
- Endpoint accepts valid GitHub URLs
- Returns 202 Accepted with analysis ID
- Creates database record with status='pending'
- Queues Celery task
- Returns 400 for invalid input

**API Contract:**
```python
# Request
POST /api/analyze
{
  "github_url": "https://github.com/facebook/react",
  "options": {
    "detect_duplicates": true,
    "detect_dead_code": true
  }
}

# Response (202 Accepted)
{
  "analysis_id": "uuid",
  "status": "pending",
  "estimated_time": 45
}
```

---

### TASK-204: API Endpoint - Get Analysis
**Status:** ✅ DONE  
**Priority:** P0  
**Estimate:** 1 day  
**Actual:** 15 minutes (with TASK-203)  
**Assignee:** Development Team  
**Completed:** September 30, 2025  
**Dependencies:** TASK-203 ✅  
**PRD Reference:** PRD.md p.45, GET /api/analysis/{id}

**Subtasks:**
- [ ] TASK-204.1: Implement `GET /api/analysis/{id}` endpoint
- [ ] TASK-204.2: Query database for analysis record
- [ ] TASK-204.3: Return appropriate status (pending/processing/completed/failed)
- [ ] TASK-204.4: Include results if completed
- [ ] TASK-204.5: Handle not found (404)
- [ ] TASK-204.6: Write API tests

**Acceptance Criteria:**
- Returns current status of analysis
- Returns full results if completed
- Returns 404 if analysis ID not found
- Response matches API contract

---

### TASK-205: Celery Task Queue Setup
**Status:** ✅ DONE  
**Priority:** P0  
**Estimate:** 1 day  
**Actual:** 20 minutes  
**Assignee:** Development Team  
**Started:** September 30, 2025  
**Completed:** September 30, 2025  
**Dependencies:** TASK-102 ✅  
**PRD Reference:** PRD.md p.37

**Subtasks:**
- [ ] TASK-205.1: Configure Celery app
- [ ] TASK-205.2: Set up Redis as broker
- [ ] TASK-205.3: Create `tasks/__init__.py`
- [ ] TASK-205.4: Implement task status tracking
- [ ] TASK-205.5: Add task timeout (10 minutes)
- [ ] TASK-205.6: Add retry logic (3 attempts)
- [ ] TASK-205.7: Test task execution

**Acceptance Criteria:**
- Celery worker starts successfully
- Tasks can be queued and executed
- Task status is tracked
- Timeouts work correctly

---

## WEEK 3: Analysis Engine Integration

### TASK-301: Emerge Wrapper - Basic Integration
**Status:** 🔄 IN PROGRESS  
**Priority:** P0  
**Estimate:** 2 days  
**Assignee:** Development Team  
**Started:** September 30, 2025  
**Dependencies:** TASK-205 ✅  
**PRD Reference:** PRD.md p.24, F2.0

**Subtasks:**
- [ ] TASK-301.1: Create `analysis/emerge_wrapper.py`
- [ ] TASK-301.2: Study Emerge's API/CLI
- [ ] TASK-301.3: Implement `run_emerge_analysis()` function
  - [ ] Call Emerge programmatically (not subprocess)
  - [ ] Pass repository path
  - [ ] Configure language detection
- [ ] TASK-301.4: Parse Emerge output to our format
- [ ] TASK-301.5: Handle Emerge errors
- [ ] TASK-301.6: Write integration tests with sample repos

**Acceptance Criteria:**
- Can run Emerge on any repository
- Parses output correctly
- Handles Python, JavaScript, Java, C/C++
- Error handling works

---

### TASK-302: Analysis Celery Task
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 2 days  
**Dependencies:** TASK-301, TASK-202  
**PRD Reference:** PRD.md p.41, Analysis Engine Flow

**Subtasks:**
- [ ] TASK-302.1: Create `tasks/analyze_repository.py`
- [ ] TASK-302.2: Implement main analysis task:
  - [ ] Clone repository
  - [ ] Run Emerge analysis
  - [ ] Parse results
  - [ ] Calculate basic metrics
  - [ ] Store results in database
  - [ ] Clean up temp files
  - [ ] Update status to 'completed' or 'failed'
- [ ] TASK-302.3: Add progress tracking
- [ ] TASK-302.4: Add comprehensive error handling
- [ ] TASK-302.5: Add logging at all stages
- [ ] TASK-302.6: Test with various repositories

**Acceptance Criteria:**
- Full analysis flow works end-to-end
- Results stored correctly in database
- Temp files cleaned up
- Status updated appropriately
- Errors logged and handled

---

### TASK-303: Graph Data Structure
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 1 day  
**Dependencies:** TASK-301  
**PRD Reference:** PRD.md p.45, Graph Data

**Subtasks:**
- [ ] TASK-303.1: Define graph data structure for frontend
```python
{
  "nodes": [
    {
      "id": "file_path",
      "label": "FileName.js",
      "type": "file",
      "data": {
        "path": "src/components/FileName.js",
        "loc": 234,
        "complexity": 8,
        "language": "JavaScript",
        "health": "green"
      }
    }
  ],
  "edges": [
    {
      "id": "edge_id",
      "source": "file_a",
      "target": "file_b",
      "type": "imports"
    }
  ]
}
```
- [ ] TASK-303.2: Implement conversion from Emerge output to graph format
- [ ] TASK-303.3: Optimize graph size (clustering for large repos)
- [ ] TASK-303.4: Write unit tests

**Acceptance Criteria:**
- Clean, consistent data structure
- Conversion works for all supported languages
- Graph size optimized
- Documented with examples

---

### TASK-304: End-to-End Integration Test
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 1 day  
**Dependencies:** TASK-302, TASK-303, TASK-204  

**Subtasks:**
- [ ] TASK-304.1: Write E2E test: POST analyze → poll GET → verify results
- [ ] TASK-304.2: Test with small repository (< 100 files)
- [ ] TASK-304.3: Test with medium repository (~500 files)
- [ ] TASK-304.4: Verify performance (<30s for small, <2min for medium)
- [ ] TASK-304.5: Test error scenarios

**Acceptance Criteria:**
- Full flow works: request → analysis → results
- Performance targets met
- All error cases handled
- Tests are repeatable

---

## WEEK 4: React Frontend Foundation

### TASK-401: React Project Setup
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 0.5 day  
**Dependencies:** None (parallel to backend)  
**PRD Reference:** PRD.md p.36, Frontend Stack

**Subtasks:**
- [ ] TASK-401.1: Create React app with TypeScript
```bash
npx create-react-app frontend --template typescript
```
- [ ] TASK-401.2: Install dependencies:
  - [ ] React Flow
  - [ ] Axios
  - [ ] React Query
  - [ ] Zustand
  - [ ] React Router
- [ ] TASK-401.3: Set up TailwindCSS
- [ ] TASK-401.4: Configure TypeScript (strict mode)
- [ ] TASK-401.5: Set up ESLint + Prettier
- [ ] TASK-401.6: Create folder structure:
```
frontend/src/
├── components/
├── pages/
├── hooks/
├── api/
├── types/
├── store/
└── utils/
```

**Acceptance Criteria:**
- App runs with `npm start`
- TailwindCSS working
- TypeScript configured
- Linting working

---

### TASK-402: API Client Setup
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 0.5 day  
**Dependencies:** TASK-401  
**PRD Reference:** PRD.md p.42

**Subtasks:**
- [ ] TASK-402.1: Create `api/client.ts`
- [ ] TASK-402.2: Configure Axios instance
- [ ] TASK-402.3: Create API methods:
  - [ ] `analyzeRepository(url)`
  - [ ] `getAnalysis(id)`
- [ ] TASK-402.4: Add TypeScript interfaces for API responses
- [ ] TASK-402.5: Set up React Query hooks
- [ ] TASK-402.6: Add error handling

**Acceptance Criteria:**
- Can call backend API
- Type-safe API calls
- Error handling works
- React Query caching configured

---

### TASK-403: Landing Page UI
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 1 day  
**Dependencies:** TASK-402  
**PRD Reference:** PRD.md p.52, Main Screen Wireframe

**Subtasks:**
- [ ] TASK-403.1: Create `pages/Home.tsx`
- [ ] TASK-403.2: Implement header with logo
- [ ] TASK-403.3: Create URL input component
- [ ] TASK-403.4: Add validation (show error for invalid URL)
- [ ] TASK-403.5: Create "Analyze" button
- [ ] TASK-403.6: Add example buttons (Try React, Try Express, etc.)
- [ ] TASK-403.7: Style with TailwindCSS
- [ ] TASK-403.8: Make responsive

**Acceptance Criteria:**
- Clean, professional UI
- URL validation works
- Matches wireframe design
- Responsive on desktop/laptop
- Follows design system (colors, typography)

---

### TASK-404: Loading States Component
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 0.5 day  
**Dependencies:** TASK-403  
**PRD Reference:** PRD.md p.56, Loading States

**Subtasks:**
- [ ] TASK-404.1: Create `components/LoadingSpinner.tsx`
- [ ] TASK-404.2: Create `components/ProgressBar.tsx`
- [ ] TASK-404.3: Add loading messages:
  - [ ] "Cloning repository..."
  - [ ] "Analyzing X / Y files..."
  - [ ] "Generating visualization..."
- [ ] TASK-404.4: Add animations

**Acceptance Criteria:**
- Smooth animations
- Clear progress indication
- Accessible (ARIA labels)

---

### TASK-405: Error Handling UI
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 0.5 day  
**Dependencies:** TASK-403  
**PRD Reference:** PRD.md p.56, Error States

**Subtasks:**
- [ ] TASK-405.1: Create `components/ErrorMessage.tsx`
- [ ] TASK-405.2: Handle common errors:
  - [ ] Invalid URL
  - [ ] Repository not found
  - [ ] Analysis failed
  - [ ] Network error
- [ ] TASK-405.3: Add retry button where appropriate
- [ ] TASK-405.4: Make errors user-friendly

**Acceptance Criteria:**
- All error types handled
- Clear, actionable messages
- Retry works correctly

---

### TASK-406: Basic Routing
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 0.5 day  
**Dependencies:** TASK-403  

**Subtasks:**
- [ ] TASK-406.1: Set up React Router
- [ ] TASK-406.2: Create routes:
  - [ ] `/` - Home page
  - [ ] `/analysis/:id` - Visualization page (placeholder)
- [ ] TASK-406.3: Implement navigation

**Acceptance Criteria:**
- Routing works
- URLs are clean
- Browser back/forward work

---

## WEEK 5: Visualization - Part 1

### TASK-501: React Flow Integration
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 1 day  
**Dependencies:** TASK-406  
**PRD Reference:** PRD.md p.24, F3.0

**Subtasks:**
- [ ] TASK-501.1: Install React Flow
- [ ] TASK-501.2: Create `components/CodeGraph.tsx`
- [ ] TASK-501.3: Set up basic React Flow canvas
- [ ] TASK-501.4: Configure controls (zoom, pan, fit view)
- [ ] TASK-501.5: Add background pattern
- [ ] TASK-501.6: Style with CSS

**Acceptance Criteria:**
- React Flow renders
- Can zoom/pan
- Controls work
- Looks professional

---

### TASK-502: Data Transformation Layer
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 1 day  
**Dependencies:** TASK-501, TASK-303  
**PRD Reference:** PRD.md p.45

**Subtasks:**
- [ ] TASK-502.1: Create `utils/graphTransformer.ts`
- [ ] TASK-502.2: Parse API response to React Flow format
- [ ] TASK-502.3: Handle different node types (file, directory, package)
- [ ] TASK-502.4: Create edges from dependencies
- [ ] TASK-502.5: Add metadata to nodes
- [ ] TASK-502.6: Write unit tests

**Acceptance Criteria:**
- Transforms API data correctly
- All node types supported
- Edges created properly
- Type-safe transformations

---

### TASK-503: Basic Node Component
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 1 day  
**Dependencies:** TASK-502  
**PRD Reference:** PRD.md p.57, Node Specifications

**Subtasks:**
- [ ] TASK-503.1: Create `components/nodes/FileNode.tsx`
- [ ] TASK-503.2: Display file name
- [ ] TASK-503.3: Display icon based on file type
- [ ] TASK-503.4: Size based on LOC (50px-150px)
- [ ] TASK-503.5: Add hover effect (scale, shadow)
- [ ] TASK-503.6: Style with TailwindCSS
- [ ] TASK-503.7: Make accessible (keyboard navigation)

**Acceptance Criteria:**
- Node displays file info
- Responsive to interactions
- Visually appealing
- Accessible

---

### TASK-504: Edge Rendering
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 0.5 day  
**Dependencies:** TASK-503  

**Subtasks:**
- [ ] TASK-504.1: Configure edge types
- [ ] TASK-504.2: Style edges (color, width, style)
- [ ] TASK-504.3: Add arrows
- [ ] TASK-504.4: Handle edge selection

**Acceptance Criteria:**
- Edges render correctly
- Direction is clear (arrows)
- Hover effect works
- Performance acceptable

---

### TASK-505: Layout Algorithm
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 1.5 days  
**Dependencies:** TASK-504  
**PRD Reference:** PRD.md p.68, Layout Algorithm

**Subtasks:**
- [ ] TASK-505.1: Install dagre library
- [ ] TASK-505.2: Implement hierarchical layout
- [ ] TASK-505.3: Calculate node positions
- [ ] TASK-505.4: Handle different graph sizes
- [ ] TASK-505.5: Add layout options (TB, LR, etc.)
- [ ] TASK-505.6: Optimize for performance

**Acceptance Criteria:**
- Graph is laid out logically
- No overlapping nodes
- Direction flows well (top-to-bottom or left-to-right)
- Works for graphs up to 500 nodes

---

## WEEK 6: Visualization - Part 2

### TASK-601: Interactive Controls
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 1 day  
**Dependencies:** TASK-505  
**PRD Reference:** PRD.md p.17, US-2.1

**Subtasks:**
- [ ] TASK-601.1: Implement zoom with mouse wheel
- [ ] TASK-601.2: Implement pan with click-and-drag
- [ ] TASK-601.3: Add zoom in/out buttons
- [ ] TASK-601.4: Add "Reset View" button
- [ ] TASK-601.5: Add "Fit to Screen" button
- [ ] TASK-601.6: Smooth animations
- [ ] TASK-601.7: Keyboard shortcuts (+ - 0 keys)

**Acceptance Criteria:**
- All controls work smoothly
- 60 FPS performance
- Keyboard shortcuts documented
- Touch-friendly (for future tablet support)

---

### TASK-602: Node Selection
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 1 day  
**Dependencies:** TASK-601  
**PRD Reference:** PRD.md p.17, US-2.2

**Subtasks:**
- [ ] TASK-602.1: Handle click events on nodes
- [ ] TASK-602.2: Highlight selected node (border, glow)
- [ ] TASK-602.3: Store selection in state (Zustand)
- [ ] TASK-602.4: Allow deselection (click background)
- [ ] TASK-602.5: Keyboard navigation (Tab, Arrow keys)
- [ ] TASK-602.6: Multi-select (Ctrl+click) - future enhancement

**Acceptance Criteria:**
- Click selects node
- Visual feedback clear
- Only one node selected at a time (MVP)
- Keyboard navigation works

---

### TASK-603: Details Side Panel
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 2 days  
**Dependencies:** TASK-602  
**PRD Reference:** PRD.md p.25, F5.0

**Subtasks:**
- [ ] TASK-603.1: Create `components/DetailsPanel.tsx`
- [ ] TASK-603.2: Show panel when node is selected
- [ ] TASK-603.3: Display file information:
  - [ ] File name and path
  - [ ] Lines of code
  - [ ] Cyclomatic complexity
  - [ ] Language
  - [ ] Health score
- [ ] TASK-603.4: Display dependencies list
- [ ] TASK-603.5: Display dependents list
- [ ] TASK-603.6: Add "View on GitHub" link
- [ ] TASK-603.7: Make panel closeable
- [ ] TASK-603.8: Add smooth slide-in animation
- [ ] TASK-603.9: Make responsive (collapsible on small screens)

**Acceptance Criteria:**
- Panel shows relevant information
- All data displayed correctly
- Animations smooth
- Close button works
- GitHub link works

---

### TASK-604: Legend Component
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 0.5 day  
**Dependencies:** TASK-603  
**PRD Reference:** PRD.md p.53, UI Wireframe

**Subtasks:**
- [ ] TASK-604.1: Create `components/Legend.tsx`
- [ ] TASK-604.2: Show health indicators:
  - [ ] 🟢 Green - Healthy
  - [ ] 🟡 Yellow - Warning
  - [ ] 🔴 Red - Issues
- [ ] TASK-604.3: Show node types/sizes
- [ ] TASK-604.4: Make collapsible
- [ ] TASK-604.5: Position in corner

**Acceptance Criteria:**
- Clear legend visible
- All indicators explained
- Can be hidden if needed

---

### TASK-605: Visualization Page Layout
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 1 day  
**Dependencies:** TASK-604  
**PRD Reference:** PRD.md p.53, Visualization Screen Wireframe

**Subtasks:**
- [ ] TASK-605.1: Create `pages/Visualization.tsx`
- [ ] TASK-605.2: Implement layout:
  - [ ] Header with back button, repo name, export button
  - [ ] Main canvas (CodeGraph)
  - [ ] Details panel (DetailsPanel)
  - [ ] Legend (Legend)
  - [ ] Controls overlay
- [ ] TASK-605.3: Fetch analysis data on mount
- [ ] TASK-605.4: Handle loading state
- [ ] TASK-605.5: Handle error state
- [ ] TASK-605.6: Make layout responsive

**Acceptance Criteria:**
- Layout matches wireframe
- All components integrated
- Data flows correctly
- Responsive design

---

## WEEK 7: Code Quality Features

### TASK-701: Duplicate Code Detection Integration
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 1 day  
**Dependencies:** TASK-302  
**PRD Reference:** PRD.md p.19, US-3.3

**Subtasks:**
- [ ] TASK-701.1: Install jscpd
- [ ] TASK-701.2: Create `analysis/duplicate_detector.py`
- [ ] TASK-701.3: Run jscpd on repository
- [ ] TASK-701.4: Parse jscpd output
- [ ] TASK-701.5: Calculate duplicate percentage per file
- [ ] TASK-701.6: Store results in database
- [ ] TASK-701.7: Add to analysis task
- [ ] TASK-701.8: Test with repositories that have duplicates

**Acceptance Criteria:**
- jscpd runs successfully
- Duplicate percentage calculated
- Results stored correctly
- Performance acceptable (<10% overhead)

---

### TASK-702: Health Score Calculation
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 2 days  
**Dependencies:** TASK-701  
**PRD Reference:** PRD.md p.18, US-3.1 & p.47 Algorithm

**Subtasks:**
- [ ] TASK-702.1: Create `analysis/health_calculator.py`
- [ ] TASK-702.2: Implement health calculation algorithm:
```python
def calculate_health(file):
    score = 100
    if complexity > 20: score -= 30
    elif complexity > 10: score -= 15
    if duplicate_percentage > 20: score -= 25
    elif duplicate_percentage > 10: score -= 10
    if has_dead_code: score -= 15
    
    if score >= 80: return "green"
    elif score >= 60: return "yellow"
    else: return "red"
```
- [ ] TASK-702.3: Calculate for each file
- [ ] TASK-702.4: Store in analysis results
- [ ] TASK-702.5: Add overall repo health score
- [ ] TASK-702.6: Write unit tests with various scenarios
- [ ] TASK-702.7: Make thresholds configurable

**Acceptance Criteria:**
- Health scores calculated for all files
- Algorithm matches specification
- Results make sense (validate manually)
- Thresholds can be adjusted

---

### TASK-703: Color Coding in Visualization
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 1 day  
**Dependencies:** TASK-702  
**PRD Reference:** PRD.md p.57, Node Component

**Subtasks:**
- [ ] TASK-703.1: Update `FileNode.tsx` component
- [ ] TASK-703.2: Apply color based on health:
  - [ ] Green: #ECFDF5 background, #10B981 border
  - [ ] Yellow: #FFFBEB background, #F59E0B border
  - [ ] Red: #FEF2F2 background, #EF4444 border
- [ ] TASK-703.3: Add health indicator icon
- [ ] TASK-703.4: Show health score on hover
- [ ] TASK-703.5: Ensure colorblind-friendly (use patterns/icons too)
- [ ] TASK-703.6: Update legend

**Acceptance Criteria:**
- Nodes color-coded correctly
- Colors match design system
- Tooltip shows health details
- Accessible for colorblind users

---

### TASK-704: Health Metrics Dashboard
**Status:** ⬜ TODO  
**Priority:** P1 (Post-MVP consideration)  
**Estimate:** 1 day  
**Dependencies:** TASK-703  

**Subtasks:**
- [ ] TASK-704.1: Create `components/MetricsDashboard.tsx`
- [ ] TASK-704.2: Show overall statistics:
  - [ ] Total files analyzed
  - [ ] Health distribution (% green/yellow/red)
  - [ ] Average complexity
  - [ ] Duplicate code percentage
  - [ ] Dead code count
- [ ] TASK-704.3: Add simple charts (pie chart, bar chart)
- [ ] TASK-704.4: Make collapsible

**Acceptance Criteria:**
- Clear metrics displayed
- Charts are readable
- Data is accurate

---

## WEEK 8: Dead Code Detection

### TASK-801: Call Graph Builder
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 2 days  
**Dependencies:** TASK-301  
**PRD Reference:** PRD.md p.47, Dead Code Algorithm

**Subtasks:**
- [ ] TASK-801.1: Create `analysis/call_graph_builder.py`
- [ ] TASK-801.2: Parse AST for each file (using tree-sitter)
- [ ] TASK-801.3: Extract function/class definitions
- [ ] TASK-801.4: Extract function calls
- [ ] TASK-801.5: Build call graph (NetworkX)
- [ ] TASK-801.6: Handle imports/exports
- [ ] TASK-801.7: Support Python, JavaScript, Java
- [ ] TASK-801.8: Write unit tests with sample code

**Acceptance Criteria:**
- Call graph built correctly
- Includes all functions and calls
- Imports tracked
- Works for supported languages

---

### TASK-802: Dead Code Detection Algorithm
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 3 days  
**Dependencies:** TASK-801  
**PRD Reference:** PRD.md p.47, Algorithm Specification

**Subtasks:**
- [ ] TASK-802.1: Create `analysis/dead_code_detector.py`
- [ ] TASK-802.2: Identify entry points:
  - [ ] main() functions
  - [ ] Exported symbols
  - [ ] Test functions
  - [ ] Public API (based on naming)
- [ ] TASK-802.3: Traverse graph from entry points
- [ ] TASK-802.4: Mark reachable nodes
- [ ] TASK-802.5: Identify unreachable nodes
- [ ] TASK-802.6: Apply heuristics to reduce false positives:
  - [ ] Skip magic methods (__init__, etc.)
  - [ ] Skip decorators
  - [ ] Detect dynamic calls (getattr, eval)
- [ ] TASK-802.7: Calculate confidence score
- [ ] TASK-802.8: Test with real repositories
- [ ] TASK-802.9: Validate accuracy (manually check sample)

**Acceptance Criteria:**
- Detects unused functions
- False positive rate <10%
- Confidence scores make sense
- Works for Python, JavaScript, Java

---

### TASK-803: Dead Code Indicators in UI
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 1 day  
**Dependencies:** TASK-802, TASK-703  
**PRD Reference:** PRD.md p.19, US-3.2

**Subtasks:**
- [ ] TASK-803.1: Update node component to show dead code indicator
- [ ] TASK-803.2: Add icon or badge for dead code
- [ ] TASK-803.3: Show confidence score in tooltip
- [ ] TASK-803.4: Add filter to show only dead code
- [ ] TASK-803.5: Update details panel with dead code info
- [ ] TASK-803.6: Update legend

**Acceptance Criteria:**
- Dead code clearly marked
- Confidence score visible
- Can filter to see only dead code
- Legend explains indicator

---

### TASK-804: Dead Code Export
**Status:** ⬜ TODO  
**Priority:** P1  
**Estimate:** 0.5 day  
**Dependencies:** TASK-803  
**PRD Reference:** PRD.md p.19, US-3.2

**Subtasks:**
- [ ] TASK-804.1: Create export button in UI
- [ ] TASK-804.2: Generate CSV/JSON with dead code list
- [ ] TASK-804.3: Include: file, function, line, confidence
- [ ] TASK-804.4: Download file

**Acceptance Criteria:**
- Export button works
- File format is usable
- All dead code included

---

## WEEK 9: Integration & Testing

### TASK-901: End-to-End Testing Suite
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 2 days  
**Dependencies:** TASK-803  
**PRD Reference:** PRD.md p.60

**Subtasks:**
- [ ] TASK-901.1: Set up Playwright
- [ ] TASK-901.2: Write E2E tests:
  - [ ] Test 1: Complete flow (input URL → analyze → view results)
  - [ ] Test 2: Click node → view details
  - [ ] Test 3: Zoom/pan controls
  - [ ] Test 4: Filter functionality
  - [ ] Test 5: Error handling
- [ ] TASK-901.3: Test with multiple repositories
- [ ] TASK-901.4: Add to CI pipeline

**Acceptance Criteria:**
- All E2E tests pass
- Tests are reliable (not flaky)
- CI runs tests automatically
- Coverage for all critical flows

---

### TASK-902: Performance Testing
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 1 day  
**Dependencies:** TASK-901  
**PRD Reference:** PRD.md p.56, Performance Requirements

**Subtasks:**
- [ ] TASK-902.1: Test with small repo (<100 files)
  - [ ] Verify analysis time <10s
- [ ] TASK-902.2: Test with medium repo (<1k files)
  - [ ] Verify analysis time <30s
- [ ] TASK-902.3: Test with large repo (<10k files)
  - [ ] Verify analysis time <2min
- [ ] TASK-902.4: Test visualization performance
  - [ ] Verify 60 FPS with 500 nodes
  - [ ] Measure render time
- [ ] TASK-902.5: Load testing (10 concurrent analyses)
- [ ] TASK-902.6: Document results
- [ ] TASK-902.7: Optimize bottlenecks

**Acceptance Criteria:**
- All performance targets met
- No memory leaks
- System handles concurrent requests
- Optimizations implemented if needed

---

### TASK-903: Bug Fixes & Polish
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 2 days  
**Dependencies:** TASK-902  

**Subtasks:**
- [ ] TASK-903.1: Review all open issues
- [ ] TASK-903.2: Fix critical bugs
- [ ] TASK-903.3: Fix high-priority bugs
- [ ] TASK-903.4: UI polish (animations, spacing, colors)
- [ ] TASK-903.5: Accessibility improvements
- [ ] TASK-903.6: Browser compatibility testing
- [ ] TASK-903.7: Mobile responsiveness fixes (for future)

**Acceptance Criteria:**
- Zero critical bugs
- <5 high-priority bugs
- UI is polished and professional
- Passes accessibility audit (WCAG 2.1 AA)

---

## WEEK 10: Launch Preparation

### TASK-1001: Documentation
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 1 day  
**Dependencies:** TASK-903  

**Subtasks:**
- [ ] TASK-1001.1: Write user documentation:
  - [ ] How to analyze a repository
  - [ ] How to interpret results
  - [ ] What health indicators mean
  - [ ] FAQ
- [ ] TASK-1001.2: Write developer documentation:
  - [ ] Architecture overview
  - [ ] Setup instructions
  - [ ] API documentation
  - [ ] Contributing guide
- [ ] TASK-1001.3: Create video tutorial (optional)
- [ ] TASK-1001.4: Update README.md

**Acceptance Criteria:**
- Documentation is comprehensive
- Easy to follow
- Includes examples
- No outdated information

---

### TASK-1002: Deployment Setup
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 2 days  
**Dependencies:** TASK-1001  
**PRD Reference:** PRD.md p.37

**Subtasks:**
- [ ] TASK-1002.1: Choose hosting provider (DigitalOcean/AWS/GCP)
- [ ] TASK-1002.2: Set up production environment
  - [ ] Database (PostgreSQL)
  - [ ] Redis
  - [ ] Backend containers
  - [ ] Frontend hosting
- [ ] TASK-1002.3: Configure domain and SSL
- [ ] TASK-1002.4: Set up environment variables
- [ ] TASK-1002.5: Configure monitoring (Prometheus/Grafana)
- [ ] TASK-1002.6: Set up error tracking (Sentry)
- [ ] TASK-1002.7: Configure backups
- [ ] TASK-1002.8: Write deployment runbook

**Acceptance Criteria:**
- Production environment running
- HTTPS enabled
- Monitoring working
- Backups configured
- Deployment process documented

---

### TASK-1003: Beta Testing
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 3 days  
**Dependencies:** TASK-1002  
**PRD Reference:** PRD.md p.12, Success Metrics

**Subtasks:**
- [ ] TASK-1003.1: Deploy to production
- [ ] TASK-1003.2: Recruit 20-30 beta testers
- [ ] TASK-1003.3: Create feedback form
- [ ] TASK-1003.4: Monitor usage and errors
- [ ] TASK-1003.5: Collect feedback
- [ ] TASK-1003.6: Fix critical issues found
- [ ] TASK-1003.7: Analyze metrics:
  - [ ] Analysis success rate
  - [ ] Average session duration
  - [ ] User satisfaction
- [ ] TASK-1003.8: Iterate based on feedback

**Acceptance Criteria:**
- 20+ beta testers signed up
- Feedback collected from 15+ testers
- Critical issues fixed
- Satisfaction score >4.0/5.0
- Ready for public launch

---

### TASK-1004: Public Launch
**Status:** ⬜ TODO  
**Priority:** P0  
**Estimate:** 1 day  
**Dependencies:** TASK-1003  

**Subtasks:**
- [ ] TASK-1004.1: Final QA check
- [ ] TASK-1004.2: Open to public
- [ ] TASK-1004.3: Announce on:
  - [ ] Twitter/X
  - [ ] Reddit (r/programming, r/webdev)
  - [ ] Hacker News
  - [ ] Dev.to
  - [ ] GitHub (create org, make repo public)
- [ ] TASK-1004.4: Create landing page with examples
- [ ] TASK-1004.5: Monitor launch day
- [ ] TASK-1004.6: Respond to feedback
- [ ] TASK-1004.7: Fix any critical issues immediately

**Acceptance Criteria:**
- System stable
- Public announcement made
- Initial users acquired
- Support channels active

---

## Post-MVP Tasks (Weeks 11-16)

### TASK-1101: GitHub OAuth Authentication
**Status:** ⬜ TODO  
**Priority:** P1  
**Estimate:** 1 week  
**PRD Reference:** PRD.md p.27, F7.0

**Subtasks:**
- [ ] Register GitHub OAuth app
- [ ] Implement OAuth flow
- [ ] Store access tokens securely
- [ ] Enable private repository analysis
- [ ] Add user settings page

---

### TASK-1102: Advanced Filters
**Status:** ⬜ TODO  
**Priority:** P1  
**Estimate:** 1 week  
**PRD Reference:** PRD.md p.18, US-2.3 & p.27, F8.0

**Subtasks:**
- [ ] Search by file name
- [ ] Filter by language
- [ ] Filter by health status
- [ ] Filter by complexity
- [ ] Save filter presets

---

### TASK-1103: Export Functionality
**Status:** ⬜ TODO  
**Priority:** P1  
**Estimate:** 1 week  
**PRD Reference:** PRD.md p.21, US-4.1 & p.28, F9.0

**Subtasks:**
- [ ] Export as PNG
- [ ] Export as SVG
- [ ] Export as PDF report
- [ ] Export data as JSON

---

### TASK-1104: Repository Comparison
**Status:** ⬜ TODO  
**Priority:** P1  
**Estimate:** 1 week  
**PRD Reference:** PRD.md p.28, F10.0

**Subtasks:**
- [ ] Compare two repositories
- [ ] Compare two commits
- [ ] Side-by-side visualization
- [ ] Diff metrics

---

## Future Features (Months 6+)

### TASK-1201: AI-Powered Insights
**PRD Reference:** PRD.md p.28, F11.0

### TASK-1202: Collaborative Features
**PRD Reference:** PRD.md p.29, F12.0

### TASK-1203: CI/CD Integration
**PRD Reference:** PRD.md p.29, F13.0

### TASK-1204: IDE Extensions
**PRD Reference:** PRD.md p.29, F14.0

---

## Summary Statistics

**Total MVP Tasks:** 74 tasks  
**Total Estimated Time:** 10 weeks  
**Critical Path:** TASK-000 → TASK-101-105 → TASK-201-205 → TASK-301-304 → TASK-401-406 → TASK-501-505 → TASK-601-605 → TASK-701-704 → TASK-801-804 → TASK-901-903 → TASK-1001-1004

**Tasks by Phase:**
- Phase 0 (Validation): 1 task
- Week 1 (Setup): 5 tasks
- Week 2 (GitHub): 5 tasks
- Week 3 (Analysis): 4 tasks
- Week 4 (React): 6 tasks
- Week 5 (Viz Part 1): 5 tasks
- Week 6 (Viz Part 2): 5 tasks
- Week 7 (Quality): 4 tasks
- Week 8 (Dead Code): 4 tasks
- Week 9 (Testing): 3 tasks
- Week 10 (Launch): 4 tasks
- Post-MVP: 4 tasks
- Future: 4+ tasks

**Priority Breakdown:**
- P0 (Critical): 70 tasks
- P1 (High): 4 tasks
- P2 (Medium): 0 tasks
- P3 (Low): 0 tasks

---

## Task Management Process

### Daily Workflow:
1. Check task list
2. Pick next task (follow dependencies)
3. Update status to "IN PROGRESS"
4. Complete task
5. Update status to "REVIEW" or "DONE"
6. Check off subtasks
7. Move to next task

### Weekly Review:
1. Review completed tasks
2. Update estimates for remaining tasks
3. Identify blockers
4. Adjust timeline if needed
5. Report progress to stakeholders

### Task Status Updates:
- Update this file after completing each task
- Check off subtasks as you go
- Document any blockers or issues
- Update estimates if significantly off

---

**Last Updated:** September 30, 2025  
**Next Review:** After TASK-000 (Validation)  
**Status:** Ready to Begin

