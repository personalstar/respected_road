#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/26 11:35 上午
# @Author  : xin
# @Detail  : 小函数合集

# 九九乘法表 判断素数 求公约数/公倍数 打印三角形

import math
import random


# 生成随机数
def randow_num(n, m):
    return random.randint(n, m)


# 九九乘法表
def multiplcation_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            # print(i, 'x', j, '=', i * j, end='\t')
            print('%dx%d=%d' % (i, j, i * j), end='\t')
        print('')


# 判断输入的正整数是否为素数
def prime_number():
    num = int(input('请输入一个正整数：'))
    sqr = int(math.sqrt(num))
    check = False
    for i in range(2, sqr + 1):
        if num % i == 0:
            print('%d不是素数' % num)
            check = True
            break
        else:
            continue
    if check == False:
        print('%d是素数' % num)


# 输入两个正整数，求最大公约数和最小公倍数
def func_number(x, y):
    if x > y:
        x, y = y, x
    for i in range(y, 0, -1):
        if x % i == 0 and y % i == 0:
            print('最大公约数为：%d' % i)
            print('最小公倍数为：%d' % (x * y / i))
            break


# 打印三角形
def triangle():
    n = int(input('输入打印行数：'))
    for i in range(n):
        for j in range(i + 1):
            print('*', end='')
        print('')

    for i in range(n + 1):
        print(' ' * (n - i), '*' * i, end='')
        print('')

    for i in range(n):
        n_num = n - i
        s_num = i * 2 + 1
        print(' ' * n_num, '*' * s_num)


# 没过拉斯维加斯的桌上赌博游戏——CRAPS赌博游戏
def craps_game():
    first_time_num = randow_num(2, 12)
    if first_time_num == 2 or first_time_num == 3 or first_time_num == 12:
        print('庄家胜，点数为：', first_time_num)
    elif first_time_num == 7 or first_time_num == 11:
        print('玩家胜，点数为：', first_time_num)
    else:
        print('第一轮点数为：', first_time_num)
        while True:
            n_num = randow_num(2, 12)
            if n_num == 7:
                print('庄家胜，点数为：', n_num)
                break
            elif n_num == first_time_num:
                print('玩家胜，点数为：', n_num)
                break


# multiplcation_table()
# prime_number()
# func_number(15, 25)
# triangle()
craps_game()
