import cocos
from base_screen import BaseScreen
from models.TankBase import TankBase

class TankCrashScreen(BaseScreen):	
	def __init__(self):
		super(TankCrashScreen, self).__init__()		
		self.create_layer()		
		self.create_tank()
		#self.tank = TankBase(0)
		self.schedule(self.update)

	def create_layer(self):		
		label = cocos.text.Label("Tank test screen",
			font_size = 16,
			anchor_x = 'center',
			anchor_y = 'center')		
		label.position = self.win_width / 2, self.win_height - 20
		self.add(label)

	def create_tank(self):
		self.add(TankBase(0))

	def update(self,obj):
		pass
