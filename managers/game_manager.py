#!/usr/bin/env python

import cocos
import pyglet
from random import randint

from models.map import Map
from models.TankBase import TankBase


class GameManager(object):

	def __init__(self,level):
		super(GameManager, self).__init__()	
		self.observers = [] # keep observers

		self.level = level	
		self.map = Map('resources/maps/game_map.tmx')
		
		self.count_of_available_player_tanks = 5
		
		self.standart_tanks_count = 1
		self.fast_tanks_count = 1
		self.heavy_tanks_count = 1		
		self.count_of_max_enemy_tanks_on_map = 3

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
		tank_type = self.get_available_tank_type()
		if tank_type == -1:
			return

		enemy_tank = TankBase(self.get_available_tank_type())
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
		if self.count_of_available_player_tanks == 0:
			return

		self.count_of_available_player_tanks -= 1
		self.player_tank = TankBase(3,isEnemy = False)
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
		self.remove_bullets_that_intersects()

		for bullet in self.bullets:
			if not self.is_rect_inside_map(bullet.get_rect()):
				bullet.destroy()
				self.bullets.remove(bullet)			
			elif self.is_bullet_hit_some_block(bullet) or self.is_bullet_hit_some_tank(bullet):				
				bullet.destroy()
				self.bullets.remove(bullet)

			elif not bullet.isMoving:
				bullet.move()
			

	def move_tanks(self):
		for tank in self.tanks:			
			if not tank.isMoving:
				if self.is_rect_inside_map(tank.get_next_step_rect()):
					if not self.is_tank_will_hit_some_tank(tank):
						if not self.is_tank_will_hit_some_block(tank):
							tank.move()
							pass
						
			


	###################################################
	##  HELPERS

	def is_rect_inside_map(self,rect):
		mapRect = cocos.rect.Rect(0,0,520,520)
		bottom_left_corner_inside = mapRect.contains(rect.x,rect.y)
		top_right_corner_inside = mapRect.contains(rect.topright[0],rect.topright[1])
		return bottom_left_corner_inside and top_right_corner_inside


	def is_tank_will_hit_some_tank(self,tank):
		tank_rect = tank.get_next_step_rect()
		for tmp_tank in self.tanks:
			if tmp_tank != tank:
				tmp_tank_rect = tmp_tank.get_rect()
				if tank_rect.intersect(tmp_tank_rect):
					return True
		return False

	def is_tank_will_hit_some_block(self,tank):
		rect = tank.get_next_step_rect()
		rect.x += 1
		rect.y += 1
		rect.width -= 2
		rect.height -= 2
		tank_position = rect.x + rect.width/2, rect.y + rect.height/2 
		return not self.map.isTankCanMoveInRect(rect)

	def is_bullet_hit_some_block(self,bullet):		
		return not self.map.isBulletCanMoveInRect(bullet.get_rect())

	def is_bullet_hit_some_tank(self,bullet):
		is_bullet_hit_tank = False
		for tank in self.tanks:
			if tank.isEnemy != bullet.isEnemy:
				tank_rect = tank.get_rect()
				bullet_rect = bullet.get_rect()
				if tank_rect.intersects(bullet_rect):
					tank.damage(1000)
					if is_bullet_hit_tank == False:
						is_bullet_hit_tank = True

		return is_bullet_hit_tank

	def remove_bullets_that_intersects(self):
		for bullet1 in self.bullets:
			for bullet2 in self.bullets:
				if bullet1 != bullet2:
					bullet1_rect = bullet1.get_rect()
					bullet2_rect = bullet2.get_rect()
					if bullet1_rect.intersects(bullet2_rect):
						bullet1.destroy()
						bullet2.destroy()
						self.bullets.remove(bullet1)
						self.bullets.remove(bullet2)

	def get_available_tank_type(self):		
		type_list = [self.standart_tanks_count,self.fast_tanks_count,self.heavy_tanks_count]
		if (type_list[0] + type_list[1] + type_list[2] == 0):
			return -1
		return 1
		#  need check this code
		# while True:
		# 	tank_type = randint(0,2)
		# 	if type_list[tank_type] > 0:
		# 		if tank_type == 0:
		# 			self.standart_tanks_count -= 1
		# 		elif tank_type == 1:
		# 			self.fast_tanks_count -= 1
		# 		elif tank_type == 2:
		# 			self.heavy_tanks_count -= 1					
		# 		return tank_type



	####################################################
	## Observers methods

	def attach(self,observer): #attach observer
		self.observers.append(observer)

	def update_info_for_observers(self):
		for observer in self.observers:
			if hasattr(observer,'update_info'):
				info = {"tanks":10}
				observer.update_info(info)


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
			if tank == self.player_tank and self.count_of_available_player_tanks == 0:
				self.player_win()

			self.tanks.remove(tank)
			self.update_info_for_observers()

			if len(self.tanks) == 0 and self.standart_tanks_count == 0 and self.fast_tanks_count == 0 and self.heavy_tanks_count == 0:
				self.player_win()




	######################################################
	###  GAME ENDED

	def player_win(self):
		print "\n\n********************************\n YOU WIN \n ***********************"

	def player_loose(self):
		print "\n\n********************************\n YOU LOOSE \n ***********************"


		




		


		
