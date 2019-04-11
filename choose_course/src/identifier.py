# -*- coding:utf-8 -*-

from lib import commons
import os
import pickle

class Nid:
    def __init__(self, role, db_path):
        """
        标识唯一ID
        :param role:
        :param db_path:
        """
        role_list = [
            'admin', 'school', 'teacher', 'course', 'course_to_teacher', 'classes', "student"
        ]

        if role not in role_list:
            raise Exception('用户角色错误，选择为：%s' % ",".join(role_list))

        self.role = role
        self.uuid = commons.create_uuid()
        self.db_path = db_path

    def __str__(self):
        return self.uuid

    def get_obj_by_uuid(self):
        for name in os.listdir(os.path.join(self.db_path)):
            if name == self.uuid:
                return pickle.load(open(os.path.join(self.db_path,self.uuid),'rb'))

class AdminNid(Nid):
    def __init__(self,db_path):
        super(AdminNid,self).__init__('admin',db_path)
