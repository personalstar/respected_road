#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/4 5:40 下午
# @Author  : xin
# @Detail  : property装饰器：getter / setter 方法

class Person(object):
    # __slots__限定当前类只能绑定_name , _age两个变量，
    __slots__ = ('_name', '_age', '_sex')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 — gatter方法
    @property
    def name(self):
        return self._name

    # 访问器 — gatter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age < 16:
            print(f'{self._name} 在玩飞行棋')
        else:
            print(f'{self._name} 在玩斗地主')


def main():
    person = Person('二狗子', 15)
    person.play()
    person.age = 30
    person.play()

    # __slots__限定能绑定sex，所以可以新增的sex属性
    person._sex = 'man'
    print(person._sex)

    # __slots__限定只能绑定name、age、sex，所以新增的school属性会报错；若没有限定函数，则可新增属性
    # person._school = 'sz'
    # print(person._school)
    # AttributeError: 'Person' object has no attribute '_school'


if __name__ == '__main__':
    main()
