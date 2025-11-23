from pydantic import BaseModel, Field

class DonorLogin(BaseModel):
    user_name: str = Field(..., alias="userName", description="Username of the donor")
    password: str = Field(..., description="Password for the donor account")

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "userName": "johndoe",
                "password": "SecurePass123!"
            }
        }

