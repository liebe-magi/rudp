import socket

class UDPSender:
    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def send(self, msg):
        '''
        UDP送信
        [i] msg:入力テキスト(str)
        '''
        data = msg.encode('utf-8')

        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.sendto(data, (self.host, self.port))