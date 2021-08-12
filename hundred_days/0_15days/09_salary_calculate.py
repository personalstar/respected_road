#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/11 11:02 上午
# @Author  : xin
# @Detail  : 不同职位员工工资计算

"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""

from abc import ABCMeta, abstractmethod


# 抽象类
class Employee(object, metaclass=ABCMeta):
    """员工"""

    def __init__(self, name):
        """
        初始化

        :param name: 姓名
        """
        self._name = name

    @property
    def name(self):
        return self._name

    # 抽象方法，子类必须复写
    @abstractmethod
    def get_salary(self):
        """
        获得月薪

        :return: 月薪
        """
        pass


class Manager(Employee):
    """经理"""

    def get_salary(self):
        return 15000


class Programmer(Employee):
    """程序猿"""

    def __init__(self, name, worktime=0):
        super().__init__(name)
        self._worktime = worktime

    @property
    def worktime(self):
        return self._worktime

    @worktime.setter
    def worktime(self, worktime):
        self._worktime = worktime if worktime > 0 else 0

    def get_salary(self):
        return 150 * self._worktime


class Saleman(Employee):
    """销售员"""

    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 1200 + self._sales * 0.05


def main():
    emps = [
        Manager('刘备'), Manager('曹操'), Manager('孙权'),
        Programmer('诸葛亮'), Programmer('司马懿'), Programmer('周瑜'),
        Saleman('关羽'), Saleman('许褚'), Saleman('吕蒙'),
    ]

    """
    .isinstance(object,classinfo)函数
    object为实例对象；classinfo可以是直接或间接类名、基本类型或者由它们组成的元组
    若object类型与classinfo相同则返回True，否则返回False
    """
    for emp in emps:
        if isinstance(emp, Programmer):
            emp.worktime = int(input(f'请输入程序员{emp.name}本月的工作时间（小时）：'))
        elif isinstance(emp, Saleman):
            emp.sales = int(input(f'请输入销售员{emp.name}本月的销售业绩:（元）'))
        print(f'{emp.name}本月的工资为：{emp.get_salary()}元')


if __name__ == '__main__':
    main()
