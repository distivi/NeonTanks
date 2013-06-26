#!/usr/bin/env python

import copy
import cocos
import pyglet
from random import randint
import xml.etree.ElementTree as ET
from models.bullet import Bullet
from models.enemy_brain import EnemyBrain
from managers.sound_manager import SoundManager

# TankBase - base class for all tanks 

class TankBase(cocos.sprite.Sprite):
    def __init__(self,power,position=(200,200),isEnemy = True):
        super(TankBase,self).__init__("resources/tanks/tank_player.png",position)
        self.observers = [] # kepp observers
        self.x,self.y = position #base object position
        self.isMoving = False
        self.isRotating = False
        self.isNeedRotateBeforeMoving = False
        self.hp = 5 # tank's health
        self.isEnemy = isEnemy # is tank anemy
        self.path = "" #path to sprite
        self.power = power # tanks power level
        self.direction = 0
        self.bullet_power = 0
        self.setDirection(0)
        self.bullet_direction = 0
        self.moving_animation = None
        


        #load texture

        if self.power == 0:
            self.path = "resources/tanks/neon_tank_standart.png"
            self.bullet_power = 1
        elif self.power == 1:
            self.path = "resources/tanks/neon_tank_speed.png"
            self.bullet_power = 1
        elif self.power == 2:
            self.path = "resources/tanks/neon_tank_heavy.png"
            self.bullet_power = 2
        elif self.power == 3:
            self.direction = -1
            self.bullet_power = 1
            self.path = "resources/tanks/neon_tank_player.png"            
        elif self.power == 4:
            self.bullet_power = 2
            self.direction = -1
            self.path = "resources/tanks/neon_tank_player_heavy.png"

        # WARNING: only for test
        # self.path = "resources/tanks/tank_test.png"

        super(TankBase,self).__init__(self.path,position=(self.x,self.y))
        self.add_shadow()

        self.defineSpeed()

        if self.power < 3:
            # for enemy tanks
            self.way_nodes = []
            self.schedule_interval(self.AI_movement,0.1) #change direction every 1 sec
            self.schedule_interval(self.shoot,1) # shoots every 2 seconds


    def add_shadow(self):
        shadow_path = None
        
        if self.power == 0:
            shadow_path = "resources/tanks/shadow_for_neon_tank_standart.png"        
        elif self.power == 1:
            shadow_path = "resources/tanks/shadow_for_neon_speed_tank.png"
        elif self.power == 2:
            shadow_path = "resources/tanks/shadow_for_neon_heavy_tank.png"
        elif self.power == 3:
            shadow_path = "resources/tanks/shadow_for_neon_tank_player.png"
        elif self.power == 4:
            shadow_path = "resources/tanks/shadow_for_neon_tank_player_heavy.png"

        if shadow_path:
            shadow = cocos.sprite.Sprite(shadow_path)
            self.add(shadow,z = -1)

    def attach(self,observer): #attach observer
        self.observers.append(observer)

    def AI_movement(self,dt):
        self.way_nodes = EnemyBrain.instance.get_direction_for_tank(self)
        
        if self.way_nodes and len(self.way_nodes) > 1:
            '''
            for observer in self.observers:
                if hasattr(observer,'draw_enemy_moved_path'):
                    observer.draw_enemy_moved_path(self.way_nodes)
            '''

            self.set_AI_direction()
        else:
            self.setDirection(-1)
 

    def set_AI_direction(self):
        if self.way_nodes and len(self.way_nodes) > 1:
            first_node = self.way_nodes[1]
            new_position = first_node.position

            new_direction = -1

            if new_position.x > self.position[0]:
                new_direction = 1
            elif new_position.x < self.position[0]:
                new_direction = 3
            elif new_position.y > self.position[1]:
                new_direction = 0
            elif new_position.y < self.position[1]:
                new_direction = 2

            self.setDirection(new_direction)
            self.way_nodes.remove(self.way_nodes[0])



    def user_select_direction(self, direction):
        self.setDirection(direction)

    def move(self): #move object        
        if self.direction == -1 or self.isRotating: # stand or rotating
            return

        if self.isNeedRotateBeforeMoving:
            self.rotate_tank()
            
        tank_length = 10
        distance = 20
        pos = 0,0
        angle = 0

        angle = self.direction * 90
        isTankMoveByY = (self.direction % 2 == 0)
        isTankMoveingPositive = (self.direction ==0 or self.direction ==1)
        pluxMinusDirection = 1 if isTankMoveingPositive else -1

        if isTankMoveByY:
            pos = 0,distance * pluxMinusDirection
        else:
            pos = distance * pluxMinusDirection, 0
            
        startMoving = cocos.actions.CallFunc(self.setMoving, True)
        moveTank = cocos.actions.MoveBy(pos, duration = self.speed)
        endMoving = cocos.actions.CallFunc(self.setMoving, False)
        
        self.moving_animation = startMoving + moveTank + endMoving

        self.do(self.moving_animation)

    def rotate_tank(self):
        if self.direction == -1:
            return

        self.isNeedRotateBeforeMoving = False

        angle = self.direction * 90        
        rotate_duration = 0 if angle == self.rotation else 0.2

        begin_animation = cocos.actions.CallFunc(self.setRotating, True)
        rotateTank = cocos.actions.RotateTo(angle, duration = rotate_duration)
        end_animation = cocos.actions.CallFunc(self.setRotating, False)
        rotate_animation = begin_animation + rotateTank + end_animation
        self.do(rotate_animation)

        

    def shoot(self,obj = 1): #tank shoots        
        SoundManager(0.4).playShoot()
        if self.isRotating:
            return

        if not self.isEnemy:
            bullet = Bullet("resources/bullets/player_bullet.png",self.position,self.bullet_direction,self.isEnemy,self.bullet_power)        
        else:
            bullet = Bullet("resources/bullets/enemy_bullet.png",self.position,self.bullet_direction,self.isEnemy,self.bullet_power)
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

    def say_where_i_am(self):        
        for observer in self.observers:
            if hasattr(observer,"tankMoved"):
                observer.tankMoved(self)
 

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
        if self.direction != direction:            
            self.direction = direction
            if not self.isMoving:
                self.rotate_tank()
            else:
                self.isNeedRotateBeforeMoving = True 

            if self.direction != -1:
                self.bullet_direction = self.direction

        
    def setMoving(self,isMoving = False):        
        self.isMoving = isMoving
        if not isMoving:
            self.say_where_i_am()
            if self.isNeedRotateBeforeMoving:
                self.rotate_tank()
            if self.power < 3:
                self.set_AI_direction()
                    

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