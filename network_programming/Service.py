
# import socket
#
# socket_service = socket.socket(
#     socket.AF_INET,
#     socket.SOCK_STREAM
# )
#
# 设置地址元组
address = (
    "192.168.1.82",
    8989
)
#
# # 绑定端口号
# socket_service.bind(address)
#
# # 设置最大连接数
# socket_service.listen(5)
#
# while True:
#     """
#         循环建立连接
#     """
#     # 建立客户端连接
#     client_socket, addr = socket_service.accept()
#
#     print("连接地址：%s" %str(addr))
#
#     msg = '欢迎来到Soket课堂' +"\r\n"
#     client_socket.send(msg.encode('utf-8'))
#     client_socket.close()

# 使用Socketserver控件实现服务器

import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print("服务端启动")
        while True:
            conn = self.request
            print(self.client_address)
            while True:
                client_data = conn.recv(2048)
                print(str(client_data,"utf-8"))
                print("等待...")
                conn.sendall(client_data)
            conn.close()

if __name__ == '__main__':
    # 初始化ThreadServer
    server = socketserver.ThreadingTCPServer(address,MyServer)
    # 启动server
    server.serve_forever()




































