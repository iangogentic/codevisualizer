# CodeMapper - Complete Setup & Test Guide
## Everything You Need to Run CodeMapper

**Date:** September 30, 2025

---

## ✅ **What's Been Built (23% Complete):**

- ✅ Backend API (FastAPI)
- ✅ Frontend UI (React + React Flow)
- ✅ Analysis Engine (Emerge integrated)
- ✅ Database (SQLite - no Docker needed!)
- ✅ GitHub Integration
- ✅ 17/74 tasks complete
- ✅ All code on GitHub: https://github.com/iangogentic/codevisualizer

---

## 🚀 **Quick Start (2 Commands):**

### **Step 1: Start Backend**

Open PowerShell Window #1:
```powershell
cd C:\Users\ianig\Desktop\CodeVisualizer\backend
.\venv\Scripts\activate
$env:PYTHONPATH = "C:\Users\ianig\Desktop\CodeVisualizer\backend"
py -m uvicorn api.main:app --reload
```

**✅ Success when you see:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

### **Step 2: Start Frontend**

Open PowerShell Window #2:
```powershell
cd C:\Users\ianig\Desktop\CodeVisualizer\frontend
npm start
```

**✅ Success when you see:**
```
webpack compiled successfully
```
Browser opens automatically at `http://localhost:3000`

---

## 🧪 **Test It Works:**

1. Visit `http://localhost:3000`
2. You should see: **🎨 CodeMapper** home page
3. Paste this URL: `https://github.com/pallets/flask`
4. Click: **🔍 Analyze Repository**
5. Wait 2-5 seconds
6. See the code visualization!

---

## ❌ **If Backend Won't Start:**

### Error: "No module named 'api'"
**Fix:**
```powershell
cd C:\Users\ianig\Desktop\CodeVisualizer\backend
$env:PYTHONPATH = "$PWD"
py -m uvicorn api.main:app --reload
```

### Error: "No module named 'uvicorn'"
**Fix:**
```powershell
cd C:\Users\ianig\Desktop\CodeVisualizer\backend
.\venv\Scripts\activate
pip install -r requirements.txt
```

### Error: "Database error"
**Fix:** Delete and recreate:
```powershell
cd C:\Users\ianig\Desktop\CodeVisualizer\backend
Remove-Item codemapper.db -ErrorAction SilentlyContinue
py -m uvicorn api.main:app --reload
```

---

## ❌ **If Frontend Won't Start:**

### Error: "Module not found"
**Fix:**
```powershell
cd C:\Users\ianig\Desktop\CodeVisualizer\frontend
Remove-Item -Recurse node_modules -Force
npm install
npm start
```

### Error: "Port 3000 in use"
**Fix:**
```powershell
Get-Process -Name node | Stop-Process -Force
npm start
```

---

## 🔍 **Verify Both Servers:**

### Test Backend:
```powershell
Invoke-RestMethod http://localhost:8000/api/health
```
Should return: `{"status":"healthy"}`

### Test Frontend:
Visit: `http://localhost:3000`  
Should show: CodeMapper home page

---

## 📊 **API Documentation:**

While backend is running, visit:
```
http://localhost:8000/docs
```

You'll see auto-generated API docs with:
- POST /api/analyze
- GET /api/analysis/{id}
- Interactive testing

---

## 🎯 **What CodeMapper Does:**

1. **Accepts GitHub URL** (any public repo)
2. **Clones repository** (temporary)
3. **Analyzes code** with Emerge:
   - Lines of code
   - Number of methods
   - File structure
   - Dependencies
4. **Calculates health scores:**
   - 🟢 Green = Healthy
   - 🟡 Yellow = Warning
   - 🔴 Red = Issues
5. **Visualizes** in interactive graph:
   - Zoom/pan/drag
   - Click for details
   - Color-coded

---

## 💡 **Current Status:**

**Working Features:**
- ✅ GitHub URL validation
- ✅ Repository cloning
- ✅ Code analysis (Emerge)
- ✅ Health calculation
- ✅ Interactive visualization
- ✅ Multi-language support (Python, JS, Java, C++, etc.)

**Not Yet Implemented:**
- ⏳ Duplicate code detection (Week 7)
- ⏳ Dead code detection (Week 8)
- ⏳ Advanced filters (Week 5-6)
- ⏳ Export features (Post-MVP)

---

## 📁 **Project Structure:**

```
CodeVisualizer/
├── backend/              ✅ FastAPI server
│   ├── api/main.py      ✅ Main app
│   ├── database/        ✅ SQLAlchemy models
│   ├── github/          ✅ URL validation, cloning
│   ├── analysis/        ✅ Emerge wrapper
│   └── tests/           ✅ 14 passing tests
├── frontend/            ✅ React app
│   └── src/
│       ├── pages/       ✅ Home, Visualization
│       ├── api/         ✅ API client
│       └── utils/       ✅ Data parsers
├── emerge/              ✅ Code analyzer
├── PRD.md              ✅ Product spec (2,138 lines)
├── TASKS.md            ✅ Task tracking
└── START_HERE.md       ✅ Quick start guide
```

---

## 🎊 **You're Ready!**

**Just run the 2 commands above and visit localhost:3000!**

**Having issues?** Check the error messages in the PowerShell windows and refer to the troubleshooting section above.

**Everything working?** Try analyzing different repositories!

---

**GitHub:** https://github.com/iangogentic/codevisualizer  
**Status:** ✅ 23% Complete, Fully Functional Beta!  
**Next:** Continue building more features or start using it!

🚀 **Happy code visualizing!** 🎨

