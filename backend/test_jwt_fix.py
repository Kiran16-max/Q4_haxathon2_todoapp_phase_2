"""
Test script to verify JWT authentication fix
"""
import os
import sys
from datetime import datetime, timedelta
from jose import jwt

# Add the backend src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.utils.jwt_handler import create_access_token, verify_token

def test_jwt_functionality():
    print("Testing JWT functionality with BETTER_AUTH_SECRET...")
    
    # Load environment variables
    env_vars = {}
    try:
        with open('.env', 'r') as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    env_vars[key] = value
                    os.environ[key] = value
    except FileNotFoundError:
        print("Warning: .env file not found")
        
    print(f"BETTER_AUTH_SECRET loaded: {'BETTER_AUTH_SECRET' in env_vars}")
    
    # Test creating and verifying a token
    test_data = {"sub": "test@example.com"}
    
    try:
        # Create a token
        token = create_access_token(test_data)
        print(f"✓ Created JWT token: {token[:30]}...")
        
        # Verify the token
        email = verify_token(token)
        print(f"✓ Verified JWT token, extracted email: {email}")
        
        if email == "test@example.com":
            print("✓ JWT functionality is working correctly!")
            return True
        else:
            print("✗ JWT verification returned incorrect email")
            return False
            
    except Exception as e:
        print(f"✗ JWT functionality test failed: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_jwt_functionality()
    if success:
        print("\n🎉 JWT authentication fix verified successfully!")
    else:
        print("\n❌ JWT authentication fix verification failed!")
        sys.exit(1)