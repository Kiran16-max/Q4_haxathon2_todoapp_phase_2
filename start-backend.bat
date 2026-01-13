@echo off
echo Starting FastAPI backend server...
cd /d "C:\Users\PC\Desktop\Q4_haxathon2_todoapp_phase_2\backend"

:: Load environment variables from .env file
for /f "tokens=1,* delims==" %%a in ('type .env 2^>nul') do (
  set "%%a=%%b"
)

python -m uvicorn main:app --reload --port 8000