from models import Donor
from utils import create_donor_node
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

       