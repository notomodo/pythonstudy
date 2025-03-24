import json
import hashlib

# File to store user data
FILE_NAME = "users.json"

# Load existing users from the file
def load_users():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}  # Return empty dictionary if file doesn't exist or is empty

# Save users to the file
def save_users(users):
    with open(FILE_NAME, "w") as file:
        json.dump(users, file, indent=4)

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Main logic
users = load_users()  # Load existing data

username = input("Enter username: ")
password = input("Enter password: ")
hashed_password = hash_password(password)

users[username] = hashed_password  # Store username and hashed password

save_users(users)  # Save updated dictionary back to file

print("User registered successfully!")
