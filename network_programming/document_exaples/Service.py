import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())

class MyTCPHandler1(socketserver.StreamRequestHandler):
    def handle(self):
        self.data = self.rfile.readline().strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.wfile.write(self.data.upper())


if __name__ == '__main__':
    HOST, PORT = "192.168.1.82", 9999

    with socketserver.TCPServer((HOST,PORT),MyTCPHandler1) as server:
        server.serve_forever()
