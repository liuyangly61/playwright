#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @File : example1.py
# @Time : 2022/4/24 15:35
# @Author : liuyang28599
# @Version : 1.0
# @Product : PyCharm
# @Desciption : 采用pytest改造脚本
"""
import pytest
from playwright.sync_api import sync_playwright


class TestDemo:
    browser = None
    playwright = None

    # 用例执行的前置条件
    @classmethod
    def setup_class(cls):
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch(headless=False)
        cls.page = cls.browser.new_page()

    # 用例执行的后置操作
    @classmethod
    def teardown_class(cls):
        cls.browser.close()
        cls.playwright.stop()

    # 具体的测试用例
    # 登录用例
    def test_login(cls):
        cls.page.goto('http://dsdprotest.5ibazhuayu.com.cn/hui-uc/#/login')
        # 填充username
        cls.page.fill('//*[@id="app"]/div[1]/div[1]/div/div/div[3]/form[1]/div[1]/div[2]/div[1]/input', '18800000001')
        # 填充password
        cls.page.fill('//*[@id="app"]/div[1]/div[1]/div/div/div[3]/form[1]/div[2]/div[2]/div[1]/input', '123456Bb')
        # 点击登录
        cls.page.click('//*[@id="app"]/div[1]/div[1]/div/div/div[3]/div/button')
        # 等待3s
        cls.page.wait_for_timeout(3000)

    # 修改用户信息
    def test_modifyavatar(cls):
        # 修改用户名称
        cls.page.hover('//html/body/div[1]/div[1]/div[1]/div[1]/div/div[3]/ul/li[2]/div[1]/div')
        cls.page.click('//html/body/div[1]/div[1]/div[1]/div[1]/div/div[3]/ul/li[2]/div[2]/li[3]/div/div[1]/div/span')
        cls.page.fill('//div[@class="h-form-item h-form-item-required h-form-col-2"]/div['
                      '@class="h-form-item-content"]/div[@class="h-input-wrapper h-input-type"]/input[@class="h-input '
                      'h-input-left"and@maxlength="30"]', '通过playwright修改的用户2')
        cls.page.click('//html/body/div[8]/div[2]/div/div[3]/div/button[2]/span')
        cls.page.wait_for_timeout(3000)


if __name__ == "__main__":
    pytest.main(["-s", "example1.py"])
