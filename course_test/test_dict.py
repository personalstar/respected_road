#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/30 4:56 下午
# @Author  : xin
# @Detail  : 字典课程练习

# 字典是可变容器模型，可储存任意类型对象
# 每个键值对格式： d = {key1:value2 , key2:value2}
# 大括号 {} 包起来，键值之间用冒号 : 连接，键值对之间用逗号 , 隔开

# 创建字典并输出
dict1 = {'name': 'fly', 'age': 20, 'sex': 'man'}
print(dict1['name'])  # fly
print(dict1['age'])  # 20

# 字典增删改
dict1['age'] = 25  # 修改age为25
dict1['company'] = 'cass'  # 增加键值对 'company':'cass'
del dict1['sex']  # 删除键值对 sex
print(dict1)
# {'name': 'fly', 'age': 25, 'company': 'cass'}

# 清空字典
dict1.clear()
print(dict1)  # dict1={}

# 删除字典
del dict1

# 同一个键仅允许出现一次，若出现两次，则第一次的赋值将被第二次覆盖
dict1 = {'name': 'ming', 'name': 'hong'}
print(dict1)  # {'name':'hong'}
print(dict1['name'])  # hong

# 计算字典键的总数以及类型
print(len(dict1))  # 1
print(type(dict1))  # <class 'dict'>

# .fromkeys(seq,value) 将序列seq作为字典的key，value为统一默认值
seq = ('name', 'age', 'sex')
dict2 = dict1.fromkeys(seq, 20)
print(dict2)  # {'name': 20, 'age': 20, 'sex': 20}

# .items() 以列表返回可视对象；.keys()返回key值
print(f'dict2的列表形式可视对象返回为：{dict2.items()}')  # dict_items([('name', 20), ('age', 20), ('sex', 20)])
print(f'dict2的key值可视对象为：{dict2.keys()}')  # dict_keys(['name', 'age', 'sex'])
print(f'dict2的value值可视对象为：{dict2.values()}')  # dict_values([20, 20, 20])

# .setdefault() 返回字典中对应的值，若没有该键，则返回默认值，并在字典新增该键并将默认值作为value赋予
print(dict1.setdefault('name', 'six'))
print(dict1.setdefault('class', 'six'))
print(dict1)

# .updata()将括号内的字典更新好.号前的字典里；有键值对则更新覆盖，无键值对则新增
# dict1={'name': 'hong', 'class': 'six'} dict2={'name': 20, 'age': 20, 'sex': 20}
dict1.update(dict2)
print(dict1)

# 删除键值，有则删除并返回删除的value；无则需要默认值，返回默认值，否则报错
pop_obj = dict1.pop('name')  # 删除name对应的键值对
pop_obj_1 = dict1.pop('school', 'none')  # 删除school对应的键值对，没有school则返回默认值none
print(pop_obj, pop_obj_1)
print(dict1)

# .popitem()删除最后一对键值对并返回键值对
popitem_1 = dict1.popitem()
print(popitem_1)
print(dict1)
