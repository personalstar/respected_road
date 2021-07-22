#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/22 2:59 下午
# @Author  : xin
# @Detail  : 加一

# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。

class Solution:
    # 手动实现
    def plus_one_1(self, digits):
        x = len(digits)
        carry = 0

        if digits[x - 1] + 1 == 10:
            while x - 1 >= 0:
                if digits[x - 1] + 1 == 10:
                    digits[x - 1] = 0
                    carry = 1
                    x -= 1
                else:
                    digits[x - 1] += 1
                    carry = 0
                    break
            if carry == 1:
                digits.insert(0, 1)
            else:
                pass
        else:
            digits[x - 1] += 1
        return digits

    # 利用自带函数实现
    def plus_one_2(self, digits):
        n = len(digits) - 1
        num = 0
        for i in digits:
            if n == -1:
                break
            else:
                num += i * (10 ** n)
                n -= 1
        num += 1
        final = list(str(num))
        return list(map(int, final))


if __name__ == '__main__':
    digits = [8, 9, 9, 9]
    solution = Solution()
    digits = solution.plus_one_2(digits)
    print(digits)
