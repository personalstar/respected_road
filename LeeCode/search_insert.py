#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/21 5:29 下午
# @Author  : xin
# @Detail  : 寻找插入位置

# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 请必须使用时间复杂度为 O(log n) 的算法。

class Solution:
    def searchInsert(self, nums, target):
        # 初始化插入位置
        # 设置参数，top为高位，low为低位，mid为中间位，使用二分查找法
        top = len(nums) - 1
        low = 0
        mid = (top + low) // 2

        while low != mid:
            if target <= nums[mid]:
                top = mid - 1
            else:
                low = mid + 1
            mid = (top + low) // 2
        # loc = mid if target <= nums[low] else (mid + 1)
        if target <= nums[low]:
            loc = mid
        elif target > nums[top]:
            loc = top + 1
        else:
            loc = low + 1
        print(loc)


if __name__ == '__main__':
    # nums = []
    # nums.extend(input())
    # target = input()
    nums = [1, 3, 5, 6]
    target = 5
    sol = Solution()
    sol.searchInsert(nums, target)
