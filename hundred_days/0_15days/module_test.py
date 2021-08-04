#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/27 11:36 上午
# @Author  : xin
# @Detail  : 模块练习

# 此时后者调用会覆盖前者调用
# from one_test import foo
# from two_test import foo


import one_test as m1
import two_test as m2

# 重命名模块中函数，可直接调用
from one_test import foo as m3

if __name__ == '__main__':
    m1.foo()
    m2.foo()
    m3()
