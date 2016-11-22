"""
	--- Player class ---
	holds all player information
"""

from pygame import Rect

class Player:

	# create player and initialize char vars
	def __init__(self, sprite):
		# starting coords
		self.rect = Rect(96, 352, 32, 32)
		self.sprite = sprite
		self.ms = 4

	# update x and y of player based on input
	def pos_update(self, x_off, y_off, walls):
		self.rect.x += x_off
		self.rect.y += y_off

		for wall in walls:
			if (self.rect.colliderect(wall)):
				if x_off > 0: # moving right, hit left side of a wall
					self.rect.right = wall.left
				if x_off < 0: # moving left, hit right side of a wall
					self.rect.left = wall.right
				if y_off > 0: # moving down, hit top side of a wall
					self.rect.bottom = wall.top
				if y_off < 0: # moving up, hit bottom side of a wall
					self.rect.top = wall.bottom