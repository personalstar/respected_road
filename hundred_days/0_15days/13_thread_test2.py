#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/25 2:54 下午
# @Author  : xin
# @Detail  : 多线程加锁

"""
10个用户同时想同一个账户汇钱，该账户为共享变量，被多个线程竞争使用，称之为"临界资源"
使用临界资源时，加锁解锁来获取资源操作权限，才能使得关键资源操作步骤不会被覆盖，能一一执行
"""

import time
import threadpool

from time import sleep
from threading import Thread, Lock


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 先获取锁才能执行后续的代码
        if self._lock.acquire():
            # print(f'线程{num}获取锁')
            try:
                new_balance = self._balance + money
                sleep(0.01)
                self._balance = new_balance
            finally:
                # 在finally中执行释放锁的操作保证正常异常锁都能释放
                self._lock.release()
                # print(f'释放锁，线程{num}结束')

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money, num):
        super().__init__()
        self._account = account
        self._money = money
        self._num = num

    def run(self):
        self._account.deposit(self._money, self._num)


def main():
    account = Account()
    threads = []
    start_time = time.time()

    """循环增加线程"""
    # 总共耗费了12.30秒.
    # for _ in range(1000):
    #     t = AddMoneyThread(account, 1, _ + 1)
    #     threads.append(t)
    #     t.start()
    #     print(f'线程{_ + 1}开始')
    # for t in threads:
    #     t.join()

    """单线程操作"""
    # for _ in range(1000):
    #     account.deposit(1, _ + 1)

    """线程池"""
    temp = []
    for i in range(1000):
        temp.append(i)

    thread_num = 4
    pool = threadpool.ThreadPool(thread_num)
    thread_requests = threadpool.makeRequests(account.deposit, temp)
    [pool.putRequest(req) for req in thread_requests]
    pool.wait()

    end_time = time.time()
    print('总共耗费了%.2f秒.' % (end_time - start_time))
    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()
