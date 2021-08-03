#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/27 10:36 上午
# @Author  : xin
# @Detail  :

"""
传参可设置默认值
可设置可变参数
"""


# 同名函数，与one_test同名，供module_test调用
def foo():
    print('goodbye,world')


# 三数相加，可设置默认值，传参可少传则为默认值，也可不按顺序传参
def add(a=0, b=0, c=0):
    return a + b + c


# 参数名前加 * ，表示可变参数
def add_total(*args):
    total = 0
    for val in args:
        total += val
    return total

if __name__ == '__main__':
    # 不传参，皆为默认值；顺序传参，缺失为默认值；标名参数key可不按顺序传参
    print(add())
    print(add(1))
    print(add(1, 2))
    print(add(1, 2, 3))
    print(add(b=5, c=6, a=7))

    # 调用函数带可变参数，可传0个或多个参数
    print(add_total())
    print(add_total(1))
    print(add_total(1, 2))
    print(add_total(1, 2, 3))
    print(add_total(1, 2, 3, 4, 5))
