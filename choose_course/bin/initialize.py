#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os,sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)
from src.service import initialize_service


def execute():
    initialize_service.main()

if __name__ == '__main__':
    execute()
