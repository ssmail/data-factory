# -*- coding: utf-8 -*-
# !/usr/bin/env python
# author = Chris Hong
import requests
from Spider import *
from DataClean import *

rs = requests.session()

page_param = '[page]'
page = range(1, 10)

# taobao:

tmall_url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=41464129793&sellerId=1652490016&currentPage=[page]'
tm_dustman = clean_data_tmall
tm_params = Params(tmall_url, page_param, page, tm_dustman)
tm_spider = SpiderTask(rs, tm_params, "tm_res.txt")
tm_spider.start()

# jingodng:
jd_url = 'https://club.jd.com/comment/productPageComments.action?productId=4751753&score=0&sortType=6&page=[page]&pageSize=10'
jd_dustman = clean_data_jd
jd_params = Params(jd_url, page_param, page, jd_dustman)
jd_spider = SpiderTask(rs, jd_params, "jd_res.txt")
jd_spider.start()
