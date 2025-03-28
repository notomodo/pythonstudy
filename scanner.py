import socket, argparse
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            return result == 0
    except socket.error:
        return False

def get_banner(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((host, port))
            banner = s.recv(1024).decode().strip()
            return banner if banner else "No banner"
    except:
        return "No banner"

def scan_ports(host, ports):
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = {port: executor.submit(scan_port, host, port) for port in ports}
        for port, future in results.items():
            if future.result():
                banner = get_banner(host, port)
                open_ports.append((port, banner))
    return open_ports

def parse_args():
    parser = argparse.ArgumentParser(
        description="Advanced Port Scanner",
        epilog="Example: python scanner.py 192.168.1.1 -p 1-1000"
    )
    parser.add_argument("host", help="Target host (IP or domain)")
    parser.add_argument("-p", "--ports", 
                        help="Port range to scan (e.g., '1-1000')", 
                        default="1-1024")
    parser.add_argument("-t", "--threads", 
                        help="Number of threads (default: 100)", 
                        type=int, 
                        default=100)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    ports = parse_ports(args.ports)
    open_ports = scan_ports(args.host, ports)
    
    print(f"Scanning {args.host}...")
    for port, banner in open_ports:
        print(f"Port {port}: Open | Banner: {banner}")
