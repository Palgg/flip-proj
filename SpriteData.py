"""
	--- SpriteData ---
	holds all sprites, spritesheets, and related variables
"""

import pygame

"""
	SPRITESHEETS
"""
char_sheet = pygame.image.load("res/tilesets/dc-mon.png")

"""
	LEVELS
"""
debug_level = pygame.image.load("res/maps/debug_map.png")
arena_level = pygame.image.load("res/maps/arena_1.png")


"""
	SPRITES TO LOAD ONCE
"""
# --- fighter ---
char_sheet.set_clip(pygame.Rect(160, 128, 32, 32))
fighter = char_sheet.subsurface(char_sheet.get_clip())
# --- arcanist ---
char_sheet.set_clip(pygame.Rect(0, 128, 32, 32))
arcanist = char_sheet.subsurface(char_sheet.get_clip())
# --- pathfinder ---
char_sheet.set_clip(pygame.Rect(448, 96, 32, 32))
pathfinder = char_sheet.subsurface(char_sheet.get_clip())

# --- skeleton ---
char_sheet.set_clip(pygame.Rect(577, 512, 32, 32))
skeleton = char_sheet.subsurface(char_sheet.get_clip())


# returns a sprite at the given location
def load_sprite(x_loc, y_loc, h, w):
	char_sheet.set_clip(pygame.Rect(x_loc, y_loc, h, w))
	sprite = char_sheet.subsurface