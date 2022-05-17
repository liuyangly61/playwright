#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @File : example2.py
# @Time : 2022/4/22 15:40
# @Author : liuyang28599
# @Version : 1.0
# @Product : PyCharm
# @Desciption : None
"""

from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://hs-cas.hundsun.com/cas/login?service=https%3A%2F%2Fse.hundsun.com%2F
    page.goto("https://hs-cas.hundsun.com/cas/login?service=https%3A%2F%2Fse.hundsun.com%2F")
    # Click [placeholder="域账号"]
    page.locator("[placeholder=\"域账号\"]").click()
    # Fill [placeholder="域账号"]
    page.locator("[placeholder=\"域账号\"]").fill("liuyang28599")
    # Press Tab
    page.locator("[placeholder=\"域账号\"]").press("Tab")
    # Fill [placeholder="密码"]
    page.locator("[placeholder=\"密码\"]").fill("hundsun@456")
    # Press Enter
    page.locator("[placeholder=\"密码\"]").press("Enter")
    # expect(page).to_have_url("https://se.hundsun.com/secure/RapidBoard.jspa")
    # Go to https://se.hundsun.com/secure/RapidBoard.jspa?rapidView=65
    page.goto("https://se.hundsun.com/secure/RapidBoard.jspa?rapidView=65")

    # Click img[alt="刘阳\(28599\)的个人信息"]
    page.locator("img[alt=\"刘阳\\(28599\\)的个人信息\"]").click()
    # Click text=用户信息
    page.locator("text=用户信息").click()
    # expect(page).to_have_url("https://se.hundsun.com/secure/ViewProfile.jspa")
    # Click #details-user-avatar-trigger
    page.locator("#details-user-avatar-trigger").click()
    # Click text=上传一个新图像
    page.locator("text=上传一个新图像").click()
    # Upload 李白.jpg
    page.locator("input[name=\"avatar\"]").set_input_files("F:\王者q版头像\李白.jpg")
    # 等待3s
    page.wait_for_timeout(3000)

    # Click text=确认
    page.locator("text=确认").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
