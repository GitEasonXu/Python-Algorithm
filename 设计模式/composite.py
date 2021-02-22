#!/usr/bin/env python
# coding=utf-8
'''
Author: Len-xu
Date: 2021-02-22 07:47:42
LastEditTime: 2021-02-22 08:04:49
LastEditors: Do not edit
FilePath: \Python-Algorithm\设计模式\composite.py
Description: 组合模式
'''
from abc import ABCMeta, abstractclassmethod, abstractmethod

#抽象组件
class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass

#叶子组件
class Point(Graphic):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "点(%s, %s)" % (self.x, self.y)

    def draw(self):
        print(self)

class Line(Graphic):
    def __init__(self, p1, p2) -> None:
        super().__init__()
        self.p1 = p1
        self.p2 = p2
    def __str__(self) -> str:
        return "线段[%s, %s]" % (self.p1, self.p2)

    def draw(self):
        print(self)
#复合组件
class Picture(Graphic):
    def __init__(self, iterable) -> None:
        self.children = []
        if hasattr(iterable, "__iter__"):
            for g in iterable:
                self.add(g)

    def add(self, graphic):
        self.children.append(graphic)

    def draw(self):
        print("=======复合图形========")
        for g in self.children:
            g.draw()
        print("=======复合图形========")


p1 = Point(1,2)
p2 = Point(3,4)
line1 = Line(p1, p2)
line2 = Line(Point(5,6), Point(7, 8))

picture1 = Picture([p1, p2, line1, line2])
picture2 = Picture([p1, p2, line1, line2])

pic = Picture([picture1, picture2])
pic.draw()