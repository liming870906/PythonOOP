# -x- coding:utf-8 -*-

import os
import pickle
import time
from config import settings
from src import identifier

class BaseModel:
    def save(self):
        """
        使用pickle将用户对象保存
        :return:
        """
        nid = str(self.nid)
        file_path = os.path.join(self.db_path,nid)
        pickle.dump(self,open(file_path,'wb'))

class Admin(BaseModel):
    """
    管理对象
    """
    db_path = settings.ADMIN_DB

    def __init__(self,username, password):
        self.nid = identifier.AdminNid(Admin.db_path)
        self.username = username
        self.password = password
        self.create_time = time.strftime('%Y-%m-%d')
    @staticmethod
    def login(user,pwd):
        for item in os.listdir(os.path.join(settings.ADMIN_DB)):
            obj = pickle.load(open(settings.ADMIN_DB,item))
            if user == obj.username and pwd == obj.password:
                return obj
        return None