from models import Donor, BloodBank
from utils import create_node

class AuthenticationService:
    def __init__(self):
        pass

    def signup_user(self, donor: Donor, user_type: str):
        """Signup a donor user"""
        #create the donor node
        node = create_node(donor.name, donor.email, donor.phone_number, donor.nic, donor.user_name, user_type)
        
        return node

    def signup_bloodbank(self, bloodbank: BloodBank):
        """Signup a blood bank user"""
        #create the blood bank node
        # Note: BloodBank doesn't have NIC, so we'll use registration_number instead
        node = create_node(bloodbank.name, bloodbank.email, bloodbank.phone_number, bloodbank.registration_number)
        
        return bloodbank.name         