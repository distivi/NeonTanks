#!/usr/bin/env python

import cocos
import pyglet
from random import randint

from models.map import Map
from models.TankBase import TankBase


class GameManager(object):

	def __init__(self,level):
		super(GameManager, self).__init__()	
		self.level = level	
		self.map = Map('resources/maps/game_map.tmx')
		
		self.count_of_available_player_tanks = 5
		
		self.count_of_available_standart_tanks = 5
		self.count_of_available_fast_tanks = 5
		self.count_of_available_heavy_tanks = 5		
		self.count_of_max_enemy_tanks_on_map = 5	

		self.tanks = []	
		self.bullets = []	


	def update(self):	
		self.move_bullets()
		self.move_tanks()
		pass

	def updateSpawnTanks(self):
		self.check_if_need_add_tanks_to_map()


	def check_if_need_add_tanks_to_map(self):
		if (len(self.tanks) < self.count_of_max_enemy_tanks_on_map):
			self.add_enemy_tank_to_map()

		if not hasattr(self,'player_tank'):
			self.add_player_tank_to_map()



	def add_enemy_tank_to_map(self):
		enemy_tank = TankBase(1)
		enemy_tank.attach(self)

		self.tanks.append(enemy_tank)		

		count_of_spawn_point = len(self.map.enemy_spawn_points)

		if count_of_spawn_point > 0:
			randPointIndex = randint(0,count_of_spawn_point-1)
			enemy_tank.setPosition(self.map.enemy_spawn_points[randPointIndex].position)
		else:
			enemy_tank.setPosition(20, 200)

		self.map.add(enemy_tank)

	
	def add_player_tank_to_map(self):
		self.player_tank = TankBase(3)
		self.player_tank.attach(self)
		self.tanks.append(self.player_tank)

		count_of_spawn_point = len(self.map.player_spawn_points)

		if count_of_spawn_point > 0:
			randPointIndex = randint(0,count_of_spawn_point-1)
			self.player_tank.setPosition(self.map.player_spawn_points[randPointIndex].position)
		else:
			self.player_tank.setPosition(self.map.player_spawn_points[randPointIndex].position)

		self.map.add(self.player_tank)


	def move_bullets(self):
		for bullet in self.bullets:
			if (self.is_rect_out_of_map(bullet.get_rect())):
				bullet.destroy()
				self.bullets.remove(bullet)
			elif not bullet.isMoving:
				bullet.move()

	def move_tanks(self):
		for tank in self.tanks:			
			if not tank.isMoving and not self.is_rect_out_of_map(tank.get_next_step_rect()):				
				tank.move()
			


	###################################################
	##  HELPERS

	def is_rect_out_of_map(self,rect):		
		cells = self.map.block_layer.get_in_region(rect.x,
			rect.y,
			rect.x + rect.width,
			rect.y + rect.height,)
		return (len(cells) == 0)	



	####################################################
	##   TANK Observers methods

	def __call__(self, *arg):
	 	#print "observer call ",arg
	 	pass

	def tankShoot(self,bullet):	
		self.bullets.append(bullet)
		self.map.add(bullet,z=2)

	def tankDestroyed(self,tank):
		if tank in self.tanks:
			self.tanks.remove(tank)
		




		


		
