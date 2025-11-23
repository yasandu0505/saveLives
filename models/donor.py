from pydantic import BaseModel, EmailStr, Field

class Donor(BaseModel):
    email: EmailStr
    name: str = Field(..., alias="Name", description="Full name of the donor")
    user_name: str = Field(..., alias="userName", description="Username of the donor")
    phone_number: str = Field(..., alias="phoneNumber", description="Phone number of the donor")
    nic: str = Field(..., description="National Identity Card number")
    password: str = Field(..., min_length=8, description="Password for the donor account")


    class Config:
        populate_by_name = True  # Allows both alias and field name
        json_schema_extra = {
            "example": {
                "email": "donor@example.com",
                "Name": "John Doe",
                "userName": "johndoe",
                "phoneNumber": "+1234567890",
                "nic": "123456789V",
                "password": "SecurePass123!"
            }
        }

