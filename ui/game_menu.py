#-*- coding: utf-8 -*-

import sys
import cocos
from base_screen import BaseScreen
from battle_screen import *
from managers.game_manager import GameManager
from handler_key import *

class GameMenu(BaseScreen):
	def __init__(self):
		super(GameMenu, self).__init__()
		self.create_menu()
		self.game_menu_background()

	def create_menu(self):
		menu_list = []
		menu_list.append(cocos.menu.MenuItem('Continue',self.on_continue))
		menu_list.append(cocos.menu.MenuItem('Load',self.on_load))
		menu_list.append(cocos.menu.MenuItem('Save',self.on_save))
		menu_list.append(cocos.menu.MenuItem('Quit', self.on_quit))
		self.menu = cocos.menu.Menu()
		self.menu.create_menu(menu_list);
		self.menu.position = 0, 0
		self.add(self.menu, z = 1)

	def game_menu_background(self):
		#create background game_menu
		self.menu_background  = cocos.sprite.Sprite("resources/fon/menu_background.jpg")
		self.menu_background.position = self.win_width / 2, (self.win_height / 2) + 25
		self.add(self.menu_background)

	def on_continue(self):
		resumeGame = BattleScreen()
		self.remove(self.menu)
		self.remove(self.menu_background)
		self.schedule_interval(resumeGame.update(), 0.01) 

	def on_load(self):
		print "on_load"
		
	def on_save(self):
		print "on_save"		

	def on_quit(self):
		print "quit"