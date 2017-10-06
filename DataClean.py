# -*- coding: utf-8 -*-
# !/usr/bin/env python
# author = Chris Hong
from Proxy import *
import re


def clean_data_tmall(original_string):
    result = []
    if not original_string:
        return []

    s = original_string.replace('"rateDetail":', "")
    rate = s2json(s)['rateList']
    for j in rate:
        result.append(j['rateContent'])

    return result


def clean_data_jd(original_string):
    result = []
    if not original_string:
        return []

    rate = s2json(original_string)['comments']
    for j in rate:
        result.append(j['content'])

    return result


def clean_name(original_string):
    if not original_string:
        return []

    names = re.findall(u"target='_blank'>(洪.+?)<\/a>", original_string)

    if names:
        return names
    else:
        return []


def clean_by_re(original_string):
    if not original_string:
        return []

    names = re.findall(u'target="_blank">(洪.+)<\/a><spa', original_string)

    if names:
        return names
    else:
        return []
