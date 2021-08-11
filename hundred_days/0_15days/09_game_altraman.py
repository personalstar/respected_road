#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/5 4:47 下午
# @Author  : xin
# @Detail  : 奥特曼打小怪兽

# 创建抽象对象导入包
from abc import ABCMeta, abstractmethod
# 随机函数
from random import randint, randrange


class Fighter(object, metaclass=ABCMeta):
    """战斗者"""

    # __slots__函数限定对象成员变量
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        """
        初始化方法

        :param name: 名字
        :param hp: 生命值
        """
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp

    @property
    # 活着返回True
    def alive(self):
        return self._hp > 0

    """抽象函数，不创建对象，只被继承重写，衍生多态"""

    @abstractmethod
    def attack(self, other):
        """
        攻击

        :param other: 被攻击的对象
        """
        pass


class Ultraman(Fighter):
    """奥特曼"""

    __slots__ = ('_name', '_hp', '_mp', '_max_mp')

    def __init__(self, name, hp, mp):
        """
        初始化

        :param name: 名字
        :param hp: 生命值
        :param mp: 魔法值
        """
        super().__init__(name, hp)
        self._mp = mp
        self._max_mp = mp

    # 普通攻击
    def attack(self, other):
        at = randint(15, 25)
        other.hp = (other.hp - at) if (other.hp - at) > 0 else 0
        # other.hp -= at
        print(f'{other.name}流失了{at}点生命值')
        if other.hp == 0:
            print(f'{other.name}已阵亡')

    def huge_attack(self, other):
        """
        究极必杀大招

        :param other: 被攻击对象
        :return: 成功释放大招返回True，否则返回False
        """
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp = (other.hp - injury) if (other.hp - injury) > 0 else 0
            # other.hp -= injury
            print(f'{other.name}流失了{injury}点生命值')
            if other.hp == 0:
                print(f'{other.name}已阵亡')
            return True
        else:
            print('奥特曼魔法值不够，无法触发大招，只能使用普通攻击')
            self.attack(other)
            return False

    def magic_attack(self, others):
        """
        小小法伤，群体AOE拉满

        :param others: 被攻击群体
        :return: 魔法使用成功返回True，失败返回False
        """
        if self._mp >= 20:
            self._mp -= 20
            print(f'{self.name}使用了魔法攻击')
            for other in others:
                if other.alive:
                    at = randint(10, 15)
                    other.hp = (other.hp - at) if (other.hp - at) > 0 else 0
                    # other.hp -= at
                    print(f'{other.name}流失了{at}点生命值')
                    if other.hp == 0:
                        print(f'{other.name}已阵亡')
            return True
        else:
            print('奥特曼魔法值不够，无法使用魔法攻击')
            return False

    def resume_mp(self):
        """恢复魔法值"""
        res_point = randint(1, 10)
        self._mp += res_point
        if self._mp >= self._max_mp:
            self._mp = self._max_mp
        return res_point

    def __str__(self):
        return f'----{self._name}奥特曼---- \n 生命值：{self._hp} \n 魔法值：{self._mp}'


class Monster(Fighter):
    """小怪兽"""

    __slots__ = ('_name', '_hp')

    def attack(self, other):
        at = randint(10, 20)
        other.hp = (other.hp - at) if (other.hp - at) > 0 else 0
        # other.hp -= at
        print(f'{other.name}流失了{at}点生命值')
        if other.hp == 0:
            print(f'{other.name}已阵亡')

    def __str__(self):
        return f'----{self._name}小怪兽---- \n 生命值：{self._hp}'


def is_any_alive(monsters):
    """判断有没有小怪兽活着"""
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False


def choose_alive_monster(monsters):
    """选择一直活着的小怪兽"""
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster


def display_info(ultraman, monsters):
    """显示奥特曼和小怪兽们的信息"""
    print(ultraman)
    for monster in monsters:
        print(f'{monster}')


def main():
    ul = Ultraman('啊君', 650, 200)
    m1 = Monster('古代怪兽', 500)
    m2 = Monster('磁力怪兽', 400)
    m3 = Monster('骷髅怪兽', 600)
    ms = [m1, m2, m3]
    fighting_rount = 1
    while ul.alive and is_any_alive(ms):
        print(f'===================第{fighting_rount}回合===================')
        m = choose_alive_monster(ms)
        skill = randint(1, 10)

        """60%的概率使用普通攻击,30%概率触发魔法攻击，10%概率触发大招"""
        if skill <= 6:
            print(f'{ul.name}使用了普通攻击打了{m.name}')
            ul.attack(m)
            print(f'{ul.name}恢复{ul.resume_mp()}点魔法值')
        elif skill <= 9:
            ul.magic_attack(ms)
            print(f'{ul.name}恢复{ul.resume_mp()}点魔法值')
        else:
            print(f'{ul.name}使用了大招攻击打了{m.name}')
            ul.huge_attack(m)
            print(f'{ul.name}恢复{ul.resume_mp()}点魔法值')

        """若小怪兽还活着，则反击"""
        if m.alive > 0:
            print(f'{m.name}回击了{ul.name}')
            m.attack(ul)

        """回合结束，显示战斗人员信息"""
        display_info(ul, ms)
        fighting_rount += 1

    print('===================战斗结束!===================')
    if ul.alive > 0:
        print('{}奥特曼获得胜利！'.format(ul.name))
    else:
        print('小怪兽们统治了地球！')


if __name__ == '__main__':
    main()
