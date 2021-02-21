#!/usr/bin/env python
# coding=utf-8
'''
Author: Len-xu
Date: 2021-02-21 20:00:32
LastEditTime: 2021-02-21 20:27:13
LastEditors: Do not edit
FilePath: \Python-Algorithm\设计模式\singleton.py
Description: 单例模式
'''
from typing import Any


class Singleton:
    def __new__(cls, *args, **kwargs) -> Any:
        if not hasattr(cls, "_instance_"):
            cls._instance_ = super(Singleton, cls).__new__(cls)
        return cls._instance_

class MyClass(Singleton):
    def __init__(self, data) -> None:
        super().__init__()
        self.data = data
a = MyClass(10)
b = MyClass(20)

print(a.data)
print(b.data)

print(id(a), id(b))  #可以看出变量a和b指向同一个实例

