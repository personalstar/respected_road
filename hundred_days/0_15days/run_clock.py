#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/3 4:09 下午
# @Author  : xin
# @Detail  : 实现一个时钟

import time


class Clock(object):
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def replay(self):
        return f'{self._hour}:{self._minute}:{self._second}'


def main():
    clock = Clock(23, 59, 55)
    while True:
        print(clock.replay())
        time.sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
