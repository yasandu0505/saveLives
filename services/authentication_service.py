from models import Donor
from utils import create_donor_node, validate_donor, get_donor_data, decode_protobuf_string
import bcrypt
import json

class AuthenticationService:
    def __init__(self):
        pass

    def signup_user(self, donor: Donor, user_type: str):
        """Signup a donor user"""
        hashed_password = bcrypt.hashpw(donor.password.encode('utf-8'), bcrypt.gensalt())
        hashed_password_str = hashed_password.decode("utf-8")
        node = create_donor_node(donor.name, donor.email, donor.phone_number, donor.nic, donor.user_name, user_type, hashed_password_str)
        return node

    def login_donor(self, user_name: str, password: str):
        """Login a donor user - validates username and password"""
        # Validate user exists and get user data (username matching is done in validate_donor)
        is_valid, user = validate_donor(user_name)
        
        if not is_valid or not user:
            raise Exception(f"Invalid username")
        
        donor_data_output = get_donor_data(user_name)
        donor_data = donor_data_output["value"]
        
        if not donor_data:
            raise Exception(f"Failed to retrieve donor data")
                
        # Decode the protobuf string
        decoded_string = decode_protobuf_string(donor_data)
        
        if not decoded_string:
            raise Exception(f"Failed to decode donor data")
        
        # Parse the JSON string to get the data structure
        donor_data = json.loads(decoded_string)
        
        # Extract columns and rows
        columns = donor_data.get("columns", [])
        rows = donor_data.get("rows", [])
        
        if not rows or len(rows) == 0:
            raise Exception(f"No data found for donor")
        
        # Create a dictionary mapping column names to values from the first row        
        donor_dict = dict(zip(columns, rows[0]))
        
        # Check if password column exists
        if "password" not in donor_dict:
            raise Exception(f"Password column not found in donor data")
        
        # Get the hashed password directly from the dictionary
        # The password was stored as a string (from hashed_password.decode("utf-8"))
        # so we need to encode it back to bytes for bcrypt.checkpw()
        hashed_password_str = donor_dict["password"]
        hashed_password_bytes = hashed_password_str.encode('utf-8')
        
        # Verify the provided password matches the hashed password
        # bcrypt.checkpw() expects both password and hash as bytes
        if not bcrypt.checkpw(password.encode('utf-8'), hashed_password_bytes):
            raise Exception(f"Invalid password")
        
        # decode the user's actual name
        name = decode_protobuf_string(user["name"])
        
        return {
            "user_name": donor_dict["user_name"],
            "email": donor_dict["email"],
            "phone_number": donor_dict["phone_number"],
            "nic": donor_dict["nic"],
            "name": name
        }
        