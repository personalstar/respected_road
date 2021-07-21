#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/21 4:58 下午
# @Author  : xin
# @Detail  :


class menu():
    def menu_hsr(self):
        print("你好，你点的是红烧肉")

    def menu_sxwz(self):
        print("四喜丸子")

    def menu_ljcr(self):
        print("辣椒炒肉")

    def menu_all(self):
        food_name = input("选择菜品：")
        if food_name == '红烧肉':
            menu().menu_hsr()
        elif food_name == '四喜丸子':
            menu().menu_sxwz()
        elif food_name == '辣椒炒肉':
            menu().menu_ljcr()


if __name__ == '__main__':
    menu().menu_all()
