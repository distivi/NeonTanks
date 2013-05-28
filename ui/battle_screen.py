# -*- coding: utf-8 -*-

import cocos
from base_screen import BaseScreen
from models.static_block import *
from models.brick_block import *


class BattleScreen(BaseScreen):	
	def __init__(self):
		super(BattleScreen, self).__init__()		
		self.create_layer()		
		self.create_map()
		self.info_enemeis()
		self.info_panzer()

	def create_layer(self):		
		label = cocos.text.Label("Battle Screen",
			font_size = 16,
			anchor_x = 'center',
			anchor_y = 'center')		
		label.position = self.win_width / 2, self.win_height - 20
		self.add(label)
	
	def create_map(self):
		scroller = cocos.layer.ScrollingManager()
		resources_from_tmx = cocos.tiles.load('resources/maps/test_map.tmx')
		bg_layer = resources_from_tmx['blocks']
		block_layer = resources_from_tmx['background']
		scroller.add(bg_layer)
		scroller.add(block_layer)
		self.add(scroller)

	def info_enemeis(self):
		easyEnemy = 6	#will be count
		normalEnemy = 4 #will be count
		hardEnemy = 2   #will be count
		width = self.win_width
		height = self.win_height

		labelEnemy = cocos.text.Label("Enemy: ", 
			font_size = 12,
			anchor_x = 'center',
			anchor_y = 'center',)
		labelEnemy.position = width - 45 , height - 20 
		self.add(labelEnemy)

		laelEasy = cocos.text.Label(("Easy: " + easyEnemy.__str__()), 
			font_size = 11,
			anchor_x = 'center',
			anchor_y = 'center',)
		laelEasy.position = width - 45 , height - 40 
		self.add(laelEasy)

		labelNormal = cocos.text.Label(("Normal: " + normalEnemy.__str__()), 
			font_size = 11,
			anchor_x = 'center',
			anchor_y = 'center',)
		labelNormal.position = width - 45 , height - 56
		self.add(labelNormal)

		labelHard = cocos.text.Label(("Hard: " + hardEnemy.__str__()), 
			font_size = 11,
			anchor_x = 'center',
			anchor_y = 'center',)
		labelHard.position = width - 45 , height - 72
		self.add(labelHard)

	def info_panzer(self):
		panzerHealth = "100%"		#will be count
		panzer_lvl = "img_star"		#will be count
		
		width = self.win_width
		height = self.win_height

		labelHealth = cocos.text.Label(("Health: " + panzerHealth), 
			font_size = 12,
			anchor_x = 'center',
			anchor_y = 'center',)
		labelHealth.position = width / 11 , height - 20 
		self.add(labelHealth)

		labelLvl = cocos.text.Label(("Level: " + panzer_lvl), 
			font_size = 11,
			anchor_x = 'center',
			anchor_y = 'center',)
		labelLvl.position = width / 11 , height - 35 
		self.add(labelLvl)