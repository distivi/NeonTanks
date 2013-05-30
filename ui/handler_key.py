#-*- coding: utf8 -*-

import sys
import cocos
import pyglet
from base_screen import BaseScreen

ESC = 65307
LEFT = 65361
UP = 65362
RIGHT = 65363
DOWN = 65364


class HandlerKey(BaseScreen):
    is_event_handler = True
    def __init__(self):
        super( HandlerKey, self).__init__()
        self.chars_pressed = set()
        self.direction = 'none'
        self.text = cocos.text.Label("Test class HandlerKey", x=100,y=100)
        self.add(self.text)

    def on_key_press(self, key, modifiers):
       self.chars_pressed.add(key)
       self.text.element.text = pyglet.window.key.symbol_string(key)
        
    def on_key_release(self, key, modifiers):
       self.chars_pressed.remove(key)
 
cocos.director.director.init(resizable=True, caption="Handler key")
cocos.director.director.run(cocos.scene.Scene( HandlerKey() ) )