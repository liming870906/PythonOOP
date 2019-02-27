import socket

socket_client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

address = (
    "192.168.1.82",
    8989
)
# 连接服务器
socket_client.connect(address)
print("客户端启动")
while True:
    send_msg_content = input(">>")
    if send_msg_content == "exit":
        socket_client.close()
        break
    socket_client.send(send_msg_content.encode("utf-8"))
    # 接收数据
    msg = socket_client.recv(2048)
    print(msg.decode('utf-8'))
