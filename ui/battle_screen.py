# -*- coding: utf-8 -*-

import cocos
from base_screen import BaseScreen
from main_menu import *
from models.static_block import *
from models.brick_block import *
from models.map import Map


class BattleScreen(BaseScreen):	
	def __init__(self):
		super(BattleScreen, self).__init__()		
		self.create_layer()		
		self.create_map()
		self.info_enemeis()
		self.info_panzer()
		self.button_menu()

	def create_layer(self):		
		label = cocos.text.Label("Battle Screen",
			font_size = 16,
			anchor_x = 'center',
			anchor_y = 'center')		
		label.position = self.win_width / 2, self.win_height - 20
		self.add(label)
	
	def create_map(self):
		battle_map = Map('resources/maps/test_map.tmx')		
		self.add(battle_map)

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
		menuScreen = cocos.scene.Scene(MenuScreen())
		cocos.director.director.pop(menuScreen)
