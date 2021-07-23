#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/23 3:19 下午
# @Author  : xin
# @Detail  : 最大盈利值

class Solution:
    def max_profit(self, prices):
        # 净赚
        profit = 0
        # 最低点下标
        buy_point = 0
        # 最高点下标
        sale_point = 0
        length = len(prices)

        for i in range(1, length):
            if prices[sale_point] < prices[i]:
                prices[sale_point] = prices[i]
                sale_point = buy_point + 1
            elif prices[buy_point] >= prices[i]:
                prices[buy_point] = prices[i]
                buy_point += 1
            elif prices[buy_point] < prices[i] <= prices[sale_point] and sale_point > buy_point:
                profit += (prices[sale_point] - prices[buy_point])
                prices[buy_point] = prices[i]
                buy_point = sale_point + 1
            elif prices[buy_point] < prices[i] <= prices[sale_point] and sale_point < buy_point:
                sale_point = buy_point + 1
                prices[sale_point] = prices[i]

        return profit


if __name__ == '__main__':
    prices = [1, 2, 3, 4, 5]
    solution = Solution()
    print(solution.max_profit(prices))
