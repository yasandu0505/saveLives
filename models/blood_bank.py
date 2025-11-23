from pydantic import BaseModel, EmailStr, Field


class BloodBank(BaseModel):
    email: EmailStr
    name: str = Field(..., alias="Name", description="Name of the blood bank")
    user_name: str = Field(..., alias="userName", description="Username of the blood bank")
    phone_number: str = Field(..., alias="phoneNumber", description="Phone number of the blood bank")
    registration_number: str = Field(..., alias="registrationNumber", description="Registration number of the blood bank")
    address: str = Field(..., description="Address of the blood bank")

    class Config:
        populate_by_name = True  # Allows both alias and field name
        json_schema_extra = {
            "example": {
                "email": "bloodbank@example.com",
                "Name": "City Blood Bank",
                "userName": "citybloodbank",
                "phoneNumber": "+1234567890",
                "registrationNumber": "BB-2024-001",
                "address": "123 Main Street, City, Country"
            }
        }

