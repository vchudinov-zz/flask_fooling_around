import ping,socket

def get_service_status(hostname, port):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((hostname, port))
        return True
    except socket.error as e:
        return False
    s.close()

def get_ping(hostname):
    try:
        ping.verbose_ping(hostname, count = 3)
        return True
    except socket.error, e:
        return False
