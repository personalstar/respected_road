#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/24 3:12 下午
# @Author  : xin
# @Detail  :

import os
from logger import logger
import pandas as pd
import time


def get_file_name(path, name_suffix=None):
    """
    获取文件夹下指定后缀的文件名
    :param path: 文件夹目录
    :param name_suffix: 后缀
    :return: 文件夹下指定后缀的文件名数组
    """
    try:
        names = os.listdir(path)
        result = []
        if name_suffix:
            for name in names:

                if os.path.splitext(name)[1] == name_suffix:
                    result.append(name)
                    logger.info(name)
        else:
            result = names
        logger.info("已读取并保存目标文件夹下所有指定后缀的文件名")
        return result
    except Exception:
        logger.info("路径不存在或路径下无指定后缀文件")


def save_in_excel(path, file_list):
    """
    将多个csv文件合并成一个Excel文件，并分页保存
    :param path: 文件夹路径
    :param file_list: 文件名数组
    :return:
    """
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    writer = pd.ExcelWriter(path + '//' + now + r"report.xlsx")

    for file in file_list:
        data = pd.read_csv(path + '//' + file, encoding='utf-8')
        data.to_excel(writer, file, na_rep='', index=False)
        logger.info(file + "已写入Excel")

    writer.save()


if __name__ == '__main__':
    # 路径 && 后缀
    root_path = r'E:\test'
    suffix = '.csv'

    start_time = time.time()

    res = get_file_name(root_path, suffix)
    save_in_excel(root_path, res)

    end_time = time.time()
    logger.info('总共耗费了%.2f秒.' % (end_time - start_time))
