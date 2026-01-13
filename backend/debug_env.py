import os
from dotenv import load_dotenv
from pathlib import Path

print("Current working directory:", os.getcwd())
print("__file__ location:", __file__)

# Load environment variables from the backend directory
env_path = Path(__file__).parent / ".env"
print("Looking for .env file at:", env_path)
print(".env file exists:", env_path.exists())

if env_path.exists():
    load_dotenv(dotenv_path=env_path)
    print("Loaded environment variables from .env file")

# Also try loading without specifying path (this will look in current directory)
load_dotenv()
print("Also loaded from current directory")

# Check if DATABASE_URL is available
database_url = os.getenv("DATABASE_URL")
print("DATABASE_URL from environment:", database_url)
print("All environment variables containing 'DATABASE':")
for key, value in os.environ.items():
    if 'DATABASE' in key.upper():
        print(f"  {key}: {value}")