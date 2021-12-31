#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/30 3:27 下午
# @Author  : xin
# @Detail  : 数据操作

import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def get_csv_data(file_path):
    """
    读取csv文件存入Python列表
    :param file_path: csv文件路径
    :return: list列表
    """
    res_list = []
    try:
        with open(file_path, encoding="utf-8") as f:
            data = f.readlines()
            for i in data:
                res_list.append(i.strip().split(","))
    except Exception:
        logging.warning('文件不存在')

    return res_list


if __name__ == '__main__':
    logging.info(get_csv_data())
