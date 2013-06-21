# -*- coding: utf-8 -*-

import cocos

class BaseScreen(cocos.layer.Layer):	
	def __init__(self, bg_image = "resources/background/background_image.png"):
		super(BaseScreen, self).__init__()
		self.win_width, self.win_height = cocos.director.director.get_window_size()	
		self.add_background_image(bg_image)

	def add_background_image(self, image_path):
		bg_layer =	cocos.sprite.Sprite(image_path, position = (self.win_width / 2, self.win_height / 2))
		self.add(bg_layer,z=-100)	
