#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/17 4:03 下午
# @Author  : xin
# @Detail  : 数字课程练习

# 数学函数应用：https://www.runoob.com/python3/python3-number.html

# 二进制、八进制、十六进制 转 十进制
# 十六进制转十进制
num_a = 0xA0F
print(num_a)
print(int("A0F", 16))

# 八进制转十进制
num_b = 0o37
print(num_b)
print(int("37", 8))

# 二进制转十进制
num_c = 0b101
print(num_c)
print(int("101", 2))

# 十进制 转 二进制 、 八进制 、 十六进制
print(bin(20))
print(oct(20))
print(hex(20))

# 类型转换
x = 5
y = 5.5
print(int(y))
print(float(x))

# 涉及除法的结果为float型
print(8 / 4)

# 向下取整,结果类型与除数、被除数相关
print(10 // 3, '\t', 10 // 3.0, '\t', 10.0 // 3)

# 求余
print(8 % 3)

# 幂运算： **
print(5 ** 2)
print(pow(5, 2))
