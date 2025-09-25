import os
from dotenv import load_dotenv

load_dotenv()

print("=== Environment Variables Check ===")
print(f"HOST: '{os.getenv('HOST')}'")
print(f"PK exists: {os.getenv('PK') is not None}")
print(f"PK length: {len(os.getenv('PK')) if os.getenv('PK') else 'N/A'}")
print(f"PBK exists: {os.getenv('PBK') is not None}")

# Check if .env file exists
env_path = os.path.join(os.getcwd(), '..', '.env')
print(f".env file exists: {os.path.exists(env_path)}")
print(f"Current working directory: {os.getcwd()}")
print(f"Looking for .env at: {env_path}")

# List files in parent directory
parent_dir = os.path.join(os.getcwd(), '..')
files = os.listdir(parent_dir)
print(f"Files in parent directory: {[f for f in files if f.startswith('.env')]}")