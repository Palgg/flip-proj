"""
	--- Powerup class ---
	defines behavior and types of powerups
"""

from SpriteData import powerup

class Powerup:

	def __init__(self, spawn_x, spawn_y):
		self.sprite = powerup
		self.x = spawn_x
		self.y = spawn_y - 5
