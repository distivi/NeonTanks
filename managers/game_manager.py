#!/usr/bin/env python

import cocos
import pyglet
from random import randint
import xml.etree.ElementTree as ET

from models.map import Map
from models.TankBase import TankBase
from ui.winner_screen import WinnerScreen
from ui.loser_screen import LoserScreen
from models.bonus import Bonus
from models.enemy_brain import EnemyBrain


class GameManager(object):

	def __init__(self,level):
		super(GameManager, self).__init__()	
		
		self.observers = [] # keep observers

        #set game options
		self.level = level	
		self.map = Map('resources/maps/game_map.tmx')
		EnemyBrain()
		EnemyBrain.instance.set_map(self.map)

		self.count_of_available_player_tanks = 2
		
		self.standart_tanks_count = 3
		self.fast_tanks_count = 3
		self.heavy_tanks_count = 3	
		self.count_of_max_enemy_tanks_on_map = 2
		self.spawn_index = 0

		self.tanks = []	
		self.bullets = []	
		self.bonuses = []
		self.add_base()
		self.timeout = 500

		self.enemy_way_nodes = []


	def update(self):	
		self.move_bullets()
		self.move_tanks()
		self.save()
		pass

	def updateSpawnTanks(self):
		self.check_if_need_add_tanks_to_map()


	def check_if_need_add_tanks_to_map(self):
		is_player_tank_on_map = hasattr(self,'player_tank')
		count_of_enemy_tanks_on_map = len(self.tanks) - 1 if is_player_tank_on_map else 0

		if (count_of_enemy_tanks_on_map < self.count_of_max_enemy_tanks_on_map):
			self.add_enemy_tank_to_map()

		if not is_player_tank_on_map:
			self.add_player_tank_to_map()

	def draw_enemy_moved_path(self, way_nodes):
		for node in self.enemy_way_nodes:
			node.kill()
		self.enemy_way_nodes = []

		for node in way_nodes:
			test_node = cocos.sprite.Sprite('resources/maps/test_marker2.png')
			test_node.position = node.position.x, node.position.y
			self.map.add(test_node,z = 100)
			self.enemy_way_nodes.append(test_node)



	def add_enemy_tank_to_map(self):
		tank_type = self.get_available_tank_type()
				
		if tank_type == -1:
			return

		enemy_tank = TankBase(tank_type)
		enemy_tank.attach(self)

		self.tanks.append(enemy_tank)		

		count_of_spawn_point = len(self.map.enemy_spawn_points)

		if count_of_spawn_point > 0:			
			enemy_tank.setPosition(self.map.enemy_spawn_points[self.spawn_index].position)
			if self.spawn_index + 1 == count_of_spawn_point:
				self.spawn_index = 0
			else:
				self.spawn_index += 1
		else:
			enemy_tank.setPosition(20, 200)

		self.map.add(enemy_tank)

	
	def add_player_tank_to_map(self,tankType = 3):
		if self.count_of_available_player_tanks == 0:
			return

		self.count_of_available_player_tanks -= 1

		self.player_tank = TankBase(tankType,isEnemy = False)

		self.player_tank.attach(self)
		self.player_tank.attach(EnemyBrain.instance)

		self.tanks.append(self.player_tank)

		count_of_spawn_point = len(self.map.player_spawn_points)

		if count_of_spawn_point > 0:
			randPointIndex = randint(0,count_of_spawn_point-1)

			self.player_tank.setPosition(self.map.player_spawn_points[randPointIndex].position)
		else:

			self.player_tank.setPosition(self.map.player_spawn_points[randPointIndex].position)


		self.map.add(self.player_tank)

	def add_base(self):
		self.base = cocos.sprite.Sprite('resources/base/base.png')		
		self.base.position = self.map.base_spawn_point.position
		self.map.add(self.base)

		EnemyBrain.instance.set_player_base_position(self.base.position)



	#--------------------base system ---------------

	def is_rect_hit_base(self,rect):
		if self.base:
			base_rect = self.base.get_rect()
			return base_rect.intersect(rect)

	def destroy_base(self):		
		if self.base:
			self.base.kill()			
			self.base = None			
			self.player_loose()		


	######################################################
	## Bonus system

	def add_bonus_to_map(self):
		x = randint(1,24)*20
		y = randint(1,24)*20
		self.bonus = Bonus(randint(0,3),position=(x,y))
		self.bonus.attach(self)
		self.map.add(self.bonus, z = 5)
		self.bonuses.append(self.bonus)
				
	
	def check_if_bonus_need(self):
		if len(self.bonuses) == 0:			
			self.add_bonus_to_map()

	def check_if_tank_get_bonus(self):
		is_player_tank_on_map = hasattr(self,'player_tank')
		if is_player_tank_on_map:
			tank_rect = self.player_tank.get_rect()
			for bonus in self.bonuses:
				bonus_rect = bonus.get_rect()
				if tank_rect.intersects(bonus_rect):
					bonus.tank_took_it()
					self.reward(bonus.get_bonus_type())				
				


	def updateBonus(self):
		if self.timeout <= 0:
			self.check_if_bonus_need()
			self.timeout = 500
		self.check_if_tank_get_bonus()
		self.timeout -= 1

	def removeBonus(self,bonus):
		if bonus in self.bonuses:
			self.bonuses.remove(bonus)
	
	def reward(self,bonusType):
		if bonusType == 0: # make tank more powerfull
			self.upgrade_tank()			
		elif bonusType == 1: # slow down enemy tank
			self.slow_down_all_enemy_tanks()
		else: # destroy all enemy tanks
			self.destroy_all_enemy_tanks()

	def slow_down_all_enemy_tanks(self):
		for tank in self.tanks:
			if tank.isEnemy:
				tank.slowDown()

	def destroy_all_enemy_tanks(self): # destroy all enemy tanks on the map
		for tank in self.tanks:
			if tank.isEnemy:
				self.tankDestroyed(tank)
				tank.destroy()

	def upgrade_tank(self):
		if self.player_tank.getPower() == 3:
			#self.player_tank.setPath("resources/tanks/tank_player_heavy.png")
			for tank in self.tanks:
				if not tank.isEnemy:
					self.player_tank.image = pyglet.resource.image("resources/tanks/neon_tank_player_heavy.png")
					#self.tanks.remove(tank)
					#x,y = self.player_tank.getPosition()
					#direction = self.player_tank.getDirection()
					#self.player_tank.destroy()
					#self.add_player_tank_to_map(4,direction,position=(x,y))
					#self.player_tank.setDirection(direction)
					#self.player_tank.setPosition(position=(x,y))
					
		
	############################################################
	## Bonus system end ##

	def move_bullets(self):
		self.remove_bullets_that_intersects()

		for bullet in self.bullets:
			if not self.is_rect_inside_map(bullet.get_rect()):
				bullet.destroy()
				self.bullets.remove(bullet)
			elif self.is_bullet_hit_some_block(bullet) or self.is_bullet_hit_some_tank(bullet):				
				bullet.destroy()
				self.bullets.remove(bullet)
			elif self.is_rect_hit_base(bullet.get_rect()):				
				bullet.destroy()
				self.bullets.remove(bullet)
				self.destroy_base()
			elif not bullet.isMoving:
				bullet.move()
			

	def move_tanks(self):
		for tank in self.tanks:			
			if not tank.isMoving:
				if self.is_rect_inside_map(tank.get_next_step_rect()):
					if not self.is_tank_will_hit_some_tank(tank):
						if not self.is_tank_will_hit_some_block(tank):
							if not self.is_rect_hit_base(tank.get_next_step_rect()):
								tank.move()
							
						
			


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
		return not self.map.isBulletCanMove(bullet)

	def is_bullet_hit_some_tank(self,bullet):
		is_bullet_hit_tank = False
		for tank in self.tanks:
			if tank.isEnemy != bullet.isEnemy:
				tank_rect = tank.get_rect()
				bullet_rect = bullet.get_rect()
				if tank_rect.intersects(bullet_rect):
					tank.damage(bullet.power)
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
		
		while True:
			tank_type = randint(0,2)
			if type_list[tank_type] > 0:
				if tank_type == 0:
					self.standart_tanks_count -= 1
				elif tank_type == 1:
					self.fast_tanks_count -= 1
				elif tank_type == 2:
					self.heavy_tanks_count -= 1					
				return tank_type



	####################################################
	## Observers methods

	def attach(self,observer): #attach observer
		self.observers.append(observer)
		self.update_info_for_observers()

	def update_info_for_observers(self):
		for observer in self.observers:
			if hasattr(observer,'update_info'):
				info = {}				
				info["heavy_tanks_count"] = self.heavy_tanks_count
				info["standart_tanks_count"] = self.standart_tanks_count
				info["fast_tanks_count"] = self.fast_tanks_count
				info["count_of_available_player_tanks"] = self.count_of_available_player_tanks
				observer.update_info(info)


	####################################################
	##   TANK Observers methods

	def __call__(self, *arg):
	 	##print"observer call ",arg
	 	pass

	def tankShoot(self,bullet):	
		self.bullets.append(bullet)
		self.map.add(bullet,z=2)

	def tankDestroyed(self,tank):
		if tank in self.tanks:

			self.tanks.remove(tank)
			self.update_info_for_observers()

			if tank == self.player_tank:
				del(self.player_tank)
				if self.count_of_available_player_tanks == 0:
					self.player_loose()			

			if len(self.tanks) == 1 and self.standart_tanks_count == 0 and self.fast_tanks_count == 0 and self.heavy_tanks_count == 0:
				self.player_win()

	######################################################
	###  SAVE & LOAD

	def save(self):		
		root = ET.Element('game')
		root.attrib = {'level':str(self.level)}

		for tank in self.tanks:
			tank.getXmlWithParrentNode(root)
			
		for bullet in self.bullets:
			bulletNode = bullet.getXmlWithParrentNode(root)

		self.map.getXmlWithParrentNode(root)

		xmlData = ET.tostring(root, encoding="utf-8")

		xmlFile = open('resources/saves/test.xml','wb')
		xmlFile.write(xmlData)
		xmlFile.close()

	def load(self):
		pass


	######################################################
	###  GAME ENDED

	def player_win(self):		
		winner = cocos.scene.Scene(WinnerScreen())
		cocos.director.director.push(winner)

	def player_loose(self):
		loser = cocos.scene.Scene(LoserScreen())
		cocos.director.director.push(loser)




		




		


		
