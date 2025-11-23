from .config import UPDATE_API
from datetime import datetime
import requests

def create_donor_node(name: str, email: str, phone_number: str, nic: str, user_name: str, user_type: str, hashed_password: str):
    url = f"{UPDATE_API}/entities/"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
            "id": user_name,
            "kind": {
                "major": "User",
                "minor": user_type
                },
            "created": datetime.now().isoformat(),
            "terminated": "",
            "name": {
                "startTime": datetime.now().isoformat(),
                "endTime": "",
                "value": name
            },
            "metadata": [],
            "attributes": [
                {
                "key": "Donor Data",
                "value": {
                    "values": [
                        {
                            "startTime": datetime.now().isoformat(),
                            "endTime": "",
                            "value": {
                                "columns": ["user_name", "email", "phone_number", "nic", "password"],
                                    "rows": [
                                        [user_name, email, phone_number, nic, hashed_password],
                                    ]
                            }
                        }
                    ]
                }
            }
            ],
            "relationships": []
        }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  
        output = response.json()
        return output
    except Exception as e:
        print("error : " +  str(e))
        raise Exception(f"Failed to create node: {e}")
