# -*- coding: utf-8 -*-

import cocos

class BaseScreen(cocos.layer.ColorLayer):	
	def __init__(self):
		super(BaseScreen, self).__init__(200,200,200,200)
		self.win_width, self.win_height = cocos.director.director.get_window_size()		
