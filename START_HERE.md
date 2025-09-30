# ⚡ START CODEMAPPER - Simple Instructions

## 🚀 Open 2 PowerShell Windows

### Window 1: Backend
```powershell
cd C:\Users\ianig\Desktop\CodeVisualizer\backend
.\venv\Scripts\activate
$env:PYTHONPATH = "C:\Users\ianig\Desktop\CodeVisualizer\backend"
$env:DATABASE_URL = "sqlite:///./codemapper.db"
python -m uvicorn api.main:app --reload
```

**Wait for:** ✅ `Uvicorn running on http://127.0.0.1:8000`

---

### Window 2: Frontend  
```powershell
cd C:\Users\ianig\Desktop\CodeVisualizer\frontend
npm start
```

**Wait for:** ✅ `webpack compiled successfully`  
**Browser opens:** ✅ `http://localhost:3000`

---

## ✅ You're Ready!

Visit: **http://localhost:3000**

You should see the beautiful CodeMapper home page with:
- 🎨 Gradient purple header  
- GitHub URL input field
- "Analyze Repository" button

---

## 🧪 Test It:

1. Paste: `https://github.com/pallets/flask`
2. Click "🔍 Analyze Repository"
3. Watch the magic! ✨

---

**That's it! Both servers running, app working!** 🎉

