#!/usr/bin/env python

import cocos
import pyglet

# TankBase - base class for all tansk using in the game

class TankBase(cocos.sprite.Sprite):
    def __init__(self,power,position=(200,200)):
        super(TankBase,self).__init__("resources/tanks/0.png",position)
        self.x,self.y = position #base object position
        self.speed_x,self.speed_y = 2, 2 #tank speed
        self.hp = 100 # tank's health
        self.isAnemy = True # is tank anemy
        self.path = "" #path to sprite
        self.power = power # tanks power level
        #load texture in agreement with tank power
        if self.power == 0:
            self.path = "resources/tanks/0.png"
        elif self.power == 1:
            self.path = "resources/tanks/1.png"
        elif self.power == 2:
            self.path = "resources/tanks/2.png"
        elif self.power == 3:
            self.path = "resources/tanks/3.png"

        super(TankBase,self).__init__(self.path,position=(self.x,self.y))

        self.schedule(self.update)

    def update(self,obj): #update object
        pass

    def move(self): #move object
        pos = self.x+self.speed_x,self.y+self.speed_y
        self.position = pos

    def shoot(self,obj): #tank shoots
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
