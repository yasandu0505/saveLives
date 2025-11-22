from models import Donor
from utils import create_donor_node
class AuthenticationService:
    def __init__(self):
        pass

    def signup_user(self, donor: Donor, user_type: str):
        """Signup a donor user"""
        node = create_donor_node(donor.name, donor.email, donor.phone_number, donor.nic, donor.user_name, user_type, donor.password)
        return node

       