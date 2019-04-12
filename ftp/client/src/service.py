import json
import socket

import sys

from ftp.client.config import settings


def main():
    """
    创建Socket连接
    :return:
    """
    # 添加ip及端口
    ip_port = (settings.server, settings.port)
    # 获得Socket对象
    conn = socket.socket()
    # 建立连接
    conn.connect(ip_port)
    # 获取欢迎语
    welcome_btyes = conn.recv(1024)
    # 输出欢迎语
    print(str(welcome_btyes, encoding='utf-8'))
    # 执行
    execute(conn)
    # 关闭连接
    conn.close()


def execute(conn):
    # 设置命令字典
    choice_dict = {
        'cmd' : cmd,
        'get': get,
        'post':post,
    }
    # 显示命令介绍
    help_info()
    while True:
        inp = input("请输入内容：")
        if inp == 'help':
            help_info()
            continue
        choice = inp.split('|')[0]
        if choice == 'exit':
            return
        if choice in choice_dict:
            func = choice_dict[choice]
            func(conn,inp)
def cmd(conn, inp):
    # 发送消息
    conn.sendall(bytes(inp,encoding='utf-8'))
    # 接收消息字节内容
    basic_info_bytes = conn.recv(1024)
    # 字节转换为字符串
    basic_info_str = str(basic_info_bytes,encoding='utf-8')
    # 判断返回信息是否为4001
    if basic_info_str == "4001":
        #登陆
        login(conn)
    else:
        pass
def get():
    pass
def post():
    pass

def help_info():
    """
    介绍命令方法
    :return:
    """
    print("""
        cmd|命令
        post|文件路径
        get|下载文件路径
        exit|退出
    """)
def login(conn):
    while True:
        # 输入用户名
        username = input('请输入用户名称：')
        password = input('请输入密码：')
        # 封装Json
        login_json = {'username':username, 'password':password}
        # 发送信息
        conn.sendall(bytes(json.dumps(login_json),encoding='utf-8'))
        # 获取返回信息
        recv_str = str(conn.recv(1024),encoding='utf-8')
        if recv_str == '4002':
            print("授权成功")
            break
        else:
            print("用户名密码错误")