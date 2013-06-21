# -*- coding: utf-8 -*-

import sys
import cocos
from base_screen import BaseScreen
from ui.battle_screen import BattleScreen
from ui.tank_crash_screen import TankCrashScreen


class MenuScreen(BaseScreen):	
	def __init__(self):
		super(MenuScreen, self).__init__(bg_image = "resources/background/background_image_main_menu.png")		
		self.create_menu()
		

	def create_menu(self):
		menu_list = []
		menu_list.append(cocos.menu.ImageMenuItem("resources/buttons/btn_continue.png",self.on_continue))
		menu_list.append(cocos.menu.ImageMenuItem("resources/buttons/btn_newgame.png",self.on_new_game))
		#menu_list.append(cocos.menu.MenuItem('Tank crash test', self.on_crashTest ))
		menu_list.append(cocos.menu.ImageMenuItem("resources/buttons/btn_load.png",self.on_load))
		menu_list.append(cocos.menu.ImageMenuItem("resources/buttons/btn_save.png",self.on_save))
		menu_list.append(cocos.menu.ImageMenuItem("resources/buttons/btn_exit.png", self.on_quit))
		menu = cocos.menu.Menu()
		menu.create_menu(menu_list);
		menu.position = 0,-91
		self.add(menu,z=1)

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



	
        


