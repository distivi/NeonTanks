# -*- coding: utf-8 -*-

import sys
import cocos
from base_screen import BaseScreen
from ui.battle_screen import BattleScreen


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
		menu.create_menu(menu_list);
		menu.position = 0, 0
		self.add(menu)


	def on_new_game(self):			
		battleScreen = cocos.scene.Scene(BattleScreen())
		cocos.director.director.push(battleScreen)

	def on_quit(self):
		print "exit from game"

