# -*- coding: utf-8 -*-

import cocos
from ui.base_screen import BaseScreen
from ui.game_menu import *
from ui.main_menu import *
from models.static_block import *
from models.brick_block import *
from models.map import Map
from managers.game_manager import GameManager
from models.bonus import Bonus
from ui.handler_key import *


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
		self.game_manager.updateBonus()
		

	def create_layer(self):		
		label = cocos.text.Label("Battle Screen",
			font_size = 16,
			anchor_x = 'center',
			anchor_y = 'center')		
		label.position = self.win_width / 2, self.win_height - 20
		self.add(label)

		map_border = cocos.sprite.Sprite('resources/background/map_border.png')
		map_border.position = self.win_width / 2, self.win_height / 2
		self.add(map_border)


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
				tank_direction = 1

			elif UP in self.chars_pressed:			
				tank_direction = 0

			elif DOWN in self.chars_pressed:			
				tank_direction = 2

			self.game_manager.player_tank.user_select_direction(tank_direction)
			

	def on_key_press(self, key, modifiers):
		super(BattleScreen,self).on_key_press(key,modifiers)
		if SPACE == key: 				
			self.game_manager.player_tank.shoot()



	def info_enemeis(self):
		easyEnemy = 6	#will be count
		normalEnemy = 4 #will be count
		hardEnemy = 2  #will be count
		width = self.win_width
		height = self.win_height
		indentSpriteWidth = self.win_width - 80
		indentSpriteHeight = self.win_height - 60
		indentLabelWidth = 100
		indentLabelHeight = 20

		labelEnemy = cocos.text.Label("Enemy: ", 
			font_size = 12,
			anchor_x = 'left',
			anchor_y = 'top',)
		labelEnemy.position = width - indentLabelWidth , height - indentLabelHeight
		indentLabelHeight += 35 
		self.add(labelEnemy)

		#info easy panzers
		spriteEasy = cocos.sprite.Sprite("resources/tanks/neon_tank_speed.png")
		spriteEasy.position = indentSpriteWidth, indentSpriteHeight
		self.labelFast = cocos.text.Label((" " + easyEnemy.__str__()), 
			font_size = 11,
			anchor_x = 'left',
			anchor_y = 'top',)
		self.labelFast.position = width - (indentLabelWidth - 40) , height - indentLabelHeight  
		indentLabelHeight += 50
		indentSpriteHeight -= 50
		self.add(self.labelFast)
		self.add(spriteEasy)

		#info normal panzers
		spriteNormal = cocos.sprite.Sprite("resources/tanks/neon_tank_standart.png")
		spriteNormal.position = indentSpriteWidth, indentSpriteHeight 		
		self.labelNormal = cocos.text.Label((" " + normalEnemy.__str__()), 
			font_size = 11,
			anchor_x = 'left',
			anchor_y = 'top',)
		self.labelNormal.position = width - (indentLabelWidth - 40) , height - indentLabelHeight
		indentLabelHeight += 50
		indentSpriteHeight -= 50
		self.add(self.labelNormal)
		self.add(spriteNormal)

		#info hard panzers
		spriteHard = cocos.sprite.Sprite("resources/tanks/neon_tank_heavy.png")
		spriteHard.position = indentSpriteWidth, indentSpriteHeight 		
		self.labelHard = cocos.text.Label((" " + hardEnemy.__str__()), 
			font_size = 11,
			anchor_x = "left",
			anchor_y = "top",)
		self.labelHard.position = width - (indentLabelWidth - 40) , height - indentLabelHeight
		indentLabelHeight += 50
		self.add(self.labelHard)
		self.add(spriteHard)

	def info_panzer(self):
		panzerHealth = 3		#will be count
		
		width = self.win_width - 80
		height = self.win_height / 10

		self.labelHealth = cocos.text.Label(("Health: " + panzerHealth.__str__()), 
			font_size = 12,
			anchor_x = 'center',
			anchor_y = 'center',)
		self.labelHealth.position = width , height
		self.add(self.labelHealth)

	def button_menu(self):
		button = []
		button.append(cocos.menu.ImageMenuItem("resources/buttons/test_menu_button.png", self.go_to_game_menu))
		menu = cocos.menu.Menu()
		menu.create_menu(button)
		menu.position = -self.win_width / 2.5, self.win_height / 2.5
		self.add(menu)

	def go_to_game_menu(self):		
		self.unschedule(self.update)
		self.game_menu = GameMenu()
		self.game_menu.attach(self)
		self.add(self.game_menu, z = 1)

	def resume_game_menu(self):
		self.remove(self.game_menu)
		self.schedule_interval(self.update, 0.01)

	#######################################################
	## Observer methods

	def __call__(self, *arg):
		pass

	def update_info(self, info):
		print(info)
		# self.labelNormal.setText("     " + info["standart_tanks_count"].__str__())
		# self.labelHard.setText(  "     " + info["heavy_tanks_count"].__str__())
		# self.labelFast.setText(  "     " + info["fast_tanks_count"].__str__())
		# self.labelHealth.setText("Lives: " + info["count_of_available_player_tanks"].__str__())
		

		
