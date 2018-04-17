# -*- coding: utf-8 -*-
# !/usr/bin/env python
# __author__ = 'hongkefeng'
import cookielib
import os
import urllib2

import requests
import datetime
import time
from random import randint
from Proxy import *
from aip import AipOcr
from PIL import Image, ImageDraw, ImageFont  # dynamic import

from baidu import image2str


def vote(session, proxies, cookies):
    data = {"submitdata": "1$%s}2$%s}3$%s}4$%s}5$%s}6$%s}7$%s}8$%s}9$%s}10$%s}11$%s" % (
        str(randint(1, 2)), str(randint(1, 2)), str(randint(1, 2)), str(randint(1, 2)), str(randint(1, 2)),
        str(randint(1, 2)), str(randint(1, 2)), str(randint(1, 2)), str(randint(1, 2)), str(randint(1, 2)),
        str(randint(1, 2)))}

    nowTime = int(round(time.time() * 1000))
    time.sleep(3)
    rn = str(randint(0, 999999999)).zfill(9)

    baidu_img_text = image2str("screenshot.png")

    img_text = raw_input("如果验证码准确，请直接按回车，如果验证码不准，请输入验证码后回车:")

    if len(img_text) == 4:
        img_text = img_text
    else:
        img_text = baidu_img_text

    base_url = "http://www.wjx.cn/joinnew/processjq.ashx?"
    url = "submittype=1&curID=21937277&t=" + str(nowTime) + "&rn=" + rn + "&validate_text=" + img_text

    full_url = base_url + url

    r = session.post(url=full_url, data=data, proxies=proxies, cookies=cookies, verify=False)

    return 'complete.aspx' in r.text
