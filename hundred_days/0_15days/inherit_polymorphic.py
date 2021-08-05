#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/5 2:55 下午
# @Author  : xin
# @Detail  : 继承与多态

# 创建父类
class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # 修改器
    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age

    def playing(self):
        if self._age > 18:
            print(f'{self._name} is watching game')
        else:
            print(f'{self._name} is watching cartoon')


# 创建子类：学生类，继承父类
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    # 创建相同函数，改变实现方式，即为多态，子类可自行定义不同于父类的函数实现方式
    def playing(self):
        if self._age > 15:
            print(f'{self._name}, who is in {self._grade}, is playing game')
        else:
            print(f'{self._name}, who is in {self._grade}, is studying')

    # 新定义全新函数
    def watching(self):
        print(f'{self._name} is watching marvel')


# 创建子类：教师类，继承父类
class Teacher(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self._course = course

    @property
    def course(self):
        return self._course

    @course.setter
    def song(self, course):
        self._course = course

    def listening(self, song):
        print(f'{self._name} is listening {song}')


def main():
    stu = Student('小明', 19, '大一')
    # 重写父类对象函数playing
    stu.playing()
    # 新增子类对象函数watching
    stu.watching()

    tea = Teacher('小文', 25, 'math')
    # 沿用父类对象函数playing
    tea.playing()
    # 新增子类对象函数listening
    tea.listening('dangerous')


if __name__ == '__main__':
    main()
