#用户信息（登陆密码验证，账户及密码存储,加密用户信息）


class UserInfo :
    """
    用户信息类
    """
    def __init__(self,id,name, password,age,path):
        """
        初始化方法
        :param id: 用户ID
        :param name: 用户名称
        :param password: 用户密码
        :param age: 用户年龄
        :param path: 用户FTP路径
        """
        self.id = id
        self.name = name
        self.password = password
        self.age = age
        self.path = path

    def register_account(self,name,password,age):
        """
        注册账户方法
        :param name:  用户名称
        :param password: 用户密码
        :param age: 年龄
        :return: bool 是否注册成功  True成功  or  False失败
        """
        pass

    def login_account(self,name, password):
        """
        登陆方法
        :param name: 用户名称
        :param password: 密码
        :return: bool 是否登陆成功标记  True成功  or  False失败
        """
    def __encryption(self):
        """
        加密方法
        :return:
        """
        pass

