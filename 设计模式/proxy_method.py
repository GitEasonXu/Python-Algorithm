#!/usr/bin/env python
# coding=utf-8
'''
Author: Len-xu
Date: 2021-02-23 07:52:21
LastEditTime: 2021-02-23 08:21:47
LastEditors: Do not edit
Description: 代理模式
'''

from abc import ABCMeta, abstractclassmethod, abstractmethod

class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass

class RealSubject(Subject):
    def __init__(self, filename) -> None:
        self.filename = filename
        with open(self.filename, "r", encoding='utf-8') as f:
            self.content = f.read()
            #self.content = f.readlines()

    def get_content(self):
        return self.content

    def set_content(self, content):
        with open(self.filename, "w", encoding='utf-8') as f:
            f.write(content) 

#使用这种模式会在创建实例的时候就将文件内容加载到内存中
file = RealSubject("./test.txt")
print(file.get_content())

class VirtualProxy(Subject):
    def __init__(self, filename) -> None:
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)  #组合的方式
        return self.subj.get_content()

    def set_content(self, content):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        self.subj.set_content(content)

#使用虚代理模式，在实例化对象时并没有将内容加载至内存中，只是在调用使用时才加载。
file = VirtualProxy("./test.txt")
file.get_content()

class ProtectedProxy(RealSubject):
    def __init__(self, filename) -> None:
        super().__init__(filename)
    def set_content(self, content):
        raise PermissionError("没有写入权限")

file = ProtectedProxy("test.txt")
file.set_content("你好！")