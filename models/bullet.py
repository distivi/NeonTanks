#!/usr/bin/env python

# Bullet class new

import cocos
import pyglet

class Bullet(cocos.sprite.Sprite):
    def __init__(self,path,position,direction,isEnemy = True):
        super(Bullet,self).__init__(path,position)
        self.x,self.y = position
        self.speed = 0.05
        self.isMoving = False
        self.isEnemy = isEnemy
        self.direction = direction
        self.init_real_position()

    def init_real_position(self):
        distance = 20

        self.move_posistion = 0,0

        if self.direction == 0: #move up            
            self.move_posistion = 0,distance

        elif self.direction == 1: #move down            
            self.move_posistion = 0,-distance

        elif self.direction == 2: #move right            
            self.move_posistion = distance,0
            
        elif self.direction == 3: # move left            
            self.move_posistion = -distance,0

        self.x += self.move_posistion[0]
        self.y += self.move_posistion[1]


    def move(self):
        self.isMoving = True
        moveAction = cocos.actions.MoveBy(self.move_posistion, duration = self.speed)
        repeatMoving = cocos.actions.Repeat(moveAction)  

        self.do(repeatMoving)
 
    
    def getPosition(self):
        return (self.x,self.y)

    def destroy(self): #destroy object
        self.kill()
        
        
