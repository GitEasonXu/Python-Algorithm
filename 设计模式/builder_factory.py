#!/usr/bin/env python
# coding=utf-8
'''
Author: Len-xu
Date: 2021-02-21 14:22:53
LastEditTime: 2021-02-21 14:36:38
LastEditors: Do not edit
FilePath: \Python-Algorithm\设计模式\builder_factory.py
Description: 建造者模式
'''
from abc import ABCMeta, abstractmethod

# 产品
class Player:
    def __init__(self, face=None, body=None, arm=None, leg=None) -> None:
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg
    def __str__(self) -> str:
        return "{}, {}, {}, {}".format(self.face, self.body, self.arm, self.leg)

#抽象建造者
class Builder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass
    @abstractmethod
    def build_body(self):
        pass
    @abstractmethod
    def build_arm(self):
        pass
    @abstractmethod
    def build_leg(self):
        pass

#具体建造者
class MonsterBuilder(Builder):
    def build_face(self):
        return "创建怪兽脸"

    def build_body(self):
        return "创建怪兽身体"

    def build_arm(self):
        return "创建怪兽手臂"

    def build_leg(self):
        return "创建怪兽腿"
#指挥者
class PlayerDirector:
    def __init__(self) -> None:
        self.player = Player()

    def build_player(self, builder):
        self.player.body = builder.build_body()
        self.player.face = builder.build_face()
        self.player.arm = builder.build_arm()
        self.player.leg = builder.build_leg()
        return self.player

#客户端
builder = MonsterBuilder()
play_dir = PlayerDirector()
player = play_dir.build_player(builder)
print(player)

