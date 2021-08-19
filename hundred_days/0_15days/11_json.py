#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/19 11:43 上午
# @Author  : xin
# @Detail  : 对json数据处理

import json

"""
dump-将Python对象按照json格式序列化到文件中
dumps-将Python对象处理成json格式的字符串
load-将文件中的json数据反序列化成对象
loads-将字符串的内容反序列化成Python对象
"""


def main():
    mydict = {
        'name': '公孙离',
        'age': 18,
        'wechat': 'wechat123',
        'boyfriend': '李信',
        'cars': [
            {'brand': 'audi', 'price': '5w5'},
            {'brand': 'bmw', 'price': '6w6'},
            {'brand': 'benz', 'price': '7w7'}
        ]
    }

    try:
        with open('../data/json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('数据保存成功')

    try:
        with open('../data/json', 'r', encoding='utf-8') as fs2:
            data_json = json.load(fs2)
            print(data_json)
    except FileNotFoundError:
        print('无法打开指定文件')
    except LookupError:
        print('指定了未知编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')
    except IOError as e:
        print(e)
    print('数据保存成功')


if __name__ == '__main__':
    main()
