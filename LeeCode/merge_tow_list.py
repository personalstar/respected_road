#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/22 11:32 上午
# @Author  : xin
# @Detail  : 合并两个有序列表

# 给你两个有序整数数组nums1 和 nums2，请你将 nums2 合并到nums1中，使 nums1 成为一个有序数组。
# 初始化nums1 和 nums2 的元素数量分别为m 和 n 。你可以假设nums1 的空间大小等于m + n，这样它就有足够的空间保存来自 nums2 的元素。

nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
nums2 = [1, 2, 2]
length1 = len(nums1)
length2 = len(nums2)
while length1 > 6:
    del nums1[length1 - 1]
    length1 -= 1
while length2 > 3:
    del nums1[length2 - 1]
    length2 -= 1
nums1.extend(nums2)
nums1.sort()
print(nums1)
