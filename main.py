from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from models import Donor, DonorLogin
from services import AuthenticationService
from utils import verify_token


app = FastAPI(
    title="SaveLives API",
    description="FastAPI application for SaveLives",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

authentication_service = AuthenticationService()
security = HTTPBearer()


@app.post("/signup/donor")
async def signup_donor(donor: Donor):
    """Signup endpoint for donors"""
    try:
        user = authentication_service.signup_user(donor, user_type="donor")
        return {
            "message": "Donor signed up successfully", 
            "status_code": 200,
            "data": {
                "user": user,
                "user_type": user["kind"]["minor"]
            }
        }
    except Exception as e:
        return {
            "message": "Failed to sign up donor",
            "status_code": 500,
            "data": {
                "error": str(e)
            }
        }
        
        
@app.post("/login/donor")
async def login_donor(login_data: DonorLogin):
    """Login endpoint for donors - requires only username and password"""
    try:
        result = authentication_service.login_donor(login_data.user_name, login_data.password)
        return {
            "message": "Donor logged in successfully",
            "status_code": 200,
            "data": result
        }
    except Exception as e:
        return {
            "message": "Failed to login donor",
            "status_code": 401,
            "data": {
                "error": str(e)
            }
        }


async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    FastAPI dependency to verify JWT token and get current user.
    Used to protect routes that require authentication.
    """
    token = credentials.credentials
    payload = verify_token(token)
    
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return payload


@app.get("/donor/profile")
async def get_donor_profile(current_user: dict = Depends(get_current_user)):
    """
    Protected route example - Get donor profile.
    Requires valid JWT token in Authorization header.
    """
    return {
        "message": "Profile retrieved successfully",
        "status_code": 200,
        "data": {
            "user_name": current_user.get("user_name"),
            "user_type": current_user.get("user_type"),
            "message": "This is a protected route. You are authenticated!"
        }
    }

