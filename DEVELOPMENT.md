# Development Guide
## CodeMapper Local Development Setup

**Last Updated:** September 30, 2025

---

## Quick Start

### Prerequisites
- Python 3.11+
- Node.js 20+
- Docker & Docker Compose
- Git

### Setup

**1. Clone Repository:**
```bash
git clone https://github.com/iangogentic/codevisualizer.git
cd codevisualizer
```

**2. Start Backend (Docker):**
```bash
docker-compose up -d
```

**3. Start Frontend:**
```bash
cd frontend
npm install
npm start
```

**4. Access:**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

---

## Project Structure

```
CodeVisualizer/
├── backend/                # Python FastAPI backend
│   ├── api/               # API routes and schemas
│   ├── analysis/          # Code analysis engine
│   ├── database/          # Database models
│   ├── github/            # GitHub integration
│   ├── migrations/        # Alembic migrations
│   └── tests/             # Backend tests
├── frontend/              # React TypeScript frontend
│   └── src/
│       ├── components/    # React components
│       ├── utils/         # Utilities (emergeParser.ts)
│       └── App.tsx        # Main app
├── emerge/                # Emerge code analyzer (forked)
├── .github/workflows/     # CI/CD pipelines
└── docs/                  # Documentation
```

---

## Development Workflow

See `WORKFLOW.md` and `.cursorrules` for complete workflow automation.

**Current Status:** Week 1 - Foundation Setup Complete

**Next:** Week 2 - GitHub Integration (TASK-201+)

