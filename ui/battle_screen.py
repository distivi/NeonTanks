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

		
