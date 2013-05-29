import cocos



class Map(cocos.layer.ScrollingManager):	
	def __init__(self,map_path):
		super(Map, self).__init__()
		resources_from_tmx = cocos.tiles.load(map_path)

		bg_layer = resources_from_tmx['background']
		self.add(bg_layer)

		self.block_layer = resources_from_tmx['blocks']
		self.add(self.block_layer)


		print self.block_layer.properties

		# testing code
		print self.block_layer
		for rows in self.block_layer.cells:
			for cell in rows:
				tile = cell.tile
				if tile:				 
					print "-->",cell
					print tile.properties

		cell00 = self.block_layer.get_cell(0,0)
		cell25 = self.block_layer.get_cell(25,25)
		
		print cell00
		print cell25

		self.block_x = 0
		self.block_y = 0

		self.schedule_interval(self.update, 1)
		
		

	def update(self, dt, *args, **kwargs):   
		self.deleteCellAtPosition((self.block_x, self.block_y)) 

		self.block_y += 1
		if self.block_y == 25:
			self.unschedule(self.update)
			
		

	def deleteCellAtPosition(self,position):		
		cell = self.block_layer.get_cell(position[0],position[1])				
		for rows in self.block_layer.cells:
			if cell in rows:
				print "remove ",cell				
				rows.remove(cell)				
				self.update_blocks()
				return

	def update_blocks(self):
		self.remove(self.block_layer)
		self.add(self.block_layer)




		
