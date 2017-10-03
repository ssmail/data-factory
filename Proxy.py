# -*- coding: utf-8 -*-
# !/usr/bin/env python
# author = Chris Hong
import re
import sys
import json
import random
import logging
from getproxy import GetProxy

reload(sys)
sys.setdefaultencoding('utf-8')

PROXY_FILE = "proxy"

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def random_headers():
    header = [{
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    }]
    return random.choice(header)


def proxy_center(http_ip=False, https_ip=False):
    proxys = []

    with open(PROXY_FILE, 'r') as f_proxy:
        proxy_list = f_proxy.readlines()

    for proxy in proxy_list:
        try:
            info = s2json(proxy)
            if info['type'] == 'http' and http_ip:
                proxys.append((info['type'], info['host'], info['port']))

            if info['type'] == 'https' and https_ip:
                proxys.append((info['type'], info['host'], info['port']))
        except Exception, e:
            logging.error("get proxy ip error: ", e.message)
            pass
    return proxys


def random_proxy(http_ip=True, https_ip=False):
    proxies = random.choice(proxy_center(http_ip=http_ip, https_ip=https_ip))
    return {proxies[0]: '{http}://{ip}:{port}'.format(http=proxies[0],
                                                      ip=proxies[1],
                                                      port=proxies[2])}


def s2json(json_input):
    try:
        decoded = json.loads(json_input)
        return decoded
    except (ValueError, KeyError, TypeError):
        print "JSON format error"


def update_proxy():
    g = GetProxy(output_proxies_file=PROXY_FILE)

    # 1. 初始化，必须步骤
    g.init()

    # 2. 加载 input proxies 列表
    g.load_input_proxies()

    # 3. 验证 input proxies 列表
    g.validate_input_proxies()

    # 4. 加载 plugin
    g.load_plugins()

    # 5. 抓取 web proxies 列表
    g.grab_web_proxies()

    # 6. 验证 web proxies 列表
    g.validate_web_proxies()

    # 7. 保存当前所有已验证的 proxies 列表
    g.save_proxies()


if __name__ == "__main__":
    update_proxy()
