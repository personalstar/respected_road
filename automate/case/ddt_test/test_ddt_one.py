#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/30 3:26 下午
# @Author  : xin
# @Detail  : DDT数据驱动demo1

import ddt
import unittest
import requests
import logging

from automate.tools.data_helper import get_csv_data
from automate.tools.log_display import log_display

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

base_url = "http://hwbeta-api.intra.casstime.com"


@ddt.ddt
class DemoOne(unittest.TestCase):

    # 装饰测试方法，添加测试数据
    @ddt.data(*get_csv_data('./data/demo.csv'))
    # 自动将文件中的参数对应到def方法的参数上
    @ddt.unpack
    def test_fastOeV2(self, vin, q, result):
        url = "/maindata-service/maindata/restApi/v1/oe/fastOeV2"
        data = {
            "vin": vin,
            "q": q,
            "remark": None
        }

        resp = requests.get(url=base_url + url, params=data)
        res = resp.json()
        res_assert = res["message"]
        log_display(data, res)

        assert res_assert == result, f'断言失败：{res_assert} == {result}'
