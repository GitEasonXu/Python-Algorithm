#!/usr/bin/env python
# coding=utf-8
'''
Author: Len-xu
Date: 2021-02-21 11:56:17
LastEditTime: 2021-02-21 13:14:55
LastEditors: Do not edit
FilePath: \Python-Algorithm\设计模式\factory_method.py
Description: 
'''
#简单工厂模式是将类的实例化写到一个类里面
#工厂模式则是将其拆分开来，每个工厂函数只包含一个类的实例化
from abc import ABCMeta, abstractmethod

# 抽象产品角色 
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass
# 具体产品角色
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

# 抽象工厂角色
class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass

# 具体工厂角色

class AliPaymentFactory(PaymentFactory):
    def create_payment(self):
        return AliPay()

class WechatPaymentFactory(PaymentFactory):
    def create_payment(self):
        return WechatPay()

class HuabeiPaymentFactory(PaymentFactory):
    def create_payment(self):
        return AliPay(use_huabei=True)


pf = HuabeiPaymentFactory()
p = pf.create_payment()
p.pay(1000)

#相比较简单工厂模式的优点：增加新的具体产品角色时，只需要再增加一个具体工厂角色即可
