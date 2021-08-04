#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/3 3:23 下午
# @Author  : xin
# @Detail  : 变量作用域解析


def foo():
    tall = 180  # 此处的tall与全局变量的tall并非同一个变量，仅同名
    print(f'局部变量tall = {tall}')

def foo_glo():
    # global定义为全局变量，若有该全局变量，即变量等同，否则创建一个全局变量
    # 此时修改变量，全局变量
    global tall
    tall = 200
    print(f'局部定义全局变量tall = {tall}')


if __name__ == '__main__':
    # 定义全局变量，初始化为0
    tall = 0

    foo()
    print(f'此处为全局变量tall = {tall}')
    foo_glo()
    print(f'此处为全局变量tall = {tall}')
