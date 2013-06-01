import cocos

class BaseStaticBlock(object):	
	def __init__(self,cell):
		super(BaseStaticBlock, self).__init__()		
		self.cell = cell		
		self.can_move_bullet = cell.tile.properties["can move bullet"]
		self.xp = cell.tile.properties["hp"]


		
		
		
