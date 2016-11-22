"""
	--- Entry ---
	game starts here
"""

"""
	--- TODO ---
	1.) add file for global vars and map info etc for all classes to access. also allow for pre-loading!
	2.) add logic for groups of entities (enemies, sprites, etc...)
	3.) make spritesheet dictionaries, abstract to own SpriteList class or some shit idk yet
	4.) main menu
	5.) other map elements like hazards, powerups, etc
	6.) health bars
	7.) upload to git and shit
"""

"""
	modules
"""
import sys, pygame
from Player import *
from BasicEnemy import *
from ArenaMap import *
from pygame.locals import *

"""
	colors 
"""
WHITE = (255, 255, 255)

"""
	vars
"""
# 40 tiles wide, 23 tiles tall
screen_width = 1280
screen_height = 736
# for control of how fast screen updates
clock = pygame.time.Clock()

"""
	create screen
"""
pygame.init()
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Flip")

"""
	sprite data
"""
#levels
#debug_level = pygame.image.load("res/maps/debug_map.png")
arena_level = pygame.image.load("res/maps/arena_1.png")
# tileset for characters
char_sheet = pygame.image.load("res/tilesets/dc-mon.png")

# character sprites
# find a sprite (sprite x, sprite y, sprite x len, sprite y len)
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

# create the object that holds map data and load the wall rectangles
arena_map = ArenaMap(arena_level)
arena_map_walls = arena_map.load_walls()


# create the player
player = Player(arcanist)

# make enemies
enemy_one = BasicEnemy(576, 272, skeleton)


"""
	game loop
"""
running = True

while running:

	# main even loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# game logic
	keys_pressed = pygame.key.get_pressed()

	if keys_pressed[K_LEFT]:
		player.pos_update(-(player.ms), 0, arena_map_walls)
	if keys_pressed[K_RIGHT]:
		player.pos_update(player.ms, 0, arena_map_walls)
	if keys_pressed[K_UP]:
		player.pos_update(0, -(player.ms), arena_map_walls)
	if keys_pressed[K_DOWN]:
		player.pos_update(0, player.ms, arena_map_walls)

	enemy_one.move_to_player(player.rect.x, player.rect.y)

	# clear screen
	screen.fill(WHITE)

	# draw map
	screen.blit(arena_map.level_image, [0, 0])

	# draw enemies
	screen.blit(enemy_one.sprite, [enemy_one.rect.x, enemy_one.rect.y])
	
	# draw player
	screen.blit(player.sprite, [player.rect.x, player.rect.y])

	# update screen with drawn stuff
	pygame.display.flip()

	# 120 fps
	clock.tick(120)

# close window and exit
pygame.display.quit()
pygame.quit()
sys.exit()




