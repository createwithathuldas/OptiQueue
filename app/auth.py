import firebase_admin
from firebase_admin import auth as firebase_auth
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# Security scheme for FastAPI
security = HTTPBearer()

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Dependency function to verify Firebase ID token.
    
    Args:
        credentials: HTTP Authorization credentials containing the ID token
        
    Returns:
        dict: Decoded token information
        
    Raises:
        HTTPException: If token is invalid or expired
    """
    try:
        # Verify the ID token
        decoded_token = firebase_auth.verify_id_token(credentials.credentials)
        return decoded_token
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid authentication credentials: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"},
        )

def get_user_role(uid: str) -> str:
    """
    Get user role from Firestore.
    
    Args:
        uid: Firebase user ID
        
    Returns:
        str: User role ('patient', 'doctor', 'lab', 'pharmacy')
    """
    try:
        # Import here to avoid circular imports
        from app.database import db
        
        user_ref = db.collection('users').document(uid)
        user_doc = user_ref.get()
        
        if user_doc.exists:
            user_data = user_doc.to_dict()
            return user_data.get('role', 'patient')
        else:
            return 'patient'  # Default role
    except Exception as e:
        print(f"Error getting user role: {e}")
        return 'patient'  # Default role