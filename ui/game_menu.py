#-*- coding: utf-8 -*-

import sys
import cocos
from ui.base_screen import BaseScreen
from ui.battle_screen import *
from managers.game_manager import GameManager
from ui.handler_key import *

class GameMenu(cocos.sprite.Sprite):
	def __init__(self, position = (400, 325)):
		super(GameMenu, self).__init__("resources/background/menu_background.jpg", position)
		self.observers = []
		self.menu = cocos.menu.Menu()
		self.create_menu()
		self.observers.append(self.menu)
		self.attach(self.observers)

	def create_menu(self):
		menu_list = []
		menu_list.append(cocos.menu.MenuItem('Continue',self.on_continue))
		menu_list.append(cocos.menu.MenuItem('Load',self.on_load))
		menu_list.append(cocos.menu.MenuItem('Save',self.on_save))
		menu_list.append(cocos.menu.MenuItem('Quit', self.on_quit))
		self.menu.create_menu(menu_list)
		self.menu.position = - 400, -325
		self.add(self.menu, z = 1)


	def on_continue(self):
		self.resume_game()

	def on_load(self):
		print("on_load")
		
	def on_save(self):
		print("on_save")

	def on_quit(self):
		exit()

	def attach(self,observer): #attach observer
		self.observers.append(observer)

	def resume_game(self):
		for observer in self.observers:
			if hasattr(observer,'resume_game_menu'):
				observer.resume_game_menu()

				
