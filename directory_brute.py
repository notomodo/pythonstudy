import requests, time

def check_directory(url, directory):
    full_url = f"{url}/{directory}"
    try:
        response = requests.get(full_url)
        if response.status_code == 200:
            return f"Found: {full_url}"
    except requests.exceptions.RequestException:
        pass
    return None

# Test on a mock website
target_url = "https://httpbin.org"
# directories = ["admin", "login", "backup"]
# Read directories from a file
with open("common_dirs.txt", "r") as f:
    directories = f.read().splitlines()

for directory in directories:
    result = check_directory(target_url, directory)
    if result:
        print(result)

    time.sleep(1) # rate limiting

