#!/usr/bin/env python
# coding=utf-8
'''
Author: Len-xu
Date: 2021-02-21 13:27:40
LastEditTime: 2021-02-21 14:04:07
LastEditors: Do not edit
FilePath: \Python-Algorithm\设计模式\abstract_factory.py
Description: 
'''
from abc import ABCMeta, abstractmethod

#抽象产品角色
class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass

class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass

class OS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass

#抽象工厂角色
class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass
    @abstractmethod
    def make_cpu(self):
        pass
    @abstractmethod
    def make_os(self):
        pass

#具体产品角色
class SmallShell(PhoneShell):
    def show_shell(self):
        print("小手机壳")

class BigShell(PhoneShell):
    def show_shell(self):
        print("大手机壳")

class SnapDragonCPU(CPU):
    def show_cpu(self):
        print("高通骁龙CPU")

class MediaTekCPU(CPU):
    def show_cpu(self):
        print("联发科CPU")

class AppleCPU(CPU):
    def show_cpu(self):
        print("苹果CPU")

class Android(OS):
    def show_os(self):
        print("Android系统")

class IOS(OS):
    def show_os(self):
        print("IOS系统")

# 具体工厂
class MiFactory(PhoneFactory):
    def make_shell(self):
        return BigShell()
    
    def make_cpu(self):
        return SnapDragonCPU()
    
    def make_os(self):
        return Android()


class AppleFactory(PhoneFactory):
    def make_shell(self):
        return SmallShell()
    
    def make_cpu(self):
        return AppleCPU()

    def make_os(self):
        return IOS()

# 客户端
class Phone:
    def __init__(self, shell, cpu, os) -> None:
        self.shell = shell
        self.cpu = cpu
        self.os = os
    
    def show_info(self):
        self.shell.show_shell()
        self.cpu.show_cpu()
        self.os.show_os()

def make_phone(phone_factory):
    shell = phone_factory.make_shell()
    cpu = phone_factory.make_cpu()
    os = phone_factory.make_os()
    return Phone(shell, cpu, os)

    
phone = make_phone(AppleFactory())
phone.show_info()