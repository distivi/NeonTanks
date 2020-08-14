import cocos
from ui.base_screen import BaseScreen
from models.TankBase import TankBase
from ui.handler_key import HandlerKey

ESC = 65307
LEFT = 65361
UP = 65362
RIGHT = 65363
DOWN = 65364

class TankCrashScreen(HandlerKey):
	#is_event_handler = True	
	def __init__(self):
		super(TankCrashScreen, self).__init__()		
		self.create_layer()		
		self.create_tank()
		self.schedule(self.update)

	def create_layer(self):		
		label = cocos.text.Label("Tank test screen",
			font_size = 16,
			anchor_x = 'center',
			anchor_y = 'center')		
		label.position = self.win_width / 2, self.win_height - 20
		self.add(label)

	def create_tank(self):
		self.tank = TankBase(0)
		self.add(self.tank)

	def update(self,obj):
		#keys = HandlerKey()
		if LEFT in self.chars_pressed:
			self.tank.move(3)
		elif RIGHT in self.chars_pressed:
			self.tank.move(2)
		elif UP in self.chars_pressed:
			self.tank.move(0)
		elif DOWN in self.chars_pressed:
			self.tank.move(1)
		#self.tank.move()