#!/usr/bin/env python

# Bullet class

import cocos
import pyglet

class Bullet(cocos.sprite.Sprite):
    def __init__(self,path,position,direction):
        super(Bullet,self).__init__(path,position)
        self.x,self.y = position
        self.speed = 1
        self.direction = direction
        self.schedule(self.update)

    def move(self):
        #print "bullet curr position=",self.x,self.y
        if self.direction == 0: #move up
            self.rotation = 0;
            pos = self.x,self.y+self.speed
            self.position = pos
        elif self.direction == 1: #move down
            self.rotation = 180;
            pos = self.x,self.y-self.speed
            self.position = pos
        elif self.direction == 2: #move right
            self.rotation = 90;
            pos = self.x+self.speed,self.y
            self.position = pos
        elif self.direction == 3: # move left
            self.rotation = -90;
            pos = self.x-self.speed,self.y
            self.position = pos
 
    def update(self,obj):
        pass
        #self.move()

    def getPosition(self):
        return (self.x,self.y)

    def destroy(self): #destroy object
        pass
