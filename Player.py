"""
	--- Player class ---
	holds all player information
"""

from pygame import Rect
from SpriteData import dead_player

class Player:

	# create player and initialize char vars
	def __init__(self, sprite):
		# starting coords
		self.rect = Rect(96, 352, 32, 32)
		self.sprite = sprite
		self.ms = 4
		self.health = 100

	# if player has no health, change sprite and ms
	def check_dead(self):
		print self.health
		if self.health <= 0:
			self.sprite = dead_player
			self.ms = 0

	# update x and y of player based on input
	def pos_update(self, x_off, y_off, walls, hazards, powerup):
		self.rect.x += x_off
		self.rect.y += y_off

		if self.rect.colliderect(powerup.rect):
			self.health += powerup.p_give_buff()
			powerup.status = 2

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

		for hazard in hazards:
			if (self.rect.colliderect(hazard)):
				if self.health > 0:
					self.health -= 0.5