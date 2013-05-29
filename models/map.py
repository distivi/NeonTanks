import cocos

class Map(cocos.layer.ScrollingManager):	
	def __init__(self,map_path):
		super(Map, self).__init__()
		resources_from_tmx = cocos.tiles.load(map_path)

		bg_layer = resources_from_tmx['background']
		self.add(bg_layer)

		block_layer = resources_from_tmx['blocks']
		self.add(block_layer)

		# testing code
		print block_layer
		for rows in block_layer.cells:
			for cell in rows:
				tile = cell.tile
				if tile:				 
					print "-->",cell
					print tile.properties

				#test_property = 'xp' in cell == True
				#print test_property

		cell00 = block_layer.get_cell(0,0)
		cell25 = block_layer.get_cell(25,25)
		
		print cell00
		print cell25
	
		# end testing code



		
