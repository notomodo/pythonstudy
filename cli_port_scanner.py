import socket, argparse

def scan_port(host, port):
	try:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.settimeout(1)
			result = s.connect_ex((host,port))
			return result == 0
	except socket.err:
		return False


host = "localhost"
for port in [80, 22, 21, 443]:
	if scan_port(host,port):
		print(f"Port {port}: Open")
