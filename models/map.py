import cocos
from models.static_block import *
from models.bullet import *
from xml.etree import ElementTree


class Map(cocos.layer.Layer):	
	def __init__(self,map_path):
		super(Map, self).__init__()		
		resources_from_tmx = cocos.tiles.load(map_path)

		bg_layer = resources_from_tmx['bg']		
		bg_layer.set_view(0, 0, 520, 520)
		self.add(bg_layer)

		self.block_layer = resources_from_tmx['test_map']
		self.block_layer.set_view(0, 0, 520, 520)
		self.add(self.block_layer)

		self.spawn_points = []
		self.parse_object_layer(map_path)




		self.blocks = []

		# testing code
		print self.block_layer
		for rows in self.block_layer.cells:
			for cell in rows:
				tile = cell.tile
				if tile:
					#print tile.properties		
					tempBlock = BaseStaticBlock(cell)
					self.blocks.append(tempBlock)
			
		#self.schedule_interval(self.testHidingAllBlocksFromMap, 0.01)

	def parse_object_layer(self,file_path):
		etree = ElementTree.parse(file_path).getroot()
		for node in etree.findall('objectgroup'):
			for spawn_object in node.findall('object'):
				self.spawn_points.append(SpawnPoint(spawn_object))

            #self.objectgroups.append(TiledObjectGroup(self, node))
	
	def testHidingAllBlocksFromMap(self, dt):
		# test method
		if len(self.blocks) > 0:			
			block = self.blocks[0]			
			self.block_layer.set_cell_opacity(block.cell.position[0] / 20, block.cell.position[1] / 20, 0.5)
		  	self.blocks.remove(block)


	def removeBlock(self, block):
		self.block_layer.set_cell_opacity(block.cell.position[0] / 20, block.cell.position[1] / 20, 0.5)
		self.blocks.remove(block)
		

	def deleteCellAtPosition(self,position):		
		# will be dinamic removing block at position
		finding_cell = self.block_layer.get_at_pixel(position[0],position[1])
		print finding_cell
		pass

	def isTankCanMoveOnPosition(self, position):
		cell = self.block_layer.get_at_pixel(position[0],position[1])
		for block in self.blocks:
			if cell == block.cell:
				return False
		return True

	def isBulletCanMoveOnPosition(self, position):
		cell = self.block_layer.get_at_pixel(position[0],position[1])
		for block in self.blocks:
			if cell == block.cell:
				return block.can_move_bullet				
		return True

	def destroyBlocksWithBulletRect(self,bullet):
		bullet_rect = bullet.get_rect() 
		#rect.Rect(x, y, self.width, self.height)
		cells = self.block_layer.get_in_region(bullet_rect.x,
			bullet_rect.y,
			bullet_rect.x + bullet_rect.width,
			bullet_rect.y + bullet_rect.height)
		print cells
		# remove blocks


class SpawnPoint(object):	
	def __init__(self, node):
		super(SpawnPoint, self).__init__()

		print node

		self.name = node.get('name')
		self.x = node.get('x')
		self.y = node.get('y')
		self.position = self.x,self.y

		print self.name,"+++",self.position


		










		
