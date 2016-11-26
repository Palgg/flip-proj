"""
	--- Entry ---
	game starts here
"""

"""
	--- TODO ---
	1.) abstract powerup spawn generation to the Powerup class file
	1.) MAKE POWERUPS A TIMED EVENT TRIGGER
	1.) FIX DUNGEON FLOOR TILE THAT DRAWS UNDER POWERUPS
	1.) main menu
	2.) add enemies group, powerups group, etc (things that need to be drawn and may dissapear)
	3.) powerup spawning/logic, timed event
	4.) specific spawns for map, pass to player
	5.) add damage for being in hazard and not moving
	6.) more sophisticated health system, visual indication of health
	7.) make the rest of the god damn game
	8.) maybe add town hub?
	9.) add possible enemy spawns to map key
	10.) add brick tile under the powerup spawn location
	11.) probably need to make assets for numbers/letters for the UI
	12.) add a method for generating new poerups
"""

"""
	modules
"""
import sys, pygame, random
from Player import *
from BasicEnemy import *
from ArenaMap import *
from SpriteData import *
from Powerup import *
from StartMenu import *
from pygame.locals import *

"""
	colors 
"""
WHITE = (255, 255, 255)

"""
	vars
"""
# 40 tiles wide, 25 tiles tall
screen_width = 1280
screen_height = 800
# for control of how fast screen updates
clock = pygame.time.Clock()

"""
	create screen
"""
pygame.init()
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Flip")

# load the map and relevant data
level = ArenaMap()
level_walls = level.load_walls()
level_hazards = level.load_hazards()
level_powerups = level.load_powerups()

# create the player
player = Player(fighter)

# make enemies
#enemy_one = BasicEnemy(576, 272, skeleton)

# powerup
powerup_spawn_index = random.randint(0, len(level_powerups)-1)
powerup = Powerup(level_powerups[powerup_spawn_index].x, level_powerups[powerup_spawn_index].y)

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
		player.pos_update(-(player.ms), 0, level_walls, level_hazards, powerup)
	if keys_pressed[K_RIGHT]:
		player.pos_update(player.ms, 0, level_walls, level_hazards, powerup)
	if keys_pressed[K_UP]:
		player.pos_update(0, -(player.ms), level_walls, level_hazards, powerup)
	if keys_pressed[K_DOWN]:
		player.pos_update(0, player.ms, level_walls, level_hazards, powerup)

	#enemy_one.move_to_player(player.rect.x, player.rect.y)

	# clear screen
	screen.fill(WHITE)

	# draw map
	screen.blit(level.level_image, [0, 0])

	# draw powerups
	if powerup.status == P_ACTIVE:
		powerup.animate()
		screen.blit(floor_default, [powerup.og_x, powerup.og_y])
		screen.blit(powerup.sprite, [powerup.x, powerup.y])
	elif powerup.status == P_INACTIVE:
		powerup.x = 0
		powerup.y = 0
		powerup.sprite = default_floor

	# draw enemies
	#screen.blit(enemy_one.sprite, [enemy_one.rect.x, enemy_one.rect.y])
	
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




