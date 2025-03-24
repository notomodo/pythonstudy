import hashlib  
from getpass import getpass

def hash_password(password):  
    # Create a SHA-256 hash object  
    sha256 = hashlib.sha256()  
    # Update the hash with the password bytes  
    sha256.update(password.encode('utf-8'))  
    # Return the hexadecimal digest  
    return sha256.hexdigest()  

# Example usage  
password = getpass("Password: ") 
hashed_password = hash_password(password)  
print(f"Password hash: {hashed_password} for Password: {password}")  

# Verify a password  
input_password = password  
input_hash = hash_password(input_password)  
if input_hash == hashed_password:  
    print("Password verified! ✅")  
else:  
    print("Invalid password! ❌")  
