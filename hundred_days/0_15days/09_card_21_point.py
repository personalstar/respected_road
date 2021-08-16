#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/13 11:27 上午
# @Author  : xin
# @Detail  : 卡牌游戏-21点

import random
from abc import ABCMeta, abstractmethod, ABC


class Card(object):
    """一张牌"""

    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def suite(self):
        return self._suite

    @property
    def face(self):
        return self._face

    """
        当自定义了__str__()函数时，若使用print输出对象，则会从这个方法中return数据
        __str__()需要返回一个字符串，当做对这个对象的描写
    """

    def __str__(self):
        if self._face == 1:
            self._face = 'A'
        elif self._face == 11:
            self._face = 'J'
        elif self._face == 12:
            self._face = 'Q'
        elif self._face == 13:
            self._face = 'K'
        else:
            self._face = str(self._face)

        return f'{self._suite}{self._face}'

    """
        直接print输出某个实例化类对象时，看到的信息"类名 + object at + 内存地址"
        我们可以通过自定义__repr__()函数使得输出我们想要的信息
    """

    def __repr__(self):
        return self.__str__()


class Poker(object):
    """一副牌"""

    def __init__(self):
        self._cards = [Card(suite, face)
                       for suite in '♠♥♣♦'
                       for face in range(1, 14)]
        self._current = 0

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        """洗牌（随机乱序），random.shuffle()：将元素随机排序"""
        self._current = 0
        random.shuffle(self._cards)

    @property
    def next(self):
        """发牌"""
        card = self._cards[self._current]
        self._current += 1
        return card

    def has_next(self):
        """判断是否还有牌"""
        return self._current < len(self._cards)


class Rule(object, metaclass=ABCMeta):
    def __init__(self):
        self._winner = []

    @abstractmethod
    def rule(self, players):
        """
        卡牌规则

        :return:返回获胜玩家
        """
        pass


class point_21(Rule):
    def __init__(self):
        super().__init__()
        self._max_point = 0
        self._change_point = 0

    @property
    def max_point(self):
        return self._max_point

    @property
    def change_point(self):
        return self._change_point

    @max_point.setter
    def max_point(self, max_point):
        self._max_point = max_point

    @change_point.setter
    def change_point(self, change_point):
        self._change_point = change_point

    def rule(self, players):
        for player in players:
            self._change_point = 0
            for card in player.cards_on_hand:
                if card.face in ['J', 'Q', 'K']:
                    self._change_point += 10
                elif card.face != 'A':
                    self._change_point += int(card.face)
                else:
                    self._change_point += 11
                    if self._change_point > 21:
                        self._change_point -= 10
            print(f'{player.name}得分为：{self._change_point}')
            if self._max_point < self._change_point <= 21 and len(self._winner) == 0:
                self._winner.append(player.name)
                self._max_point = self._change_point
            elif self._max_point == self._change_point <= 21:
                self._winner.append(player.name)
            elif self._max_point < self._change_point <= 21:
                self._winner.clear()
                self._winner.append(player.name)
                self._max_point = self._change_point
            else:
                pass

        if len(self._winner) == 0:
            self._winner.append('None')

        return self._winner


class Players(object):
    """玩家"""

    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []

    @property
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    def get(self, card):
        """摸牌"""
        self._cards_on_hand.append(card)

    def arrange(self, card_key):
        """整理手上的牌"""
        self._cards_on_hand.sort(key=card_key, reverse=True)


def get_key(card):
    return card.face, card.suite


def main():
    p = Poker()
    p.shuffle()
    players = [Players('西科'), Players('东艾'), Players('南卡'), Players('北麦')]

    # 发牌，每人三张
    for _ in range(3):
        for player in players:
            player.get(p.next)

    for player in players:
        print(f'{player.name}:')
        player.arrange(get_key)
        print(player.cards_on_hand)

    print('============game over===========')
    game_1 = point_21()
    print(f'{game_1.rule(players)} is the winner')


if __name__ == '__main__':
    main()
