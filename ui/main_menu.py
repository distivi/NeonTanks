# -*- coding: utf-8 -*-

import sys
import cocos
from base_screen import BaseScreen
from ui.battle_screen import BattleScreen
from ui.tank_crash_screen import TankCrashScreen


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
		menu_list.append(cocos.menu.MenuItem('Continue',self.on_continue))
		menu_list.append(cocos.menu.MenuItem('New Game',self.on_new_game))
		menu_list.append(cocos.menu.MenuItem('Tank crash test', self.on_crashTest ))
		menu_list.append(cocos.menu.MenuItem('Load',self.on_load))
		menu_list.append(cocos.menu.MenuItem('Save',self.on_save))
		menu_list.append(cocos.menu.MenuItem('Quit', self.on_quit))
		menu = cocos.menu.Menu()
		menu.create_menu(menu_list);
		menu.position = 0, 0
		self.add(menu)

	def on_continue(self):
		print "on_continue"

	def on_new_game(self):			
		battleScreen = cocos.scene.Scene(BattleScreen())
		cocos.director.director.push(battleScreen)

	def on_crashTest(self):
		testScreen = cocos.scene.Scene(TankCrashScreen())
		cocos.director.director.push(testScreen)

	def on_load(self):
		print "on_load"
		
	def on_save(self):
		print "on_save"		

	def on_quit(self):
		exit()



	
        


