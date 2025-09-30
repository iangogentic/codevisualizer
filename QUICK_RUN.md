# Quick Run Guide
## Start CodeMapper in 30 Seconds

**Last Updated:** September 30, 2025

---

## 🚀 Method 1: Use Batch Scripts (Easiest)

### Start Backend:
```
Double-click: start-backend.bat
```
Or in PowerShell:
```powershell
.\start-backend.bat
```

**Wait for:** "Uvicorn running on http://0.0.0.0:8000"

### Start Frontend:
```
Double-click: start-app.bat
```
Or in PowerShell:
```powershell
.\start-app.bat
```

**Wait for:** "webpack compiled successfully"

### Visit:
```
http://localhost:3000
```

---

## 🚀 Method 2: Manual Commands

### Terminal 1 - Backend:
```powershell
cd CodeVisualizer\backend
.\venv\Scripts\activate
$env:PYTHONPATH = "C:\Users\ianig\Desktop\CodeVisualizer\backend"
python -m uvicorn api.main:app --reload
```

### Terminal 2 - Frontend:
```powershell
cd CodeVisualizer\frontend
npm start
```

---

## ✅ How to Know It's Working:

### Backend (Terminal 1):
```
✅ You should see:
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete
```

### Frontend (Terminal 2):
```
✅ You should see:
webpack compiled successfully
```

### Browser:
```
✅ You should see:
🎨 CodeMapper home page
   with gradient purple header
   and GitHub URL input
```

---

## 🧪 Test It:

1. Visit `http://localhost:3000`
2. Paste: `https://github.com/pallets/flask`
3. Click "🔍 Analyze Repository"
4. Watch it analyze and visualize!

---

## ❌ Troubleshooting:

### "Backend won't start"
```powershell
cd backend
pip install -r requirements.txt
```

### "Frontend won't start"
```powershell
cd frontend
npm install
npm start
```

### "Port 3000 already in use"
Kill the process:
```powershell
Get-Process -Name node | Stop-Process -Force
```

### "Port 8000 already in use"
Kill the process:
```powershell
Get-Process -Name python | Stop-Process -Force
```

---

**Now you have 2 new PowerShell windows that should be running!**

**Check if backend is working:** http://localhost:8000  
**Check if frontend is working:** http://localhost:3000

**Both should be running!** 🚀

