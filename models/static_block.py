import cocos

class BaseStaticBlock():	
	def __init__(self,cell):
		super(BaseStaticBlock, self).__init__()
		print "create BaseStaticBlock"
		self.cell = cell		
		self.can_move_bullet = cell.tile.properties["can move bullet"]
		self.xp = cell.tile.properties["xp"]

		print self.cell
		print self.can_move_bullet
		print self.xp

		
		
		
