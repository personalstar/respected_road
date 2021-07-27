#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/19 5:23 下午
# @Author  : xin
# @Detail  : 列表课程练习

import sys


# 取值、切片与string类型一致
list1 = ['harry', 'potter', 'hello', 1988, 2020]
print('输出第二个元素：' + list1[1])
print(f'输出最后一个元素：{list1[-1]}')
print(f'输出列表长度：{len(list1)}')  # 列表长度

# 删除列表元素
del list1[-1]
print(f'删除最后一个元素：{list1}')

# 列表拼接
list1 += [1, 2, 3]
print(f'拼接列表：{list1}')

# 嵌套列表
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])

# 函数方法：
# 列表最大最小值
print(max(n))
print(min(n))

# 将元素加入列表结尾，无返回值，但会修改列表
list1.append('flower')
print(list1)
# append()表示将括号内列表作为一个元素插入list1列表
list1.append(['one', 'two', 'three'])
print(list1)
del list1[-1]
# extend()表示将括号内列表顺序插入到list列表
list1.extend(['one', 'two', 1])
print(list1)

# 统计某个元素出现的次数
print(list1.count(1))

# 从列表中找出某个值第一个匹配项的索引位置
print(list1.index('hello'))
# 移除列表中某个值的第一个匹配项
list1.remove('hello')
print(list1)

# 将元素插入列表中
list1.insert(2, 'insert_test')
print(list1)

# 移除列表中的元素（无参数值默认最后一个）
list1.pop(2)
print(list1)
list1.pop()
print(list1)

# # 反向列表
# list1_res = list1.reverse()
# print(list1_res)
list_res = list1[::-1]
print(f'反向列表：{list_res}')

# 对列表进行排序，False表示递增，True表示递减
list2 = ['acd', 'ba', 'gadf', 'f', 'zdada', 'qasdfc']
list2.sort(reverse=False)
print(f'直接对原列表进行排序：{list2}')
print(f'按字母顺序排序list2：{sorted(list2, reverse=False)}')
print(f'按key值排序list2：{sorted(list2, key=len)}')

# 复制列表
list_copy = list1.copy()
print(list_copy)

# 清空列表
list_copy.clear()
print(list_copy)

# 遍历元素索引和值
for index, elem in enumerate(list1):
    print(f'下标为{index}的元素是：{elem}')

# 生成式创建列表
list3 = [x for x in range(1, 10)]
print(f'生成式生成列表为：{list3}')
list4 = [x + y for x in 'ABCDE' for y in '1234']
print(f'生成式生成列表为：{list4}')
print(f'查看对象占用内存字节数：{sys.getsizeof(list4)}')
print(f'对象长度：{len(list4)}')
