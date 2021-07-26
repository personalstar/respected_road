#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/26 2:23 下午
# @Author  : xin
# @Detail  : 猜数字

import random


class Solution:
    # 生成随机数
    def random_num(self):
        x = random.randint(1, 100)
        return x

    def guest_func(self, num):
        x = int(num)
        count = 0

        while True:
            inp_num = int(input('请输入所猜想的数字：'))
            count += 1
            if inp_num > x:
                print('小一点')
            elif inp_num < x:
                print('大一点')
            else:
                print('答对了')
                print('一共猜了', count, '次')
                print('随机生成的数字为:', num)
                break


if __name__ == '__main__':
    sol = Solution()
    sol.guest_func(sol.random_num())
