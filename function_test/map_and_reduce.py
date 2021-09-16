#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/8 9:44 上午
# @Author  : xin
# @Detail  : map()函数 && reduce()函数

from functools import reduce

"""
语法：
map(function, lists)
第一个参数：函数，期望对lists进行的操作
第二个参数：列表，可多个
"""

list_org = [1, 2, 3, 4, 5, 6]
list_second = [10, 20, 30, 40]
list_str = ['123', '12345']


def add_one_more(x):
    return x + 1


"""利用外加函数"""
print(map(add_one_more, list_org))  # 返回地址
print(list(map(add_one_more, list_org)))  # 将对象序列化list返回：[2, 3, 4, 5, 6, 7]

"""第一参数使用lambda函数，直接定义如何操作(多)列表"""
y1 = list(map(lambda x, y: x + y, list_org, list_second))
print(y1)  # [11, 22, 33, 44]

"""将str列表转成int类型"""
print(list(map(int, list_str)))  # [123, 12345],若字符串存在字母，则会报错

"""
语法：
reduce(function,list)
第一个参数：函数，函数的参数必须为两个参数
第二个参数：列表
作用：reduce把结果和下一个元素做累计计算，计算方式由作为参数的函数决定
"""


# 累加求和，相当于sum
def add_tow_num(x, y):
    return x + y


# 将列表转换成整型数
def fn(x, y):
    return x * 10 + y


print(reduce(add_tow_num, list_second))  # 100
print(reduce(fn, list_org))  # 123456
