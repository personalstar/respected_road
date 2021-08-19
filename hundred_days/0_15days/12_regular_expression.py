#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/19 3:01 下午
# @Author  : xin
# @Detail  : 正则表达式

import re


def judge_QQ():
    """
    re.match(obj1,obj2)
    obj1 : 正则表达式字符串或者正则表达式对象
    obj2 : 与正则表达式做匹配的对象
    :return:
    """
    username = input('输入用户名：')
    m1 = r'^[0-9a-zA-Z_]{6,12}$'
    miss1 = 0
    while not re.match(m1, username):
        username = input('输入有效用户名：')
        miss1 += 1
        if miss1 == 5:
            username = None
            break

    if username is not None:
        qq = input('输入QQ号：')
        m2 = r'^[1-9]\d{4,11}$'

        miss2 = -0
        while not re.match(m2, qq):
            qq = input('输入有效QQ号：')
            miss2 += 1
            if miss2 == 5:
                qq = None
                break

    if username and qq:
        print('输入信息有效')
    else:
        print('输入信息无效')


def find_phone():
    # 创建正则表达式对象，保证手机号为11位且前后无其他数字
    # (?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D) 精准匹配国内手机号
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = """
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    """

    # 查找所有匹配并保存到列表中
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('-------------强行分割线---------------')

    # 通过迭代器取出匹配对象并获得匹配内容
    for temp in pattern.finditer(sentence):
        print(temp)
        print(temp.group())
    print('-------------强行分割线---------------')

    # 通过search函数指定搜索位置找出所有匹配
    # end()返回结束匹配的位置
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())
        print(m)


def replace():
    sentence = '我操你大爷，你他妈会不会玩，傻逼'
    sentence2 = '野区栓条狗放出来都比你凶'

    friendly = '[操草艹]|傻[逼比币叉缺屌叼吊]|煞笔|沙比|他妈'

    sen_friendly = re.sub(friendly, '**', sentence, flags=re.IGNORECASE)
    print(sen_friendly)

    sen2_friendly = re.sub(friendly, '**', sentence2, flags=re.IGNORECASE)
    print(sen2_friendly)


def devide():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。, .]', poem)
    print(sentence_list)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)


if __name__ == '__main__':
    # judge_QQ()
    # find_phone()
    # replace()
    devide()
