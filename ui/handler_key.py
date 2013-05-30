#!/usr/bin/env python
#-*- coding:utf8 -*-

import sys
import cocos
import pyglet
from base_screen import BaseScreen
#from main_menu import MenuScreen

ESC = 65307

class HandlerKey(BaseScreen):
    
    is_event_handler = True

    def __init__(self):
        super( HandlerKey, self).__init__()

        self.direction = 'none'
        self.text = cocos.text.Label("Olo", x=100,y=100)
        self.add(self.text)

    def on_key_press(self,key,modifiers):
    	if key == ESC:
           self.text.element.text = "ESC"
           print "ESC"
        else:
            #mainMenu = cocos.scene.Scene(MenuScreen())
            #cocos.director.director.push(mainMenu)
            self.text.element.text = pyglet.window.key.symbol_string(key)
 
cocos.director.director.init(resizable=True, caption="Test handler key")
cocos.director.director.run(cocos.scene.Scene( HandlerKey() ) )