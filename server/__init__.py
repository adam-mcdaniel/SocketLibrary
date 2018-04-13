# coding: latin-1
import socket
import threading
# from urllib3 import urlopen

class Server():
    def __init__(self,port):

        self.clients = []
        self.messages = {}

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("gmail.com",80))
        self.host = s.getsockname()[0]
        s.close()
        self.host = "127.0.0.1"

        # port = int(input('Port:'))
        self.port = port
        self.s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.s.bind((self.host,self.port))

        self.addr = (self.host,self.port)

        threading.Thread(target=self.run, args=(0,)).start()
        threading.Thread(target=self.run, args=(1,)).start()

    def run(self, worker):
        while True:
            if worker == 0:
                data, addr = self.receive()

                if addr not in self.clients:
                    self.clients.append(addr)

                self.messages[addr] = data

            if worker == 1:
                for client in self.clients:
                    self.send({k: v for k, v in self.messages.items() if k != client}, client)

        s.close()

    def send(self, data, addr):
        self.s.sendto(str.encode(str(data)), addr)

    def receive(self):
        data, addr = self.s.recvfrom(4096)
        data = data.decode('utf-8')
        return eval(data), addr

if __name__=="__main__":
    # my_ip = urlopen('http://ip.42.pl/raw').read()
    # print("public ip: " + str(my_ip))
    s = Server(7005)
    s.start()
