#!/usr/bin/env python
# coding=utf-8
'''
Author: Len-xu
Date: 2021-02-21 20:43:31
LastEditTime: 2021-02-21 20:56:40
LastEditors: Do not edit
FilePath: \Python-Algorithm\设计模式\adapter.py
Description: 适配器模式
'''

from abc import ABCMeta, abstractclassmethod, abstractmethod


# 接口
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass
# A系统
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

# B系统
class ApplePay:
    def cost(self, money):
        print("苹果支付%d" % money)

class BankPay:
    def cost(self, money):
        print("银联支付%d" % money)

#现在有两个系统A和B,但是两个系统支付方法不统一，A系统是pay方法，B系统是cost方法，
#那么我们如何才能够让B系统合并到A系统中达到接口统一。

#类适配器：继承类
class NewBankPay(Payment, BankPay):
    def pay(self, money):
        self.cost(money)

class NewApplePay(Payment, ApplePay):
    def pay(self, money):
        self.cost(money)

#这样我们使用NewBankPay和NewApplePay就能够实现统一
p = NewApplePay()
p.pay(100)
#但是类适配器有个缺点就是：B系统有多少个这样的类，就需要创建多少个New继承类

#因此可以使用对象适配器 组合的方法解决
#组合的实现是将B系统中的类传入到PaymentAdapter类中，然后在里面调用。它只适用于几个类方法一致。
class PaymentAdapter(Payment):
    def __init__(self, payment) -> None:
        super().__init__()
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)

p = PaymentAdapter(ApplePay())
p.pay(100)