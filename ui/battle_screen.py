# -*- coding: utf-8 -*-

import cocos
from base_screen import BaseScreen
from models.static_block import *
from models.brick_block import *
from models.map import Map
from managers.game_manager import GameManager
from handler_key import *


class BattleScreen(HandlerKey):	
	def __init__(self):
		super(BattleScreen, self).__init__()		
		self.create_layer()						
		self.info_enemeis()
		self.info_panzer()
		self.button_menu()

		self.init_game()		
		self.schedule_interval(self.update, 0.01) 


	def update(self, dt):
		self.update_tank_position()
		self.game_manager.update()
		self.game_manager.updateSpawnTanks()
		

	def create_layer(self):		
		label = cocos.text.Label("Battle Screen",
			font_size = 16,
			anchor_x = 'center',
			anchor_y = 'center')		
		label.position = self.win_width / 2, self.win_height - 20
		self.add(label)

	def init_game(self):
		self.game_manager = GameManager(1)
		self.game_manager.attach(self)
		self.game_manager.map.position = self.win_width / 2 - 260, self.win_height / 2 - 260
		self.add(self.game_manager.map)

	def update_tank_position(self):	
		if hasattr(self.game_manager,'player_tank'):
			tank_direction = -1	
			if LEFT in self.chars_pressed:			
				tank_direction = 3

			elif RIGHT in self.chars_pressed:			
				tank_direction = 2

			elif UP in self.chars_pressed:			
				tank_direction = 0

			elif DOWN in self.chars_pressed:			
				tank_direction = 1

			self.game_manager.player_tank.user_select_direction(tank_direction)
			

	def on_key_press(self, key, modifiers):
		super(BattleScreen,self).on_key_press(key,modifiers)
		if SPACE == key: 				
			self.game_manager.player_tank.shoot()



	def info_enemeis(self):
		easyEnemy = 6	#will be count
		normalEnemy = 4 #will be count
		hardEnemy = 20   #will be count
		width = self.win_width
		height = self.win_height
		indentLabelWidth = 100
		indentLabelHeight = 20

		labelEnemy = cocos.text.Label("Enemy: ", 
			font_size = 12,
			anchor_x = 'left',
			anchor_y = 'top',)
		labelEnemy.position = width - indentLabelWidth , height - indentLabelHeight
		indentLabelHeight += 20 
		self.add(labelEnemy)

		labelEasy = cocos.text.Label(("Easy: " + easyEnemy.__str__()), 
			font_size = 11,
			anchor_x = 'left',
			anchor_y = 'top',)
		labelEasy.position = width - indentLabelWidth , height - indentLabelHeight  
		indentLabelHeight += 20
		self.add(labelEasy)

		labelNormal = cocos.text.Label(("Normal: " + normalEnemy.__str__()), 
			font_size = 11,
			anchor_x = 'left',
			anchor_y = 'top',)
		labelNormal.position = width - indentLabelWidth , height - indentLabelHeight
		indentLabelHeight += 20
		self.add(labelNormal)

		labelHard = cocos.text.Label(("Hard: " + hardEnemy.__str__()), 
			font_size = 11,
			anchor_x = "left",
			anchor_y = "top",)
		labelHard.position = width - 100 , height - indentLabelHeight
		indentLabelHeight += 20
		self.add(labelHard)	

	def info_panzer(self):
		panzerHealth = "100%"		#will be count
		
		width = self.win_width
		height = self.win_height

		labelHealth = cocos.text.Label(("Health: " + panzerHealth), 
			font_size = 12,
			anchor_x = 'center',
			anchor_y = 'center',)
		labelHealth.position = width / 12 , height - 20 
		self.add(labelHealth)

	def button_menu(self):
		button = []
		button.append(cocos.menu.ImageMenuItem("resources/buttons/temp_btn.jpg", self.go_to_main_menu))
		menu = cocos.menu.Menu()
		menu.create_menu(button)
		menu.position = -self.win_width / 2.5, -self.win_height / 2.5
		self.add(menu)

	def go_to_main_menu(self):		
		cocos.director.director.pop()


	#######################################################
	## Observer methods

	def __call__(self, *arg):
		pass

	def update_info(self, info):
		print info

