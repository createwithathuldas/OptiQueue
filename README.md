# OptiQueue - Smart OPD Queue Management System

## Phase 1: The Gatekeeper (Authentication & Role-Based Access)

This is the first phase of the OptiQueue system, focusing on authentication and role-based access control.

### Features Implemented

1. **User Roles**: 
   - Patient
   - Doctor
   - Lab Technician
   - Pharmacy

2. **Registration with Secret Code Logic**:
   - Users can register as patients without any code
   - Staff members must use the access code "MEDIC_2025" to register with staff roles

3. **Login with Role-Based Redirection**:
   - Patients are redirected to `/patient/dashboard`
   - Staff members are redirected to `/staff/dashboard`

4. **Security**:
   - Frontend: Auth guard to protect pages
   - Backend: Token verification for API routes

### Tech Stack

- **Backend**: Python (FastAPI)
- **Database/Auth**: Firebase (Firestore & Authentication)
- **Frontend**: Vanilla HTML/CSS/JavaScript

### Setup Instructions

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Configure Firebase:
   - Create a Firebase project at https://console.firebase.google.com/
   - Download the service account key JSON file
   - Rename it to `firebase_credentials.json` and place it in the project root
   - Update the `.env` file with your Firebase web app configuration

3. Run the application:
   ```
   uvicorn main:app --reload
   ```

### File Structure

```
OptiQueue/
├── main.py (FastAPI entry point, serving static files and 2 placeholder routes)
├── .env (Template for Firebase keys)
├── app/
│   ├── database.py (Firebase Admin initialization)
│   └── auth.py (Token verification logic)
├── static/
│   ├── js/
│   │   ├── firebase_config.js (Client-side config)
│   │   └── auth_guard.js (Security check)
│   └── css/
│       └── style.css (Basic clean medical styling)
└── templates/
    ├── auth/
    │   ├── login.html
    │   └── register.html
    ├── patient/
    │   └── dashboard.html (Placeholder text only)
    └── staff/
        └── dashboard.html (Placeholder text only)
```