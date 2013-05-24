# -*- coding: utf-8 -*-

import sys
import cocos
from base_screen import BaseScreen


class MenuScreen(BaseScreen):	
	def __init__(self):
		super(MenuScreen, self).__init__()		
		self.create_layer()
		

	def create_layer(self):		
		label = cocos.text.Label("Main Menu",
			font_size = 16,
			anchor_x = 'center',
			anchor_y = 'center')		
		label.position = self.win_width / 2, self.win_height - 20
		self.add(label)

	

		
				
