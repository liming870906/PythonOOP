
# -*- coding:utf-8 -*-
import os
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print("BaseDir:%s" %BASEDIR)

ADMIN_DB = os.path.join(BASEDIR,"db",'admin')