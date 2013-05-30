#!/usr/bin/env python

import cocos
import pyglet
import random

# TankBase - base class for all tanks 

class TankBase(cocos.sprite.Sprite):
    def __init__(self,power,position=(200,200)):
        super(TankBase,self).__init__("resources/tanks/0.png",position)
        self.x,self.y = position #base object position
        self.speed = 0.4 #tank speed
        self.hp = 100 # tank's health
        self.isAnemy = True # is tank anemy
        self.path = "" #path to sprite
        self.power = power # tanks power level
        self.direction = "needed to be defined" #!!!!!!!!!!!!!!!!!!!!
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
        self.schedule_interval(self.shoot,2) # shoots every 2 seconds

    def update(self,obj): #update object
        pass

    def move(self,direction=1): #move object
        if direction == 0: #move up
            self.rotation = 180;
            pos = self.x,self.y+self.speed
            self.position = pos
        elif direction == 1: #move down
            self.rotation = 0;
            pos = self.x,self.y-self.speed
            self.position = pos
        elif direction == 2: #move right
            self.rotation = -90;
            pos = self.x+self.speed,self.y
            self.position = pos
        elif direction == 3: # move left
            self.rotation = 90;
            pos = self.x-self.speed,self.y
            self.position = pos


    def shoot(self,obj): #tank shoots
        print "Shoot"

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

    def getPosition(self): #get tank position
        return self.position

    def getDirection(self): #get tank direction
        return self.direction

    def sefDirection(self,direction): #set tank direction
        pass

