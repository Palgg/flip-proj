"""
	--- SpriteData ---
	holds all sprites, spritesheets, and related variables
"""

import pygame

# returns a sprite at the given location
def load_sprite(sheet, x_loc, y_loc, h, w):
	sheet.set_clip(pygame.Rect(x_loc, y_loc, h, w))
	sprite = sheet.subsurface(sheet.get_clip())
	return sprite

"""
	SPRITESHEETS
"""
char_sheet = pygame.image.load("res/tilesets/dc-mon.png")
dngn_sheet = pygame.image.load("res/tilesets/dc-dngn.png")

"""
	LEVELS
"""
debug_level = pygame.image.load("res/maps/debug_map.png")
arena_level = pygame.image.load("res/maps/arena_1.png")

"""
	FLOOR TILES
"""
floor_default = load_sprite(dngn_sheet, 64, 0, 32, 32)

"""
	SPRITES TO LOAD ONCE
"""
# --- dead player ---
dead_player = load_sprite(char_sheet, 96, 0, 32, 32)
# --- fighter ---
fighter = load_sprite(char_sheet, 160, 128, 32, 32)
# --- arcanist ---
arcanist = load_sprite(char_sheet, 0, 128, 32, 32)
# --- pathfinder ---
pathfinder = load_sprite(char_sheet, 448, 96, 32, 32)

# --- skeleton ---
skeleton = load_sprite(char_sheet, 577, 512, 32, 32)

# --- basic powerup ---
powerup = load_sprite(char_sheet, 448, 0, 32, 32)

# --- skills ---
warden_skill_one = pygame.image.load("res/skills/rock-acid-2.png")
warden_skill_icons = [warden_skill_one]

