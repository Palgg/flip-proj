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
		self.og_x = spawn_x
		self.og_y = spawn_y
		self.bob_dir = True # True = up, False = down
		self.rect = Rect(self.x, self.y, 32, 32)
		self.status = P_ACTIVE

	# gives a buff to whoever collects it
	# temporary nums for testing
	def p_give_buff(self):
		return 50

	# animation
	def animate(self):
		if self.bob_dir:
			if self.y > self.og_y - 5:
				self.y -= 1
			else:
				self.bob_dir = False
		elif not self.bob_dir:
			if self.y < self.og_y + 5:
				self.y += 1
			else:
				self.bob_dir = True