#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import cocos
from ui.base_screen import BaseScreen
from ui.battle_screen import *
from ui.main_menu import *

class LoserScreen(BaseScreen):
	def __init__(self):
		super(LoserScreen, self).__init__()
		self.create_layer()
		self.create_menu()
		
	def create_layer(self):		
		label = cocos.text.Label("You are looser...",
			font_size = 16,
			anchor_x = 'center',
			anchor_y = 'center')		
		label.position = self.win_width / 2, self.win_height - 20
		self.add(label)

	def create_menu(self):
		menu_list = []
		menu_list.append(cocos.menu.MenuItem('Continue', self.on_continue))
		menu_list.append(cocos.menu.MenuItem('Load',self.on_load))
		menu_list.append(cocos.menu.MenuItem('Quit', self.on_quit))
		menu = cocos.menu.Menu()
		menu.create_menu(menu_list)
		menu.position = 0, 0
		self.add(menu)

	def on_continue(self):
		print("on_continue")

	def on_load(self):
		print("on_load")

	def on_quit(self):
		exit()