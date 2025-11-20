from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Donor, BloodBank
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


@app.post("/signup/bloodbank")
async def signup_bloodbank(bloodbank: BloodBank):
    """Signup endpoint for blood banks"""
    try:
        user = authentication_service.signup_bloodbank(bloodbank)
        return {
            "message": "Blood bank signed up successfully", 
            "status_code": 200,
            "data": {
                "user": user,
                "user_type": user["kind"]["minor"]
            }
        }
    except Exception as e:
        return {
            "message": "Failed to sign up blood bank",
            "status_code": 500,
            "data": {
                "error": str(e)
            }
        }
