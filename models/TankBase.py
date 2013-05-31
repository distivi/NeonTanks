#!/usr/bin/env python

import cocos
import pyglet
import random

# TankBase - base class for all tanks 

class TankBase(cocos.sprite.Sprite):
    def __init__(self,power,position=(200,200)):
        super(TankBase,self).__init__("resources/tanks/tank_player.png",position)
        self.x,self.y = position #base object position
        #self.speed = 1 #tank speed
        self.hp = 100 # tank's health
        self.isAnemy = True # is tank anemy
        self.path = "" #path to sprite
        self.power = power # tanks power level
        self.direction = "needed to be defined" #!!!!!!!!!!!!!!!!!!!!
        #load texture in agreement with tank power
        if self.power == 0:
            self.path = "resources/tanks/tank_standart.png"
        elif self.power == 1:
            self.path = "resources/tanks/tank_fast.png"
        elif self.power == 2:
            self.path = "resources/tanks/tank_heavy.png"
        elif self.power == 3:
            self.path = "resources/tanks/tank_player.png"

        super(TankBase,self).__init__(self.path,position=(self.x,self.y))

        self.defineSpeed()

        self.schedule(self.update)
        self.schedule_interval(self.shoot,2) # shoots every 2 seconds

    def update(self,obj): #update object
        pass

    def move(self,direction=1): #move object
        if direction == 0: #move up
            self.rotation = 0;
            pos = self.x,self.y+self.speed
            self.position = pos
        elif direction == 1: #move down
            self.rotation = 180;
            pos = self.x,self.y-self.speed
            self.position = pos
        elif direction == 2: #move right
            self.rotation = 90;
            pos = self.x+self.speed,self.y
            self.position = pos
        elif direction == 3: # move left
            self.rotation = -90;
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

    def getXml(self):
        root = ET.Element('tank')		
        root.attrib = {'power':str(self.power),'position':str(self.position),'direction':str(self.direction),'hp':str(self.hp)}
        return root

    def defineSpeed(self):
        if self.power == 0: #fast tank
            self.speed = 1
        elif self.power == 1: #standart tank
            self.speed = 0.5
        else: # heavy tank
            self.speed = 0.1
