#!/usr/bin/env python

import copy
import cocos
import pyglet
from random import randint
import xml.etree.ElementTree as ET
from models.bullet import Bullet
from managers.sound_manager import SoundManager

# TankBase - base class for all tanks 

class TankBase(cocos.sprite.Sprite):
    def __init__(self,power,position=(200,200),isEnemy = True):
        super(TankBase,self).__init__("resources/tanks/tank_player.png",position)
        self.observers = [] # kepp observers
        self.x,self.y = position #base object position
        self.isMoving = False
        self.hp = 100 # tank's health
        self.isEnemy = isEnemy # is tank anemy
        self.path = "" #path to sprite
        self.power = power # tanks power level
        self.direction = 0        
        self.setDirection(0)        
        self.soundManager = SoundManager(0)

        #load texture in agreement with tank power

        if self.power == 0:
            self.path = "resources/tanks/tank_standart.png"
        elif self.power == 1:
            self.path = "resources/tanks/tank_fast.png"
        elif self.power == 2:
            self.path = "resources/tanks/tank_heavy.png"
        elif self.power == 3:
            self.direction = -1
            self.path = "resources/tanks/tank_player.png"

        # WARNING: only for test
        # self.path = "resources/tanks/tank_test.png"

        super(TankBase,self).__init__(self.path,position=(self.x,self.y))

        self.defineSpeed()

        if self.power != 3:
            # for enemy tanks
            self.schedule_interval(self.AI_movement,3) #change direction every 1.5 sec
            self.schedule_interval(self.shoot,2) # shoots every 2 seconds

    def attach(self,observer): #attach observer
        self.observers.append(observer)

    def AI_movement(self,dt):
        randDirection = randint(0,3)        
        self.setDirection(randDirection)

    def user_select_direction(self, direction):
        self.setDirection(direction)

    def move(self): #move object        
        tank_length = 10
        distance = 20
        pos = 0,0
        angle = 0

        if self.direction == -1: # stand
            return
        elif self.direction == 0: #move up
            angle = 0 
            pos = 0,distance

        elif self.direction == 1: #move down
            angle = 180
            pos = 0,-distance

        elif self.direction == 2: #move right
            angle = 90
            pos = distance,0 
            
        elif self.direction == 3: # move left
            angle = 270
            pos = -distance,0            

        startMoving = cocos.actions.CallFunc(self.setMoving, True)
        rotate_duration = 0 if angle == self.rotation else 0.2
        rotateTank = cocos.actions.RotateTo(angle, duration = rotate_duration)
        moveTank = cocos.actions.MoveBy(pos, duration = self.speed)
        endMoving = cocos.actions.CallFunc(self.setMoving, False)

        self.do(startMoving + rotateTank + moveTank + endMoving)
        

    def shoot(self,obj = 1): #tank shoots                
        self.soundManager.play()        
        bullet = Bullet("resources/bullets/bullet1.png",self.position,self.bullet_direction,self.isEnemy)        
        for observer in self.observers:
            if hasattr(observer,'tankShoot'):
                observer.tankShoot(bullet)


    def get_next_step_rect(self):
        rect = self.get_rect()
        distance = 20.0
        
        if self.direction == -1: # stand
            return rect
        elif self.direction == 0: #move up
            rect.y += distance
        elif self.direction == 1: #move down
            rect.y -= distance
        elif self.direction == 2: #move right
            rect.x += distance            
        elif self.direction == 3: # move left
            rect.x -= distance
        return rect


    def damage(self,damage_point): # set tank damage
        self.hp -= damage_point
        if self.hp <=0:
            self.destroy()
        pass

    def destroy(self): #remove object from layer
        self.kill()
        for observer in self.observers:
            if hasattr(observer,'tankDestroyed'):
                observer.tankDestroyed(self)
 

    def getHP(self): # get tank health
        return self.hp

    def getPower(self): # get tank power
        return self.power

    def isEnemy(self): # return tank anemy type
        return self.isEnemy

    def setPosition(self,position):        
        self.position = position 

    def getPosition(self): #get tank position
        return self.position

    def getDirection(self): #get tank direction
        return self.direction

    def setDirection(self,direction): #set tank direction        
        if direction != -1:
            self.bullet_direction = self.direction

        
        if self.direction != direction and direction != -1:
            self.direction = direction
            if not self.isMoving:                
                angle = 0
                if direction == 0: #move up
                    angle = 0
                elif direction == 1: #move down
                    angle = 180                
                elif direction == 2: #move right
                    angle = 90                                
                elif direction == 3: # move left
                    angle = 270                
            
                startMoving = cocos.actions.CallFunc(self.setMoving, True)
                rotate_duration = 0 if angle == self.rotation else 0.2
                rotateTank = cocos.actions.RotateTo(angle, duration = rotate_duration)
                endMoving = cocos.actions.CallFunc(self.setMoving, False)
                self.do(startMoving + rotateTank + endMoving)         
            

        self.direction = direction
            
        
        
    def setMoving(self,isMoving = False):        
        self.isMoving = isMoving            

    def getXml(self):
        root = ET.Element('tank')		
        root.attrib = {'power':str(self.power),'position':str(self.position),'direction':str(self.direction),'hp':str(self.hp)}
        return root

    def defineSpeed(self):
        if self.power == 0: #fast tank
            self.speed = 0.1
        elif self.power == 1: #standart tank
            self.speed = 0.2
        else: # heavy tank
            self.speed = 0.2
