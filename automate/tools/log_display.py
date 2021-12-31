#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/31 2:58 下午
# @Author  : xin
# @Detail  : 日志打印

import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def log_display(params, response):
    logging.info(f'请求参数：{params}')
    logging.info(f'响应结果：{response}')
    logging.info('-' * 100)
