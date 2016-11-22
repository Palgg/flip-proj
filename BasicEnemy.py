"""
	--- Basic Enemy class ---
	holds all information for creating a basic enemy
"""

from pygame import Rect

class BasicEnemy:

	# create and initialize Skeleton and vars
	def __init__(self, spawn_x, spawn_y, sprite):
		self.rect = Rect(spawn_x, spawn_y, 32, 32)
		self.sprite = sprite
		self.ms = 2

	def move_to_player(self, player_x, player_y):
		if self.rect.x > player_x:
			self.rect.x -= self.ms
		if self.rect.x < player_x:
			self.rect.x += self.ms
		if self.rect.y > player_y:
			self.rect.y -= self.ms
		if self.rect.y < player_y:
			self.rect.y += self.ms