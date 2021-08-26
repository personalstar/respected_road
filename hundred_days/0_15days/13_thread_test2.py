#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/25 2:54 下午
# @Author  : xin
# @Detail  :

from time import sleep
from threading import Thread, Lock


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money, num):
        # 先获取锁才能执行后续的代码
        if self._lock.acquire():
            print(f'线程{num}获取锁')
            try:
                new_balance = self._balance + money
                sleep(0.01)
                self._balance = new_balance
            finally:
                # 在finally中执行释放锁的操作保证正常异常锁都能释放
                self._lock.release()
                print(f'释放锁，线程{num}结束')

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
    for _ in range(10):
        t = AddMoneyThread(account, 1, _+1)
        threads.append(t)
        t.start()
        print(f'线程{_ + 1}开始')
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()
