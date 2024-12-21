import requests
import jwt

# The base URL of your API
BASE_URL = "http://127.0.0.1:8000/api/v1/"

# Signup test
def test_signup():
    url = BASE_URL + "signup/"
    data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "password123",
        "role": "User"
    }
    
    response = requests.post(url, json=data)
    
    if response.status_code == 201:
        print("Signup test passed: User created successfully!")
    else:
        print(f"Signup test failed: {response.status_code}, {response.text}")

# Login test
def test_login():
    url = BASE_URL + "login/"
    data = {
        "username": "testuser",
        "password": "password123"
    }
    
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        tokens = response.json()
        print("Login test passed: Access token:", tokens.get("access"))
        print("Login test passed: Refresh token:", tokens.get("refresh"))
        return tokens.get("access")  # Return the access token for further tests
    else:
        print(f"Login test failed: {response.status_code}, {response.text}")
        return None

# Function to create a vendor item
def test_create_vendor_item(access_token):
    url = BASE_URL + "vendors/"
    headers = {
        "Authorization": f"Bearer {access_token}"  # Ensure you're sending the token in the headers
    }
    data = {
        "user": 1,  # Assuming the user ID of the test user is 1
        "name": "Vendor A",
        "quantity": 100,
        "quality": "High",
        "price": 19.99,
        "message": "A high-quality product."
    }
    
    print("Sending request with Authorization header:", headers)  # Debugging line
    
    response = requests.post(url, json=data, headers=headers)  # Ensure headers are correctly set
    
    if response.status_code == 201:
        print("Create vendor item test passed!")
        return response.json()  # Return the created item details (for future tests)
    else:
        print(f"Create vendor item test failed: {response.status_code}, {response.text}")
        return None

# Function to list all vendor items
def test_list_vendor_items(access_token):
    url = BASE_URL + "vendors/"
    headers = {
        "Authorization": f"Bearer {access_token}"  # Include the token in the headers
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("List vendor items test passed!")
        print(response.json())  # Print the list of vendor items
    else:
        print(f"List vendor items test failed: {response.status_code}, {response.text}")

# Function to update a vendor item
def test_update_vendor_item(access_token, vendor_id):
    url = BASE_URL + f"vendors/{vendor_id}/"
    headers = {
        "Authorization": f"Bearer {access_token}"  # Include the token in the headers
    }
    updated_data = {
        "name": "Updated Vendor A",
        "quantity": 200,
        "quality": "Premium",
        "price": 29.99,
        "message": "Updated high-quality product."
    }
    
    response = requests.put(url, json=updated_data, headers=headers)
    
    if response.status_code == 200:
        print("Update vendor item test passed!")
        print(response.json())  # Print the updated vendor item details
    else:
        print(f"Update vendor item test failed: {response.status_code}, {response.text}")

# Function to delete a vendor item
def test_delete_vendor_item(access_token, vendor_id):
    url = BASE_URL + f"vendors/{vendor_id}/"
    headers = {
        "Authorization": f"Bearer {access_token}"  # Include the token in the headers
    }
    
    response = requests.delete(url, headers=headers)
    
    if response.status_code == 204:
        print("Delete vendor item test passed!")
    else:
        print(f"Delete vendor item test failed: {response.status_code}, {response.text}")

# Main function to run tests
if __name__ == "__main__":
    # Run the tests
    print("Running tests...\n")

    # Test signup
    test_signup()

    # Test login and get the access token
    access_token = test_login()
    
    print("access_token :", access_token)  # Print the access token for debugging

    if access_token:
        # Create a new vendor item
        created_item = test_create_vendor_item(access_token)

        if created_item:
            # Test listing all vendor items
            test_list_vendor_items(access_token)

            # Test updating the created vendor item
            test_update_vendor_item(access_token, created_item['id'])

            # Test deleting the created vendor item
            test_delete_vendor_item(access_token, created_item['id'])
