# -*- coding: utf-8 -*-
# !/usr/bin/env python
# author = Chris Hong

from Proxy import *

reload(sys)
sys.setdefaultencoding('utf-8')

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class SpiderTask:
    def __init__(self, rs, params, txt=None):
        self.rs = rs
        self.params = params
        self.txt = txt

    def http_spider(self, url, timeout=5000):
        proxies = random_proxy(http_ip=True)
        headers = random_headers()
        try:
            resp = self.rs.get(url, proxies=proxies, headers=headers, timeout=timeout)
            if resp.status_code != 200:
                logging.error("Error: " + resp.text + "StatusCode: " + str(resp.status_code))
                return 'error'
            else:
                return resp.text
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
            text = self.http_spider(i)

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
