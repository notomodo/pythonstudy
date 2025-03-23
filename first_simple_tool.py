import random  
import time  
from getpass import getpass  

logs = [  
    "INFO: User logged in",  
    "ERROR: Disk full",  
    "DEBUG: Connection established",  
    "INFO: User logged in",  
    "ERROR: Disk full",  
    "DEBUG: Connection established",  
    "INFO: User logged in",  
    "ERROR: Disk full",  
    "DEBUG: Connection established",  
    "ERROR: Invalid credentials"  
]  

def check_strength(password):  
    """  
    Checks the strength of a password based on length, digits, and uppercase letters.  
    Returns: 'strong', 'missing uppercase', 'missing digit', 'very weak', or 'too short'.  
    """  
    digit_present = 0  
    uppercase_present = 0  

    for i in password:  
        if i.isdigit():  
            digit_present += 1  
        if i.isupper():  
            uppercase_present += 1  

    if len(password) >= 8:  
        if digit_present >= 1 and uppercase_present >= 1:  
            return "strong"  
        elif digit_present >= 1:  
            return "missing uppercase"  
        elif uppercase_present >= 1:  
            return "missing digit"  
        else:  
            return "very weak"  
    else:  
        return "too short"  

def count_errors(logs):  
    """Counts the number of ERROR entries in a list of logs."""  
    errors = 0  
    for log in logs:  
        if 'ERROR' in log.upper():  
            errors += 1  
    return errors  

def retry_connection(max_retries):  
    """Attempts a network connection with retries. Returns True if successful."""  
    while max_retries > 0:  
        if random.randint(0, 1) == 1:  
            return True  
        max_retries -= 1  
        time.sleep(2)  
    return False  

# Main Workflow  
password = getpass("Enter your password: ").strip()  
print(f"Password strength: {check_strength(password)}")  

print(f"Analyzing logs... Found {count_errors(logs)} errors.")  

if retry_connection(3):  
    print("Connection successful! 🎉")  
else:  
    print("Connection failed! 🔒")  