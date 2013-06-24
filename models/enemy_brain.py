# from models.TankBase import TankBase
import cocos
import copy

class Point(object):
	def __init__(self, x, y):
		super(Point, self).__init__()
		self.x = x
		self.y = y

	def equal(self, point):
		return True if self.x == point.x and self.y == point.y else False

	def get_distance(self, point):
		dist = ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5
		return dist
		

class WebNode(object):
	def __init__(self, arg):
		super(WebNode, self).__init__()
		self.position = arg['position']
		self.neighboring_nodes = []

	def add_neighbor_node(self, node):
		self.neighboring_nodes.append(node)

class WayWeb(object):	
	def __init__(self):
		super(WayWeb, self).__init__()
		self.web_nodes = []


	def add_node(self,web_node):
		self.web_nodes.append(web_node)
		self.find_neighbors_for_node(web_node)

	def find_neighbors_for_node(self,node):
		position_up = copy.deepcopy(node.position)
		position_up.y += 20

		position_down = copy.deepcopy(node.position)
		position_down.y -= 20

		position_right = copy.deepcopy(node.position)
		position_right.x += 20

		position_left = copy.deepcopy(node.position)
		position_left.x -= 20

		all_neighbors = [position_up, position_left, position_down, position_right]

		for tmp_node in self.web_nodes:
			for tmp_point in all_neighbors:
				if tmp_node.position.equal(tmp_point):
					node.add_neighbor_node(tmp_node)
					tmp_node.add_neighbor_node(node)

class EnemyBrain(object):
	# implement singleton pattern
	def __new__(cls):
		if not hasattr(cls, 'instance'):			
			cls.instance = super(EnemyBrain, cls).__new__(cls)
			cls.instance.way_web = WayWeb()
			cls.instance.player_tank_position = Point(0,0)
			cls.instance.player_base_position = Point(0,0)
			cls.instance.map = None			
		return cls.instance

	def set_map(self,map_):
		self.map = map_
		self.create_way_node()


	def create_way_node(self):
		print self.map
		for x in range(25):
			for y in range(25):
				position = Point((x + 1)*20, (y + 1)*20) 				
				rect = cocos.rect.Rect(position.x - 10,position.y-10,20,20)				
				can_move = self.map.isTankPotentiallyCanMoveInRect(rect)
				if can_move:
					'''
					# uncomment to debug in UI
					test_node = cocos.sprite.Sprite('resources/maps/test_marker.png')
					test_node.position = position.x, position.y
					self.map.add(test_node,z = 100)
					'''
					params = {"position":position}
					node = WebNode(params)
					self.way_web.add_node(node)				


	def set_player_base_position(self,position):
		self.player_base_position = Point(position[0],position[1])

	def get_nearest_position_for_tank(self,tank):
		tank_position = tank.position
		tank_position = Point(tank_position[0],tank_position[1])
		
		distance_to_base = tank_position.get_distance(self.player_base_position)
		distance_to_tank = tank_position.get_distance(self.player_tank_position)		
		min_dist = min(distance_to_base,distance_to_tank)
		if min_dist == distance_to_base:
			return self.player_base_position
		else:
			return self.player_tank_position

	
	def get_direction_for_tank(self, tank):
		print tank.position
		min_position = self.get_nearest_position_for_tank(tank)
		print "min dist ",min_position.x,';',min_position.y
		if min_position.equal(self.player_tank_position):
			print "nearest is tank"
		else:
			print "nearest is base"
		# print "Enemy tank position ",tank.position
		# print "Player tank position ",self.player_tank_position
		# print "PLayer base position ",self.player_base_position
		pass

	####################################################
	##   TANK Observers methods

	def __call__(self, *arg):
	 	#print "observer call ",arg
	 	pass

	def tankMoved(self,tank):		
		self.player_tank_position = Point(tank.position[0],tank.position[1])

		
		