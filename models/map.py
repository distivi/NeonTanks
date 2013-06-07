import cocos
from models.static_block import *
from models.bullet import *
import xml.etree.ElementTree as ET


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

		self.blocks = []
		self.parse_blocks_layer()

		self.enemy_spawn_points = []
		self.player_spawn_points = []
		self.parse_object_layer(map_path)

		

	def parse_object_layer(self,file_path):
		etree = ET.parse(file_path).getroot()
		for node in etree.findall('objectgroup'):
			for spawn_object in node.findall('object'):
				spawn_point = SpawnPoint(spawn_object)
				if (spawn_point.isPLayerSpawnPoint == True):
					self.player_spawn_points.append(spawn_point)
				else:
					self.enemy_spawn_points.append(spawn_point)

				


	def parse_blocks_layer(self):
		for rows in self.block_layer.cells:
			for cell in rows:				
				if cell.tile:					
					self.blocks.append(BaseStaticBlock(cell))

	
	def testHidingAllBlocksFromMap(self, dt):
		# test method
		if len(self.blocks) > 0:			
			block = self.blocks[0]			
			self.block_layer.set_cell_opacity(block.cell.position[0] / 20, block.cell.position[1] / 20, 0.5)
		  	self.blocks.remove(block)


	def removeBlock(self, block):
		self.block_layer.set_cell_opacity(block.cell.position[0] / 20, block.cell.position[1] / 20, 0.5)
		self.blocks.remove(block)
		

	def isTankCanMoveOnPosition(self, position):
		cell = self.block_layer.get_at_pixel(position[0],position[1])
		if cell:
			for block in self.blocks:				
				if cell == block.cell:
					return False
		return True

	def isBulletCanMoveOnPosition(self, position):
		cell = self.block_layer.get_at_pixel(position[0]+2,position[1]+2)
		if cell:
			for block in self.blocks:			
				if cell == block.cell:
					return block.can_move_bullet
		return True

	def isTankCanMoveInRect(self,rect):
		cells = self.block_layer.get_in_region(rect.x,rect.y,rect.topright[0],rect.topright[1])
		for cell in cells:
			for block in self.blocks:				
				if cell == block.cell:
					return False
		return True

	
	def isBulletCanMove(self,bullet):
		bullet_rect = bullet.get_rect()
		cells = self.block_layer.get_in_region(bullet_rect.x,bullet_rect.y,bullet_rect.topright[0],bullet_rect.topright[1])		
		isBulletCanMove = True
		for cell in cells:
			for block in self.blocks:				
				if cell == block.cell and block.can_move_bullet == False:					
					isBulletCanMove = False
					self.destroyBlocksWithBullet(block,bullet)					

		return isBulletCanMove

		

	def destroyBlocksWithBullet(self,block,bullet):
		if block.hp <= bullet.power:
			self.removeBlock(block)

	def getXmlWithParrentNode(self,root):
		mapNode = ET.SubElement(root,'map')		
		for block in self.blocks:
			block.getInfo()
		#mapNode.attrib = {'power':str(self.power),'position':str(self.position),'direction':str(self.direction),'hp':str(self.hp)}
		return mapNode

		

class SpawnPoint(object):	
	def __init__(self, node):
		super(SpawnPoint, self).__init__()

		self.isPLayerSpawnPoint = (node.get('name') == 'spawn_player_point')					
		self.x = int(node.get('x'))
		self.y = 520 - int(node.get('y'))
		self.position = self.x,self.y