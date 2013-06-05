#-*- coding: utf-8 -*-

import sys
import cocos
from base_screen import BaseScreen
from ui.battle_screen import *

class GameMenu(BaseScreen):
	def __init__(self):
		super(GameMenu, self).__init__()
		self.create_layer()
		self.create_menu()


	def create_layer(self):
		label = cocos.text.Label("Game menu",
			font_size = 16,
			anchor_x = 'center',
			anchor_y = 'center')		
		label.position = self.win_width / 2, self.win_height - 20
		self.add(label)


	def create_menu(self):
		menu_list = []
		menu_list.append(cocos.menu.MenuItem('Continue',self.on_continue))
		menu_list.append(cocos.menu.MenuItem('Load',self.on_load))
		menu_list.append(cocos.menu.MenuItem('Save',self.on_save))
		menu_list.append(cocos.menu.MenuItem('Quit', self.on_quit))
		menu = cocos.menu.Menu()
		menu.create_menu(menu_list);
		menu.position = 0, 0
		self.add(menu)

	def on_continue(self):
		cocos.director.director.pop()

	def on_load(self):
		print "on_load"
		
	def on_save(self):
		print "on_save"		

	def on_quit(self):
		cocos.director.director.pop()