import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()

clock = pygame.time.Clock()

SCREEN_SIZE = (800, 600)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Mario Game")

player_image = pygame.image.load("images/mario.png")
flipped_player_image = pygame.image.load("images/mario_flip.png")

player_speed = 10
player_x = 30
player_y = 30
player_location = [player_x, player_y]


move_right = False
move_left = False
move_up = False
move_down = False

coin_image = pygame.image.load("images/coin.png")

random_pos = [50, 50]

player_rect = pygame.Rect(player_x, player_y, player_image.get_width(), player_image.get_height())
coin_rect = pygame.Rect(random_pos[0], random_pos[1], coin_image.get_width(), coin_image.get_height())

score = 0
font = pygame.font.SysFont(None, 24)

def generate_random_pos():
	random_pos_x = randint(1, 700)
	random_pos_y = randint(1, 500)
	random_pos.clear()
	random_pos.append(random_pos_x)
	random_pos.append(random_pos_y)

generate_random_pos()

def load_coin():
	screen.blit(coin_image, random_pos)

while True:
	screen.fill((0, 0, 0))
	text = font.render(f'Score: {score}', True, (255, 255, 255))
	screen.blit(text, (350, 0))
	player_location = [player_x, player_y]
	player_rect.x = player_location[0]
	player_rect.y = player_location[1]

	load_coin()
	coin_rect.x = random_pos[0]
	coin_rect.y = random_pos[1]
	
	screen.blit(player_image, player_location)

	if move_right:
		player_x += player_speed

	elif move_left:
		screen.blit(flipped_player_image, player_location)
		player_x -= player_speed

	elif move_up:
		player_y -= player_speed

	elif move_down:
		player_y += player_speed

	if player_rect.colliderect(coin_rect):
		generate_random_pos()
		score += 1

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		if event.type == KEYDOWN:
			if event.key == K_RIGHT:
				move_right = True

			elif event.key == K_LEFT:
				move_left = True

			elif event.key == K_UP:
				move_up = True

			elif event.key == K_DOWN:
				move_down = True

		if event.type == KEYUP:
			if event.key == K_RIGHT:
				move_right = False

			elif event.key == K_LEFT:
				move_left = False

			elif event.key == K_UP:
				move_up = False

			elif event.key == K_DOWN:
				move_down = False



	pygame.display.update()
	clock.tick(60)
