#!/usr/bin/env python
# coding=utf-8
'''
Author: Len-xu
Date: 2021-02-21 09:45:39
LastEditTime: 2021-02-21 11:23:30
LastEditors: Do not edit
FilePath: \Python-Algorithm\设计模式\interface.py
Description: 
'''
class AliPay:
    def pay(self, money):
        print("支付宝支付%d" % money)

class WechatPay:
    def pay(self, money):
        print("微信支付%d" % money)

def finish_pay(p, money):
    p.pay(100) 
#这里由于AliPay和WechatPay对应的pay方法一样，所以方便调用。但是如果实现方法不一样那么就不是很便利了，可能
#需要通过if else isinstance判断来跳转使用。

p = AliPay()
p = WechatPay()
finish_pay(p, 1000)

#通过上面分析完之后，我们发现了统一接口的重要性，那么怎么约束方法的统一性呢？
#这就使用到了接口，接口定义每种方法的抽象样子，然后子类继承必须严格按照要求实现。
class Payment:
    def pay(self, money):
        raise NotImplementedError #要求继承它的类必须实现该方法

from abc import ABCMeta, abstractclassmethod, abstractmethod
from typing import List
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

class AliPay(Payment):
    def pay(self, money):
        print("支付宝支付%d" % money)

class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d" % money)

def finish_pay(p, money):
    p.pay(100) 
p = AliPay()
finish_pay(p, 1000)

# 里氏替换原则：子类方法和对应父类方法接收参数应该一直，并且返回对象一样。
class User:
    def show_name(self):
        return "普通用户"

class VIPUser(User):
    def show_name(self):
        return "VIP用户"

# 依赖倒置原则
# 已支付为例，底层代码就是不同的支付类，高层代码就是支付显示界面
# 第一思考：高层需要调用底层什么东西, 高层需要调用登录和付款方法，因此定义一个抽象类(接口)，里面定义好每个方法。
# 定义好接口后，项目经理就可以指派任务，每个人实现不同的支付类(底层代码)
# 接口
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

    def login(self, user_name:str):
        pass
# 底层代码，底层代码按照接口实现所需求的支付类
class AliPay(Payment):
    def pay(self, money):
        print("支付宝支付%d" % money)
    def login(self, user_name:str):
        #通过用户名来完成支付宝登录逻辑，登录成功返回True否则返回False
        return True

class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d" % money)
    def login(self, user_name:str):
        #通过用户名来完成微信登录逻辑，登录成功返回True否则返回False
        return True

# 高层模块设计，高层模块会根据抽象接口，来实现业务逻辑。
def user_pay(payment, username, money):
    if not payment.login(username):
        print("用户：%s 登录失败." % username)
        return
    print("用户：%s 登录成功." % username) 
    payment.pay(money)

p = WechatPay()
user_pay(p, "Len-xu", 1000)
# 通过这样抽象设计之后，只要接口不修改，底层的修改是不会影响高层模块的设计。

# 接口隔离原则：
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass
    @abstractmethod
    def fly(self):
        pass
    @abstractmethod
    def swim(self):
        pass
# Tiger继承了Animal，所以必须要实现Animal中所有的方法，但是老虎显然不会飞和游泳所以不能实现。
# 这样就应该对抽象Animal类拆分
class Tiger(Animal):
    def run(self):
        print("老虎在跑")

class LandAnimal(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass
class WaterAnimal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass
class SkyAnimal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass

class Tiger(LandAnimal):
    def run(self):
        print("老虎在跑")

class Frog(LandAnimal, WaterAnimal):
    def run(self):
        print("青蛙在跳")
    def swim(self):
        print("青蛙在游泳")