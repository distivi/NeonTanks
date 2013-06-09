#-*- coding: utf-8 -*-

import sys
import cocos
from base_screen import BaseScreen
from ui.battle_screen import *

class GameMenu():
	def __init__(self):
		self.create_menu()

	def create_menu(self):
		menu_list = []
		menu_list.append(cocos.menu.MenuItem('Continue',self.on_continue))
		menu_list.append(cocos.menu.MenuItem('Load',self.on_load))
		menu_list.append(cocos.menu.MenuItem('Save',self.on_save))
		menu_list.append(cocos.menu.MenuItem('Quit', self.on_quit))
		self.menu = cocos.menu.Menu()
		self.menu.create_menu(menu_list);
		self.menu.position = 0, 0
		self.add(self.menu)

	def on_continue(self):
		self.remove(self.menu)

	def on_load(self):
		print "on_load"
		
	def on_save(self):
		print "on_save"		

	def on_quit(self):
		print "quit"