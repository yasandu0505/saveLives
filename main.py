from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Donor, DonorLogin
from services import AuthenticationService


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
        # TODO: Implement login logic in authentication_service
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

