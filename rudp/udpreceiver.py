import socket

class UDPReceiver:
    def __init__(self, host, port, bufsize=4096):
        self.host = host
        self.port = port
        self.bufsize = bufsize

    def receive(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind((self.host, self.port))
            while True:
                data, _ = s.recvfrom(self.bufsize)
                msg = data.decode('utf-8', errors='replace').strip()

                yield msg