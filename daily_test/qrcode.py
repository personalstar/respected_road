#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/22 3:34 下午
# @Author  : xin
# @Detail  : 二维码生成

from MyQR import myqr
import random

# ran_num = random.randrange(0, 3)
# print(ran_num)
data = [
    'first',
    'second',
    'third'
]

myqr.run(words=data[random.randrange(0, 3)], save_name='test1.jpg', colorized=False)
