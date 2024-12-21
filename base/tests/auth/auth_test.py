import requests

# The base URL of your API
BASE_URL = "http://127.0.0.1:8000/api/v1/"

# Signup test
def test_signup():
    url = BASE_URL + "signup/"
    data = {
        "username": "asd1",
        "email": "asd1@gmail.com",
        "password": "123",
        "role": "User"
    }
    
    # Send data as JSON, and set headers for JSON content
    response = requests.post(url, json=data)

    if response.status_code == 201:
        print("Signup test passed: User created successfully!")
    else:
        print(f"Signup test failed: {response.status_code}, {response.text}")

# Login test
def test_login():
    url = BASE_URL + "login/"
    data = {
        "username": "asd1",
        "password": "123"
    }
    
    # Send data as JSON, and set headers for JSON content
    response = requests.post(url, json=data)
    print(response.json())
    
    if response.status_code == 200:
        tokens = response.json()
        print("Login test passed: Access token:", tokens.get("access"))
        print("Login test passed: Refresh token:", tokens.get("refresh"))
        return tokens.get("access"), tokens.get("refresh")  # Return tokens for further tests
    else:
        print(f"Login test failed: {response.status_code}, {response.text}")
        return None, None

# Function to test refresh token (if implemented)
def test_refresh_token(refresh_token):
    url = BASE_URL + "token/refresh/"
    data = {
        "refresh": refresh_token
    }
    
    # Send data as JSON, and set headers for JSON content
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        tokens = response.json()
        print("Refresh token test passed: New access token:", tokens.get("access"))
    else:
        print(f"Refresh token test failed: {response.status_code}, {response.text}")

if __name__ == "__main__":
    # Run the tests
    print("Running signup and login tests...\n")

    # Test signup
    test_signup()

    # Test login and get tokens
    access_token, refresh_token = test_login()

    if access_token and refresh_token:
        # Test refresh token functionality
        test_refresh_token(refresh_token)
