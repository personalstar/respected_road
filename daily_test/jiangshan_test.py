#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/13 12:40 δΈε
# @Author  : xin
# @Detail  :

class Xiaoming():

    def __init__(self):
        self.first_name = "ζ"
        self.last_name = "ε°"

    def full_name(self):
        return self.last_name + self.first_name


if __name__ == '__main__':
    stu1 = Xiaoming()
    print(stu1.full_name())
