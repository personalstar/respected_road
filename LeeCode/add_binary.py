#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/22 5:13 下午
# @Author  : xin
# @Detail  : 二进制相加

# 给你两个二进制字符串，返回它们的和（用二进制表示）。
# 输入为 非空 字符串且只包含数字 1 和 0。

class Solution:
    def add_binary(self, a, b):
        x = int(a, 2)
        y = int(b, 2)
        list1 = list(str(bin(x + y)))
        del list1[1], list1[0]
        final = ''.join(str(s) for s in list1)
        return final


if __name__ == '__main__':
    a = "1010"
    b = "1011"
    solution = Solution()
    print(solution.add_binary(a, b))
