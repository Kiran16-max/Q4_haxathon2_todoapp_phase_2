import socket

def check_port(host, port):
    """Check if a port is open on the given host."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)  # 3 second timeout
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except Exception:
        return False

if check_port('localhost', 8000):
    print("Port 8000 is open - backend server is running")
else:
    print("Port 8000 is closed - backend server is not running")