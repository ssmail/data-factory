# -*- coding: utf-8 -*-
# !/usr/bin/env python
# author = Chris Hong
import requests
from Spider import *
import DataClean

rs = requests.session()

reload(sys)
sys.setdefaultencoding('utf-8')

page_param = '[page]'
page = range(1, 10)

# taobao:
# tmall_url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=41464129793&sellerId=1652490016&currentPage=[page]'
# tm_params = Params(tmall_url, page_param, page, DataClean.clean_data_tmall)
# tm_spider = SpiderTask(rs, tm_params, "tm_res.txt", use_proxy=True)
# tm_spider.start()

# jd:
# jd_url = 'https://club.jd.com/comment/productPageComments.action?productId=4751753&score=0&sortType=6&page=[page]&pageSize=10'
# jd_dustman = clean_data_jd
# jd_params = Params(jd_url, page_param, page, jd_dustman)
# jd_spider = SpiderTask(rs, jd_params, "jd_res.txt")
# jd_spider.start()encoder


# name:
name_url = 'http://www.sheup.com/mianfeiqiming.php?qiming=%BA%E9&page=[page]&setsex=boy&setming=0'
jd_params = Params(name_url, page_param, page, DataClean.clean_name)

jd_spider = SpiderTask(rs, jd_params, "name.txt", encoder='gbk')
jd_spider.start()

#
# name_url = 'http://www.xingyunba.com/quming/bzname.php?page=[page]&xing=%E6%B4%AA&sex=1&whh=0'
# jd_params = Params(name_url, page_param, page, DataClean.clean_by_re)
# jd_spider = SpiderTask(rs, jd_params, "names.txt", use_proxy=False)
#
# jd_spider.start()
