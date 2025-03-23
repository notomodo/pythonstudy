import datetime
from getpass import getpass

# Simulated user database (plaintext for demo purposes)
users = {"admin": "password123"}

# --- Functions ---
def login(username, password):
    """Validates credentials against the user database."""
    return users.get(username) == password  # Simple validation

def log_attempt(username, success):
    """Logs login attempts to a file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "SUCCESS" if success else "FAIL"
    log_entry = f"{timestamp} | User: {username} | Status: {status}\n"

    with open("login_attempts.log", "a") as f:
        f.write(log_entry)

def count_errors(logs):
    """Counts the number of FAIL entries in logs."""
    return sum(1 for log in logs if "FAIL" in log)

def detect_brute_force():
    """Checks for >3 FAILED attempts in the last 5 minutes."""
    try:
        with open("login_attempts.log", "r") as f:
            logs = f.readlines()
    except FileNotFoundError:
        return False  # No log file yet

    now = datetime.datetime.now()
    fail_count = 0

    for log in logs:
        if "FAIL" in log:
            # Extract timestamp from log entry
            timestamp_str = log.split("|")[0].strip()
            log_time = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            # Check if the log is within the last 5 minutes
            if (now - log_time).total_seconds() < 300:  # 5 minutes = 300 seconds
                fail_count += 1

    return fail_count > 3

# --- Main Workflow ---
max_attempts = 3
success = False

for _ in range(max_attempts):
    username = input("Username: ").strip()
    password = getpass("Password: ").strip()
    success = login(username, password)
    log_attempt(username, success)

    if success:
        print("Login successful! 🎉")
        break
    else:
        print("Invalid credentials! ❌")

# Check for brute-force attacks
if detect_brute_force():
    print("ALERT: Brute-force attack detected! 🔥")