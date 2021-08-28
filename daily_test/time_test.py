#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/28 5:19 下午
# @Author  : xin
# @Detail  : 时间库函数

import arrow

# t = arrow.utcnow().format("YYYY-MM-DD" + ' 00:00:00')
t = arrow.now().format("YYYY-MM-DD" + ' 00:00:00')
print(t)
