# -*- coding:utf-8 -*-
import json
import socketserver

import os

from ftp.service.config import settings

ACTION_CODE = {
    '1000': 'cmd',
    '2000': 'post',
    '3000': 'get',
}

REQUEST_CODE = {
    '1001': 'cmd info',
    '1002': 'cmd ack',
    '2001': 'post info',
    '2002': 'ACK（可以开始上传）',
    '2003': '文件已经存在',
    '2004': '续传',
    '2005': '不续传',
    '3001': 'get info',
    '3002': 'get ack',
    '4001': "未授权",
    '4002': "授权成功",
    '4003': "授权失败"
}


class MultiServer(object):
    """
    启动并发的线程
    """
    def __init__(self):
        socketserver.ThreadingTCPServer((settings.BIND_HOST,settings.BIND_PORT),MultiServerHandler).serve_forever()

class MultiServerHandler(socketserver.BaseRequestHandler):
    """
    并发回调方法
    """
    def handle(self):
        conn = self.request
        conn.sendall(bytes("欢迎登陆",encoding='utf-8'))
        # 创建Action对象
        obj = Action(conn)
        # 循环获取客户端信息
        while True:
            client_bytes = conn.recv(1024)
            if not client_bytes:
                break
            client_str = str(client_bytes,encoding='utf-8')
            if obj.has_login:
                o = client_str.split('|',1)
                if len(o):
                    func = getattr(obj,o[0])
                    func(client_str)
                else:
                    conn.sendall(bytes('输入格式错误','utf-8'))
            else:
                obj.login(client_str)

class Action(object):

    def __init__(self,conn):
        # socket_service对象
        self.conn = conn
        # 登陆标记
        self.has_login = False
        # 用户名称
        self.username = None
        # 主目录
        self.home = None
        # 当前目录
        self.current_dir = None

    def login(self,origin):
        """
        登陆方法
        :param origin:
        :return:
        """
        self.conn.sendall(bytes("4001",encoding='utf-8'))
        # 循环
        while True:
            login_str = str(self.conn.recv(1024),encoding='utf-8')
            login_dict = json.loads(login_str,encoding='utf-8')
            if login_dict['username'] == 'James' and login_dict['password'] == '123':
                self.conn.sendall(bytes('4002',encoding='utf-8'))
                self.has_login = True
                self.username = "James"
                self.initialize()
                break
            else:
                self.conn.sendall(bytes("4003",encoding='utf-8'))

    def initialize(self):
        """
        初始化home和current_dir
        :return:
        """
        self.home = os.path.join(settings.USER_HOME,self.username)
        self.current_dir = os.path.join(settings.USER_HOME,self.username)
