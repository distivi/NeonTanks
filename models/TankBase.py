#!/usr/bin/env python

import cocos
import pyglet

# TankBase - base class for all tansk using in the game

class TankBase(cocos.sprite.Sprite):
    def __init__(self,path = "media/test.png",position=(200,200)):
        super(TankBase,self).__init__(path,position)
        self.schedule(self.update)
        #self.schedule(self.move)
        self.x,self.y = position #base object position
        self.hp = 100 # tank's health
        self.isAnemy = True # is tank anemy
        self.isMoving = True # is tank moving
        self.power = 0 # tanks power level

    def update(self,obj): #update object
        pass
        #self.rotation += obj*20

    def move(self,obj,x,y):
        pos = self.x+x,self.y+y
        self.position = pos
        if self.x > 500 :
            self.x = 100

    def shoot(self,obj): # tank shoot
        pass
