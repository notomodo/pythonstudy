import argparse
import requests
from concurrent.futures import ThreadPoolExecutor

def check_dir(target_url, directory, timeout=2):
    full_url = f"{target_url}/{directory}"
    try:
        response = requests.get(full_url, timeout=timeout)
        if response.status_code == 200:
            return full_url
    except requests.exceptions.RequestException:
        pass
    return None

def load_wordlist(wordlist_path):
    with open(wordlist_path, "r") as f:
        return [line.strip() for line in f if line.strip()]

def brute_force(target_url, wordlist_path, max_threads=50):
    directories = load_wordlist(wordlist_path)
    found = []
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = {executor.submit(check_dir, target_url, dir): dir for dir in directories}
        for future in futures:
            result = future.result()
            if result:
                found.append(result)
    return found


def parse_args():
    parser = argparse.ArgumentParser(
        description="Directory/File Brute-Forcer",
        epilog="Example: python dir_brute.py http://example.com -w wordlist.txt -t 50"
    )
    parser.add_argument("url", help="Target URL (e.g., http://example.com)")
    parser.add_argument("-w", "--wordlist", 
                        help="Path to wordlist file (required)", 
                        required=True)
    parser.add_argument("-t", "--threads", 
                        help="Thread count (default: 50)", 
                        type=int, 
                        default=50)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    print(f"Scanning {args.url}...")
    found = brute_force(args.url, args.wordlist, args.threads)
    if found:
        print("\nFound directories/files:")
        for url in found:
            print(f"🔍 {url}")
    else:
        print("No directories found.")
