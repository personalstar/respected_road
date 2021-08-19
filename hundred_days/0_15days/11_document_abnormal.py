#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/18 5:25 下午
# @Author  : xin
# @Detail  : 文件与异常

import time
from math import sqrt

"""
'r' 读取（默认）
'w' 写入（会先截断之前的内容）
'x' 写入，若文件已存在会产生异常
'a' 追加，将内容写入到已有文件的末尾
'b' 二进制模式
't' 文本模式（默认）
'+' 更新，既可以读又可以写
"""


def main():
    # 若文件不存在或无法打开，将引发异常导致程序崩溃
    # f = open('poem', 'r', encoding='utf-8')
    # print(f.read())
    # f.close()

    # 使用try与except增强程序的兼容性/健壮性
    f = None
    try:
        f = open('../data/poem', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定文件')
    except LookupError:
        print('指定了未知编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')

    # 无论程序正常与否，均会执行finally块代码
    finally:
        if f:
            f.close()

    print('-------------------------------')

    # 通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源
    try:
        with open('../data/poem', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定文件')
    except LookupError:
        print('指定了未知编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')

    print('-------------------------------')

    # 读取整个文件
    with open('../data/poem', 'r', encoding='utf-8') as f:
        print(f.read())

    # for-in循环按行读取
    with open('../data/poem', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
        print()

    # readlines()方法将文件按行读取到一个列表容器中
    with open('../data/poem') as f:
        lines = f.readlines()
    print(lines)


def is_prime(n):
    """判断n是否为素数"""
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False


def main2():
    filenames = ('../data/test_1.text', '../data/text_2.text', '../data/text_3.text')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时出错')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成！')


def photo_copy():
    try:
        with open('../data/17.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open('../data/17_paste.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定文件无法打开')
    except IOError as e:
        print('读写文件时出现错误')
    print('程序试行结束。')


if __name__ == '__main__':
    # main()
    # main2()
    photo_copy()
