import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Query API Configuration
QUERY_API = os.getenv("QUERY_API")
UPDATE_API = os.getenv("UPDATE_API")

# Validate required environment variables
if not QUERY_API and not UPDATE_API:
    raise ValueError("QUERY_API and UPDATE_API environment variables are not set in .env file")

