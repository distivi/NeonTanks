#!/usr/bin/env python

import cocos
import pyglet

from models.map import Map
from models.TankBase import TankBase


class GameManager(object):

	def __init__(self,level):
		super(GameManager, self).__init__()	
		self.level = level	
		self.map = Map('resources/maps/test_map.tmx')
		self.createTanks()
		self.createPlayerTank()
		self.add_player_tank_to_map()

		self.counter = 0


	def update(self):
		# game enginee		
		self.counter += 1
		if self.counter == 200:
			print "update in gameManger"
			self.add_tank_to_map()			


	def createTanks(self):
		self.tanks = []		
		self.count_of_standart_tanks = self.count_of_standart_tanks_for_level(self.level)
		self.count_of_fast_tanks = self.count_of_fast_tanks_for_level(self.level)
		self.count_of_heavy_tanks = self.count_of_heavy_tanks_for_level(self.level)

		for i in range(0,self.count_of_standart_tanks):
			tmpTank = TankBase(0)
			self.tanks.append(tmpTank)

		for i in range(0,self.count_of_fast_tanks):
			tmpTank = TankBase(1)
			self.tanks.append(tmpTank)

		for i in range(0,self.count_of_heavy_tanks):
			tmpTank = TankBase(2)
			self.tanks.append(tmpTank)	

	def createPlayerTank(self):
		self.player_tank = TankBase(3)
		self.player_tank.speed = 3
		self.tanks.append(self.player_tank)


	# helpers

	def count_of_standart_tanks_for_level(self,level):
		return level * 5

	def count_of_fast_tanks_for_level(self,level):
		return level * 3

	def count_of_heavy_tanks_for_level(self,level):
		return level * 3

	def add_tank_to_map(self):
		tank = self.tanks[0]
		tank.position = 100, 200	
		self.map.add(tank)

	def add_player_tank_to_map(self):
		self.player_tank.position = 100, 100	
		self.map.add(self.player_tank)


		
