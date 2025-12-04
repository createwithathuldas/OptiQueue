from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os

# Create FastAPI app
app = FastAPI(title="OptiQueue - Smart OPD Queue Management")

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Serve the registration page
@app.get("/auth/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("auth/register.html", {"request": request})

# Serve the login page
@app.get("/auth/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})

# Serve the patient dashboard
@app.get("/patient/dashboard", response_class=HTMLResponse)
async def patient_dashboard(request: Request):
    return templates.TemplateResponse("patient/dashboard.html", {"request": request})

# Serve the staff dashboard
@app.get("/staff/dashboard", response_class=HTMLResponse)
async def staff_dashboard(request: Request):
    return templates.TemplateResponse("staff/dashboard.html", {"request": request})

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to OptiQueue - Smart OPD Queue Management System"}