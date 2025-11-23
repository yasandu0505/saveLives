from datetime import datetime, timedelta
from jose import jwt
from typing import Optional, Dict, Any
from .config import JWT_SECRET_KEY, JWT_ALGORITHM, JWT_EXPIRATION_DAYS


def generate_token(user_data: Dict[str, Any]) -> str:
    """
    Generate a JWT token for a user.
    
    Args:
        user_data: Dictionary containing user information (user_name, user_type, etc.)
        
    Returns:
        str: Encoded JWT token
        
    Example:
        token = generate_token({"user_name": "yasandu2005", "user_type": "donor"})
    """
    # Calculate expiration time (1 day from now)
    expire = datetime.utcnow() + timedelta(days=JWT_EXPIRATION_DAYS)
    
    # Create token payload
    payload = {
        "user_name": user_data.get("user_name"),
        "user_type": user_data.get("user_type", "donor"),
        "exp": expire,  # Expiration time
        "iat": datetime.utcnow()  # Issued at time
    }
    
    # Encode and return the token
    encoded_jwt = jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt


def verify_token(token: str) -> Optional[Dict[str, Any]]:
    """
    Verify and decode a JWT token.
    
    Args:
        token: JWT token string to verify
        
    Returns:
        Optional[Dict]: Decoded token payload if valid, None if invalid/expired
        
    Example:
        payload = verify_token(token)
        if payload:
            user_name = payload["user_name"]
    """
    try:
        # Decode and verify the token
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        # Token has expired
        return None
    except jwt.JWTError:
        # Invalid token
        return None

