# -*- coding: utf-8 -*-

import sys
import cocos
from ui.main_menu import MenuScreen
from ui.battle_screen import BattleScreen

def main():
	world_width = 800
	world_height = 600
	cocos.director.director.init(world_width, world_height)
	menuScreen = MenuScreen() #BattleScreen()
	main_scene = cocos.scene.Scene(menuScreen)
	cocos.director.director.run(main_scene)
    
if __name__ == '__main__': main()