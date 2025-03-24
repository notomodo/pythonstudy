import socket

def check_port(host,port):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(1)
		result = sock.connect_ex((host,port))
		sock.close()
		return result == 0  # True if open, False otherwise
	except socket.error:
		return False

# Testing common ports
target_host = "localhost"
ports_to_scan = [80, 443, 22, 21, 8080, 5001]

for port in ports_to_scan:
	if check_port(target_host, port):
		print(f"Port {port}: Open 🟢")
	else:
		print(f"Port {port}: Closed 🔴")
