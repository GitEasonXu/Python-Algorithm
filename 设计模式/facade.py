#!/usr/bin/env python
# coding=utf-8
'''
Author: Len-xu
Date: 2021-02-22 08:10:43
LastEditTime: 2021-02-22 08:21:24
LastEditors: Do not edit
FilePath: \Python-Algorithm\设计模式\facade.py
Description: 外观模式
'''
from abc import ABCMeta, abstractclassmethod, abstractmethod

class Device(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass
    def stop(self):
        pass

class CPU(Device):
    def run(self):
        print("CPU开始运行")

    def stop(self):
        print("CPU停止工作")

class Disk(Device):
    def run(self):
        print("硬盘开始运行")

    def stop(self):
        print("硬盘停止工作")

class Memory(Device):
    def run(self):
        print("内存开始运行")

    def stop(self):
        print("内存停止工作")
# 外观：可以使用户不去查看底层模块，通过封装一个类(外观)直接帮用户创建好
# 外观感觉和建造者模式比较相似
class Computer:
    def __init__(self) -> None:
        self.cpu = CPU()
        self.disk = Disk()
        self.memory = Memory()
    
    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()
    
    def stop(self):
        self.disk.stop()
        self.memory.stop()
        self.cpu.stop()

computer = Computer()
computer.run()
computer.stop()