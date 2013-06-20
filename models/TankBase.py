#!/usr/bin/env python

import copy
import cocos
import pyglet
from random import randint
import xml.etree.ElementTree as ET
from models.bullet import Bullet
#from managers.sound_manager import SoundManager

# TankBase - base class for all tanks 

class TankBase(cocos.sprite.Sprite):
    def __init__(self,power,position=(200,200),isEnemy = True):
        super(TankBase,self).__init__("resources/tanks/tank_player.png",position)
        self.observers = [] # kepp observers
        self.x,self.y = position #base object position
        self.isMoving = False
        self.isRotating = False
        self.isNeedRotateAfterMoving = False
        self.hp = 5 # tank's health
        self.isEnemy = isEnemy # is tank anemy
        self.path = "" #path to sprite
        self.power = power # tanks power level
        self.bullet_power = 0
        self.direction = 0        
        self.setDirection(0)
        self.moving_animation = None
        #self.soundManager = SoundManager(0)


        #load texture

        if self.power == 0:
            self.path = "resources/tanks/tank_standart.png"
            self.bullet_power = 1
        elif self.power == 1:
            self.path = "resources/tanks/neon_tank_speed.png"
            self.bullet_power = 1
        elif self.power == 2:
            self.path = "resources/tanks/tank_heavy.png"
            self.bullet_power = 2
        elif self.power == 3:
            self.direction = -1
            self.bullet_power = 1
            self.path = "resources/tanks/neon_tank_player.png"            
        elif self.power == 4:
            self.bullet_power = 2
            self.direction = -1
            self.path = "resources/tanks/tank_player_heavy.png"

        # WARNING: only for test
        # self.path = "resources/tanks/tank_test.png"

        super(TankBase,self).__init__(self.path,position=(self.x,self.y))
        self.add_shadow()

        self.defineSpeed()

        if self.power != 3 and self.power != 4:
            # for enemy tanks
            self.schedule_interval(self.AI_movement,3) #change direction every 1.5 sec
            self.schedule_interval(self.shoot,2) # shoots every 2 seconds

    def add_shadow(self):
        shadow_path = None
        
        if self.power == 3:
            shadow_path = "resources/tanks/shadow_for_neon_tank_player.png"
        elif self.power == 1:
            shadow_path = "resources/tanks/shadow_for_neon_speed_tank.png"
        if shadow_path:
            shadow = cocos.sprite.Sprite(shadow_path)
            self.add(shadow,z = -1)

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

        angle = self.direction * 90
        isTankMoveByY = (self.direction % 2 == 0)
        isTankMoveingPositive = (self.direction ==0 or self.direction ==1)
        pluxMinusDirection = 1 if isTankMoveingPositive else -1

        if isTankMoveByY:
            pos = 0,distance * pluxMinusDirection
        else:
            pos = distance * pluxMinusDirection, 0
            
        startMoving = cocos.actions.CallFunc(self.setMoving, True)
        rotate_duration = 0 if angle == self.rotation else 0.2
        rotateTank = cocos.actions.RotateTo(angle, duration = rotate_duration)
        moveTank = cocos.actions.MoveBy(pos, duration = self.speed)
        endMoving = cocos.actions.CallFunc(self.setMoving, False)
        
        self.moving_animation = startMoving + rotateTank + moveTank + endMoving

        self.do(self.moving_animation)

    def rotate_tank(self):
        if self.direction == -1:
            return

        angle = self.direction * 90        
        rotate_duration = 0 if angle == self.rotation else 0.2
        rotateTank = cocos.actions.RotateTo(angle, duration = rotate_duration)
        self.do(rotateTank)

        

    def shoot(self,obj = 1): #tank shoots        
        #self.soundManager.playShoot()
        bullet = Bullet("resources/bullets/bullet1.png",self.position,self.bullet_direction,self.isEnemy,self.bullet_power)        
        for observer in self.observers:
            if hasattr(observer,'tankShoot'):
                observer.tankShoot(bullet)


    def get_next_step_rect(self):
        rect = self.get_rect()
        distance = 20.0
        
        if self.direction == -1: # stand
            return rect

        isTankMoveByY = (self.direction % 2 == 0)
        isTankMoveingPositive = (self.direction ==0 or self.direction ==1)
        pluxMinusDirection = 1 if isTankMoveingPositive else -1

        if isTankMoveByY:
            rect.y += distance * pluxMinusDirection
        else:
            rect.x += distance * pluxMinusDirection
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
        self.direction = direction

        if not self.isMoving:           
            if direction != -1:
                self.bullet_direction = direction            
        # else:
        #     self.rotate_tank()

        
    def setMoving(self,isMoving = False):        
        self.isMoving = isMoving
                    

    def setRotating(self,isRotating = False):
        self.isRotating = isRotating

    def getXmlWithParrentNode(self,root):
        tankNode = ET.SubElement(root,'tank')		
        tankNode.attrib = {'power':str(self.power),'position':str(self.position),'direction':str(self.direction),'hp':str(self.hp)}
        return tankNode

    def defineSpeed(self):
        if self.power == 0: #fast tank
            self.speed = 0.1
        elif self.power == 1: #standart tank
            self.speed = 0.2
        else: # heavy tank
            self.speed = 0.2

    def slowDown(self,koef=0.5): # define speed after slow down bonus got(only for enemy tanks
        self.speed = self.speed/koef

    def got_bonus(self): # WARNING Only for enemy tanks
        self.path = "resources/tanks/tank_heavy.png"

    # Testing zone
    def setPath(self, path):
        self.path = path
        #super(TankBase,self).__init__(self.path,position=(self.x,self.y)) 

    def getPath(self):
        return self.path
