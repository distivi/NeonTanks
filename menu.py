# | ${color} ${color} | ${color} ${color} -*- coding: utf-8 -*-
import sys
import cocos
import pyglet
import base_screen
from base_screen import BaseScreen




class Picture(cocos.sprite.Sprite):
    def __init__(self,path="resources/face.png",position=(200,200)):
        super(Picture,self).__init__(path,position)
        self.path = path
        self.schedule(self.update)
    
    def update(self,obj):
        pass

class MenuScreen(BaseScreen):	
	def __init__(self):
		super(MenuScreen, self).__init__()		
		self.create_layer()
		self.create_menu()
		

	def create_layer(self):		
		label = cocos.text.Label("Main Menu",
			font_size = 16,
			anchor_x = 'center',
			anchor_y = 'center')		
		label.position = self.win_width / 2, self.win_height - 20
		self.add(label)

	def create_menu(self):
		menu_list = []
		menu_list.append(cocos.menu.MenuItem('New Game',self.on_new_game))		
		menu_list.append(cocos.menu.MenuItem('Quit', self.on_quit ))
		menu = cocos.menu.Menu()
		menu = create_menu(menu_list);
		menu.position = 0,0 #self.win_width / 2, self.win_height / 2
		self.add(menu)


	def on_new_game():
		print "new game"

	def on_quit():
		print "exit from game"

cocos.director.director.init()
scene = cocos.scene.Scene()

scene.add(Picture("luxfon.com-6398.jpg", position=(333,333)))
#scene.add(pict)
cocos.director.director.run(scene)


