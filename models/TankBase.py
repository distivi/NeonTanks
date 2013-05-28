#!/usr/bin/env python

import cocos
import pyglet

# TankBase - base class for all tansk using in the game

class TankBase(cocos.sprite.Sprite):
    def __init__(self,path = "media/test.png",position=(200,200)):
        super(TankBase,self).__init__(path,position)
        self.x,self.y = position #base object position
        self.speed_x,self.speed_y = 2, 2 #tank speed
        self.hp = 100 # tank's health
        self.isAnemy = True # is tank anemy
        self.power = 0 # tanks power level
        self.schedule(self.update)

    def update(self,obj): #update object
        pass

    def move(self):
        pos = self.x+self.speed_x,self.y+self.speed_y
        self.position = pos

    def shoot(self,obj): # tank shoot
        pass

    def damage(self,damage_point): # set tank damage
        self.hp -= damage_point
        if self.hp <=0:
            self.destroy()
        pass

    def destroy(self): #remove object from layer
        pass

    def getHP(self): # get tank health
        return self.hp

    def getPower(self): # get tank power
        return self.power

    def isAnemy(self): # return tank anemy type
        return self.isAnemy
