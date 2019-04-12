import os

BIND_HOST = '127.0.0.1'
BIND_PORT = 9992

BASE_DIR = os.path.dirname(os.path.dirname(os.path.join(os.path.abspath(__file__))))

USER_HOME = os.path.join(BASE_DIR,'home')

print('Base_Dir:%s'%BASE_DIR)
print('User_home:%s'%USER_HOME)

