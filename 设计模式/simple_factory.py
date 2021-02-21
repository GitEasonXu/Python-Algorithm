#!/usr/bin/env python
# coding=utf-8
'''
Author: Len-xu
Date: 2021-02-21 11:30:29
LastEditTime: 2021-02-21 11:50:55
LastEditors: Do not edit
FilePath: \Python-Algorithm\设计模式\simple_factory.py
Description: 简单工厂模式
'''
from abc import ABCMeta, abstractclassmethod, abstractmethod
from typing import List

# 接口
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass
# 底层
class AliPay(Payment):
    def __init__(self, use_huabei=False) -> None:
        super().__init__()
        self.use_huabei = use_huabei
    def pay(self, money):
        if self.use_huabei:
            print("支付宝花呗支付%d" % money)
        else:
            print("支付宝余额支付%d" % money)

class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d" % money)

# 高层
def finish_pay(p, money):
    p.pay(100)

# 工厂类主要用来生产类的
class PaymentFactory:
    def create_payment(slef, class_name):
        if class_name == "alipay": # 这里通过if else语句可以实现不同支付类的实例化，
            return AliPay()        # 因为通常来说，类的实例化实现的参数也是不尽相同的，因此这样实现方便不同类的实例化
        elif class_name == "wechat":
            return WechatPay()
        elif class_name == "huabei":
            return AliPay(use_huabei=True)
        else:
            raise TypeError("No such class named %s" % class_name)

# 客户端
pf = PaymentFactory()
p = pf.create_payment("huabei") #对用户而言对象创建方法是一样的，用户不需要了解实现细节。
finish_pay(p, 100)

# 但是简单工厂模式一个缺点：从上面可以看出有多少分类就需要加一条elif语句