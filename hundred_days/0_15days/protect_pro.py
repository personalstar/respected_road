#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/3 5:40 下午
# @Author  : xin
# @Detail  : 类中各类函数以及方法

import time


class Test:
    # 构造函数
    def __init__(self, foo):
        self.name = 'name'
        self.__foo = foo
        self.age = 18

    # 私有函数
    def __bar(self):
        print(f'私有函数调用私有属性：{self.__foo}')
        print(f'私有函数打印：__bar')

    # 公有函数
    def to_bar(self):
        print('调用公有函数')
        print(f'通过公有函数调用私有函数：{self.__bar()}')

    # 静态函数
    @staticmethod
    def static_methon():
        print('静态函数')
        school = 'gzhu'


def main():
    test = Test('hello')

    # 可直接打印构造函数的属性
    print(test.name, test.age)  # name 18

    # 公有函数及函数内成员，可直接调用
    test.to_bar()

    # 调用私有属性  对象._类名__属性
    print(f'调用私有属性：{test._Test__foo}')

    # 调用静态函数
    test.static_methon()

    # test.__bar()
    # AttributeError: 'Test' object has no attribute '__bar'
    # print(test.__foo)
    # AttributeError: 'Test' object has no attribute '__foo'


if __name__ == '__main__':
    main()
