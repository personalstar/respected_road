#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/16 5:12 下午
# @Author  : xin
# @Detail  : 字符串联系


var1 = 'HELLO WORLD'
var2 = 'HARRY'

# var1的第一个字母
print(var1[0])

# var1的最后一个字母
print(var1[-1])

# var1第二个字母开始；第四个字母结束（第四个字母不算,[]中括号遵循左闭右开原则）
print(var1[1:3])

# var1一直到第五个字母（第五个字母不算,[]中括号遵循左闭右开原则）
print(var1[:4])

# var1第七个字母开始到结束
print(var1[7:])

# 字符串拼接
print(var1[:6] + var2)

# 重复输出字符串:*
print(var2 * 3)

# 包含运算符：in/  not in
if 'H' in var1:
    print('H 位于变量 var1 中')
else:
    print('H 不在变量 var1 中')

# 原始字符串：r/R,引号前加上r/R，则引号内容直接使用，没有转义特殊或者不能打印的字符
# \n 表示换行
print('\n')
print(r'\n')

# python原则上一行表示一个语句，不允许换行，可使用"\"进行换行，当有多行字符串时，可使用三个引号 """*******"""
string_a = """
    this is the first cow
    second
    select * from table
    where name = aaa
"""
print(string_a)

# 替换变量 / 使用表达式
name = 'harry'
print(f'hello {name}')
print(f'{1 + 3}')
print(f'{1 + 3 = }')

imf = {'name': 'harry', 'number': '15'}
print(f'{imf["name"] + imf["number"]}')

# 常用个函数
var3 = 'Begining'
print('大写：' + var3.upper())
print('小写：' + var3.lower())
print('大小写互换：' + var3.swapcase())
print('长度：%d' % len(var3))
# 下面的表达式报错，原因是引号内容为str类型，而len内容为int类型，所以报错
# len_var = len(var3)
# print('长度：' + len_var)
# 替换函数，参数一位原字符，参数二为替换字符，参数三为最高替换次数
var3_replace = var3.replace('i', 'a', 1)
print('替换字符：' + var3_replace)
