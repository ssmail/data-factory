# -*- coding: utf-8 -*-
# !/usr/bin/env python
# __author__ = 'hongkefeng'

import time
from yxt import vote
import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import sys
from task_screen_shot import *

reload(sys)
sys.setdefaultencoding('utf-8')
from Proxy import random_proxy

options = webdriver.ChromeOptions()
options.add_argument("--headless")

chromedriver = "/usr/local/Cellar/chromedriver/2.29/bin/chromedriver"

# init the driver
driver = webdriver.Chrome(chromedriver, chrome_options=options)
driver.set_page_load_timeout(30)


def get_cookies(temp_cookies):
    str_cookies = {}
    for cookie in temp_cookies:
        str_cookies[cookie['name']] = cookie['value']
    return str_cookies


s = requests.session()

# 超时时间设置
driver.set_page_load_timeout(10)

# 等待时间
driver.implicitly_wait(5)

for i in range(1, 3):
    proxies = random_proxy(https_ip=False)

    driver.get("https://www.wjx.cn/wjx/join/AntiSpamImageGen.aspx?q=21937277&t=1523870440009")

    get_element_image(driver, driver.find_element_by_tag_name("img"))

    if vote(s, proxies, get_cookies(driver.get_cookies())):
        print '投票成功'
    else:
        print '投票失败'

driver.quit()
