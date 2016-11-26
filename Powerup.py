"""
	--- Powerup class ---
	defines behavior and types of powerups
"""

from pygame import Rect
from SpriteData import powerup

P_ACTIVE = 0
P_INACTIVE = 1

class Powerup:

	def __init__(self, spawn_x, spawn_y):
		self.sprite = powerup
		self.x = spawn_x
		self.y = spawn_y
		self.rect = Rect(self.x, self.y, 32, 32)
		self.status = P_ACTIVE

	# gives a buff to whoever collects it
	# temporary nums for testing
	def p_give_buff(self):
		return 50