#!/usr/bin/env python
# coding=utf-8
'''
Author: Len-xu
Date: 2021-02-23 08:29:56
LastEditTime: 2021-02-23 08:49:41
LastEditors: Do not edit
Description: 责任链模式
'''
from abc import ABCMeta, abstractclassmethod, abstractmethod

class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self, day):
        pass

class GeneralManager(Handler):
    def handle_leave(self, day):
        if day <= 10:
            print("总经理准假%d天" % day)
        else:
            print("你还是辞职吧")

class DepartmentManager(Handler):
    def __init__(self) -> None:
        self.next = GeneralManager()  # 对象以组合的方式形成一条处理链
    def handle_leave(self, day):
        if day <=5:
            print("部门经理准假%d天" % day)
        else:
            self.next.handle_leave(day)

class ProjectDirector(Handler):
    def __init__(self) -> None:
        self.next = DepartmentManager()  # 对象以组合的方式形成一条处理链

    def handle_leave(self, day):
        if day <= 3:
            print("项目经理准假%d天" % day)
        else:
            self.next.handle_leave(day)

p = ProjectDirector()

p.handle_leave(20)
