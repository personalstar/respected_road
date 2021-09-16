#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/13 5:36 下午
# @Author  : xin
# @Detail  : csv文件解析

import json
import re
import pandas as pd
import csv
import requests


# 提取csv文件内容参数
def get_messages():
    data = open(r'/Users/huangxiaoxin/Desktop/files/03_files/csv_files/creditLoan.csv',
                encoding='utf-8').read().splitlines()
    with open(r'/Users/huangxiaoxin/Desktop/files/03_files/csv_files/creditLoan_data', 'a+',
              encoding='utf-8') as f1:
        for i in data:
            i_list = i.split(',')
            # get_data = {'uri': i_list[0], 'patameter': i_list[1]}
            # get_data = {'patameter': i_list[0]}
            # f1.write(json.dumps(get_data) + '\n')

            get_data = i_list[0]
            print(get_data)
            f1.write(str(get_data) + '\n')


# 从url获取参数
def get_data(base_url):
    uri = '/xm-im-service/conversations/targetId'
    session = requests.session()
    line = open(r'D:\Cass\cassloadtest\LR\benchmark_test\xm\data\targetId', encoding='utf-8').read().splitlines()
    # line_dict = json.loads(line)

    for i in line:

        param = json.loads(i)
        res = session.request(method='get', url=base_url + uri, params=param)
        if res.json().get('latestMessage'):
            # data = {"fromUserId": res1.json()['latestMessage']['fromUserId'],
            #         "toUserId": res1.json()['latestMessage']['toUserId'],
            #         "content": res1.json()['latestMessage']['content']
            #         }
            # print(json.dumps(data, ensure_ascii=False))

            with open(r'D:\Cass\get_data\data\messages', 'a+',
                      encoding='utf-8') as f1:
                data = {"fromUserId": res.json()['latestMessage']['fromUserId'],
                        "toUserId": res.json()['latestMessage']['toUserId'],
                        "content": res.json()['latestMessage']['content']
                        }
                f1.write(json.dumps(data, ensure_ascii=False) + '\n')


# java日志获取指定字符串后参数值
def get_body_from_res():
    try:
        with open(r'./data/res1', encoding='utf-8') as f:
            pattern = re.compile(r'管理中心-卖家账单流水统计总金额，systemSellerBillFlowRequest ->SystemSellerBillFlowRequest\((.*?)\)"')
            lines = str(f.read())
            pat_all = pattern.findall(lines)

            with open(r'./data/res1_body', 'a+', encoding='utf-8') as f1:
                for i in pat_all:
                    print(type(i), i)

                    # str格式
                    # str1 = i.replace('\\', '')
                    # data = '{' + str1 + '}'
                    # f1.write(data + '\n')

                    # tuple格式(元组)
                    str1 = i.replace('=', '":"').replace(', ', '","')
                    data = '{"' + str1 + '"}'
                    f1.write(data + '\n')
    except FileNotFoundError:
        print('无法打开指定文件')
    except LookupError:
        print('指定了未知编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')


# 数据库获取组合参数
def com_params():
    try:
        with open(r'./data/res1', encoding='utf-8') as f:
            lines = f.readlines()

            with open(r'./data/res1_body', 'a+', encoding='utf-8') as f1:
                for i in lines:
                    print(i)
                    # i_list = i.split(' ')
                    # print(i_list)
                    # data = str({"partyIdTo": i_list[0], "serviceType": i_list[1]})
                    # data = data.replace('\'', '\"')
                    data = '["' + str(i) + '"]'
                    f1.write(data + '\n')

    except FileNotFoundError:
        print('无法打开指定文件')
    except LookupError:
        print('指定了未知编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')


if __name__ == '__main__':
    # get_messages()

    # 接口获取
    # base_url = "http://terminator-api.intra.casstime.com"
    # get_data(base_url)

    get_body_from_res()

    # com_params()
