"""
	--- Entry ---
	game starts here
"""

"""
	--- TODO ---
	1.) main menu
	2.) add enemies group
	5.) powerups, specific spawns, etc
	6.) more sophisticated health system, visual indication of health
	
"""

"""
	modules
"""
import sys, pygame
from Player import *
from BasicEnemy import *
from ArenaMap import *
from SpriteData import *
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

# create the object that holds map data and load the wall rectangles
level = ArenaMap()
level_walls = level.load_walls()
level_hazards = level.load_hazards()

# create the player
player = Player(arcanist)

# make enemies
# enemy_one = BasicEnemy(576, 272, skeleton)

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

	player.check_dead()

	if keys_pressed[K_LEFT]:
		player.pos_update(-(player.ms), 0, level_walls, level_hazards)
	if keys_pressed[K_RIGHT]:
		player.pos_update(player.ms, 0, level_walls, level_hazards)
	if keys_pressed[K_UP]:
		player.pos_update(0, -(player.ms), level_walls, level_hazards)
	if keys_pressed[K_DOWN]:
		player.pos_update(0, player.ms, level_walls, level_hazards)

	# enemy_one.move_to_player(player.rect.x, player.rect.y)

	# clear screen
	screen.fill(WHITE)

	# draw map
	screen.blit(level.level_image, [0, 0])

	# draw enemies
	# screen.blit(enemy_one.sprite, [enemy_one.rect.x, enemy_one.rect.y])
	
	# draw player
	screen.blit(player.sprite, [player.rect.x, player.rect.y])

	# update screen with drawn stuff
	pygame.display.flip()

	# 120 fps
	clock.tick(60)

# close window and exit
pygame.display.quit()
pygame.quit()
sys.exit()




