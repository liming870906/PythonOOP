"""
应用程序入口
"""
import os, sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)

from bean import UserInfo

if __name__ == '__main__':
    exit_flag = False
    while not exit_flag:
        # 判断用户注册还是登陆
        code = input("账户登陆（1）or注册（2）:")
        if code.isdigit():
            pass
        else:
            print("输入错误请重新输入！")
