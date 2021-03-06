#!/usr/bin/env python

import cocos
import pyglet
import xml.etree.ElementTree as ET
from random import randint

class Bonus(cocos.sprite.Sprite):
    def __init__(self,bonusType,path="resources/bonuses/0.png",position = (200,200)):
        super(Bonus,self).__init__(path,position)
        self.path = ""
        self.bonusType = bonusType
        self.isActivate = True
        self.timeout = 100
        self.observers = []

        #load textures
        if bonusType == 0: #star, increase tank level
            self.path = "resources/bonuses/0.png"
        elif bonusType == 1: # slow time
            self.path = "resources/bonuses/1.png"
        else:
            self.path = "resources/bonuses/2.png"

        super(Bonus,self).__init__(self.path,position)
        self.schedule_interval(self.update,4)
        self.schedule_interval(self.destroy,6)

    def update(self,obj):
        ##printself.parent
        while self.timeout > 0:
            self.blink()
            ##printself.timeout

    def getXml(self):
        root = ET.Element('bonus')		
        root.attrib = {'position':str(self.position),'type':str(self.bonusType)}
        return root

    def destroy(self,obj=1):
        #if self.timeout <= 0:
        self.kill()
        #print"Bonus removed"
            
        for observer in self.observers:
            if hasattr(observer,"removeBonus"):
                observer.removeBonus(self)

    def blink(self):
       action = cocos.actions.interval_actions.Blink(5,2)
       kill = cocos.actions.CallFunc(self.destroy,0)
       self.do(action)
       self.timeout -=1

    def attach(self,observer):
        self.observers.append(observer)

    def reset(self,position):
        self.timeout = 100

    def tank_took_it(self):
        self.destroy()
        #print"Bonus destroyed"
        for observer in self.observers:
            if hasattr(observer,"removeBonus"):
                observer.removeBonus(self)

    def get_bonus_type(self):
        return self.bonusType
