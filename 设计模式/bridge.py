#!/usr/bin/env python
# coding=utf-8
'''
Author: Len-xu
Date: 2021-02-21 21:05:59
LastEditTime: 2021-02-21 22:13:28
LastEditors: Do not edit
FilePath: \Python-Algorithm\设计模式\bridge.py
Description: 桥模式
'''
#首先我们定义一个Shape基类
class Shape:
    pass
#然后创建三个线  三角  圆的类
class Line(Shape):
    pass
class Rectangle(Shape):
    pass
class Circle(Shape):
    pass
#形状总有颜色，那么现在创建一个不同颜色的线
class RedLine(Line):
    pass
class GreenLine(Line):
    pass
#此时你会发现，颜色和形状两个维度是耦合在一起的，需要多少颜色的线你就需要创建多少个类，这显然很不方便。
#解决办法就是将Shape和Color分开
from abc import ABCMeta, abstractmethod
class Shape(metaclass=ABCMeta):
    def __init__(self, color) -> None:
        self.color = color
    @abstractmethod
    def draw(self):
        pass

class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        pass

class Rectangle(Shape):
    name = "长方形"
    def draw(self):
        self.color.paint(self)

class Circle(Shape):
    name = "圆形"
    def draw(self):
        self.color.paint(self)

class Red(Color):
    def paint(self, shape):
        print("绘制%s%s"%(shape.name, "红色"))

class Green(Color):
    def paint(self, shape):
        print("绘制%s%s"%(shape.name, "绿色"))

#将颜色和形状维度分离后，增加颜色或形状，只需要实现对应的类就可以了不用添加很多代码
color = Red()
shape = Circle(color)
shape.draw()