import cocos



class Map(cocos.layer.ScrollingManager):	
	def __init__(self,map_path):
		super(Map, self).__init__()
		resources_from_tmx = cocos.tiles.load(map_path)

		bg_layer = resources_from_tmx['background']
		self.add(bg_layer)

		self.block_layer = resources_from_tmx['blocks']
		self.add(self.block_layer)

		self.blocks = []


		# testing code
		print self.block_layer
		for rows in self.block_layer.cells:
			for cell in rows:
				tile = cell.tile				
				if tile:		
					self.blocks.append(cell)										
					#print tile.properties

		#cell00 = self.block_layer.get_cell(0,0)
		
		self.schedule_interval(self.testHidingAllBlocksFromMap, 0.01)
		
		

	def testHidingAllBlocksFromMap(self, dt):
		# test method
		if len(self.blocks) > 0:			
			cell = self.blocks[0]
			#print cell.position
			#print cell.position[0]/20," === ",cell.position[1]/20

			self.block_layer.set_cell_opacity(cell.position[0] / 20, cell.position[1] / 20, 0.5)
		  	self.blocks.remove(cell)
			
		

	def deleteCellAtPosition(self,position):		
		# will be dinamic removing block at position
		pass







		
