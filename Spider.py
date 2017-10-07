# -*- coding: utf-8 -*-
# !/usr/bin/env python
# author = Chris Hong

from Proxy import *

reload(sys)
sys.setdefaultencoding('utf-8')

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class SpiderTask:
    def __init__(self, rs, params, txt=None, encoder='utf-8', use_proxy=False):
        self.rs = rs
        self.params = params
        self.txt = txt
        self.encoder = encoder
        self.use_proxy = use_proxy

    def http_spider(self, url, timeout=5000):
        headers = random_headers()
        try:
            if self.use_proxy:
                proxies = random_proxy(http_ip=True)
                resp = self.rs.get(url, proxies=proxies, headers=headers, timeout=timeout)
            else:
                resp = self.rs.get(url, headers=headers, timeout=timeout)

            print 'start url: ' + url

            if resp.status_code != 200:
                logging.error("Error: " + resp.text + "StatusCode: " + str(resp.status_code))
                return 'error'
            else:
                return resp.text, resp.encoding
        except Exception, e:
            print "CRANIAL ERROR: ", e.message

    def generate_task_url(self):
        return [self.params.url.replace(self.params.params_string, str(idx)) for idx in self.params.list_range]

    def clean(self, text):
        return self.params.dustman(text)

    def start(self):
        result = []
        all_url = self.generate_task_url()

        for i in all_url:

            # get http respond text
            text, encode = self.http_spider(i)

            # encode
            text = text.encode(encode).decode(self.encoder, 'ignore')

            # clean data from respond text
            for info in self.clean(text):
                result.append(info)

        if self.txt:
            with open(self.txt, 'a') as f:
                f.writelines("\n".join(result))

        return result


class Params:
    def __init__(self, url, params_string, list_range, dustman):
        self.url = url
        self.params_string = params_string
        self.list_range = list_range
        self.dustman = dustman
