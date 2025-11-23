from models import Donor
from utils import create_donor_node, validate_donor, get_donor_data
import bcrypt

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
        print(donor_data)
    
        return user
        