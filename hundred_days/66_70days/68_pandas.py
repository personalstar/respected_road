#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/23 9:57 上午
# @Author  : xin
# @Detail  : Series的应用（一维数据：系列）

import numpy as np
import pandas as pd

# 通过列表或数组创建Series对象
ser1 = pd.Series(data=[320, 180, 300, 405], index=['一季度', '二季度', '三季度', '四季度'])
print(ser1)

# 字典中的键就是数据的索引（标签），字典中的值就是数据
# ser2 = pd.Series({'一季度': 320, '二季度': 180, '三季度': 300, '四季度': 405})

# 使用整数索引，可以直接读取或修改；使用自定义index索引
print(ser1[0], ser1[1])  # 320 180
ser1[0] = 520
print(ser1[0])  # 520
print(ser1['一季度'])  # 520

# 切片操作，默认索引数字切片遵循左闭右开原则，index索引遵循则两边都包含在内
print(f'切片一，数字索引切片：\n{ser1[1:3]}')
print('切片二，index索引切片：\n{}'.format(ser1['二季度':'四季度']))

# 切片赋值
ser1[1:3] = 13, 14
print(ser1[1:3])

# 布尔索引
print(ser1[ser1 >= 100])
