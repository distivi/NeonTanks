import cocos
from models.static_block import *
from models.bullet import *


class Map(cocos.layer.Layer):	
	def __init__(self,map_path):
		super(Map, self).__init__()		
		resources_from_tmx = cocos.tiles.load(map_path)

		bg_layer = resources_from_tmx['background']
		bg_layer.set_view(0, 0, 520, 520)
		self.add(bg_layer)

		self.block_layer = resources_from_tmx['blocks']
		self.block_layer.set_view(0, 0, 520, 520)
		self.add(self.block_layer)

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










		
