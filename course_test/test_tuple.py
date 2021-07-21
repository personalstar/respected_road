#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/21 4:03 下午
# @Author  : xin
# @Detail  : 元组课程练习

# 元组与列表不同之处：元组使用小括号()，列表使用中括号[]，其他操作基本一致

# 创建空元组
tup_null = ()
print(tup_null)

# 有小括号，用单引号；无小括号，用双引号；只包含一个元素时，需要加都好","，否则会被当做运算符
tup1 = ('a', 'b', 'c', 1, 2)
tup2 = "a", "b", "c", 1, 2
print(tup1, tup2)
tup3 = (50)
tup4 = (50,)
tup5 = "a"
tup6 = "a",
# 50不加逗号为int整型数，加逗号为元组；a不加逗号为str类型，加逗号为元组
print(type(tup3), type(tup4), type(tup5), type(tup6))

# 元组不支持修改元素
# tup1[1] = 'aaa'
# print(tup1)
