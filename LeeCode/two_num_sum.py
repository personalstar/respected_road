#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/21 2:16 下午
# @Author  : xin
# @Detail  : 两数相加

# 给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
# 你可以假设除了数字 0 之外，这两个数都不会以 0开头。

# 传值，挨个位数相加

class Solution:
    def addTwoNumbers(self, list_1, list_2):
        num_1, num_2 = len(list_1), len(list_2)
        final_num = num_1 if num_1 >= num_2 else num_2
        # if num_1 >= num_2:
        #     final_num = num_1
        # else:
        #     final_num = num_2
        list_num = []
        carry_num = 0  # 过度参数，有进位则为1

        for x in range(final_num):
            if x <= final_num:
                if x >= num_1:
                    list_1.append(0)
                if x >= num_2:
                    list_2.append(0)

                if list_1[x] + list_2[x] + carry_num >= 10:
                    list_num.append((list_1[x] + list_2[x] + carry_num) % 10)
                    carry_num = 1
                else:
                    list_num.append(list_1[x] + list_2[x] + carry_num)
                    carry_num = 0
            else:
                if carry_num == 1:
                    list_num.append(1)
        print(list_num)


if __name__ == '__main__':
    list_A = [9, 9, 9, 9, 9, 9, 9]
    list_B = [9, 9, 9, 9]
    solution = Solution()
    solution.addTwoNumbers(list_A, list_B)
