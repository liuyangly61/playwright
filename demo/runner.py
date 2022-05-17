#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @File : runner.py
# @Time : 2022/4/22 9:43
# @Author : liuyang28599
# @Version : 1.0
# @Product : PyCharm
# @Desciption : None
"""
import os

import pytest

if __name__ == "__main__":
    os.system("rd /s/q temp")
    os.system("rd /s/q report")
    pytest.main(["-s", "test_web.py", "--alluredir", "./temp"])
    os.system("allure generate ./temp -o ./report --clean")

