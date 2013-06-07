import cocos

class BaseStaticBlock(object):	
	def __init__(self,cell):
		super(BaseStaticBlock, self).__init__()		
		self.cell = cell		
		self.can_move_bullet = cell.tile.properties["can move bullet"] == 'True'
		self.hp = cell.tile.properties["hp"]

	def getInfo(self):
		print self
		print self.cell
		print self.cell.position
		print self.hp





		
		
		
