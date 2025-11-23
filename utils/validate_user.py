from .config import QUERY_API
from typing import Optional, Tuple
import requests

def validate_donor(user_name: str) -> Tuple[bool, Optional[dict]]:
    """
    Validate donor user by username.
    Returns: (is_valid: bool, user: Optional[dict])
    - If valid: (True, user_dict)
    - If not valid: (False, None)
    """
    url = f"{QUERY_API}/v1/entities/search"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "id": user_name
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  
        output = response.json()
        
        # Extract the body array and get the first object
        body = output.get("body", [])
        
        # Check if body has any items
        if not body:
            return (False, None)
        
        # Get the first object from body array
        user = body[0]
        
        # Verify the user id matches the username
        if user.get("id") != user_name:
            return (False, None)
        
        return (True, user)
    
    except Exception as e:
        print("error : " +  str(e))
        return (False, None)
    