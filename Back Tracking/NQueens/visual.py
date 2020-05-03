import pygame
import time

def set_queen(coordinates, square_color, gameDisplay):
	x = coordinates[0][0]
	y = coordinates[0][1]
	if square_color == ('white'):
		black_queen = pygame.transform.scale(pygame.image.load('black_queen.png'), (50, 50))
		gameDisplay.blit(black_queen, (x+2, y))
		pygame.display.update()

	if square_color == 'black':
		white_queen = pygame.transform.scale(pygame.image.load('white_queen.png'), (50, 50))
		gameDisplay.blit(white_queen, (x+2, y))
		pygame.display.update()

	time.sleep(1)
	#remove_queen([(x, y), square_color])

def remove_queen(screen, data):
	rect = (data[0][0], data[0][1], 55, 55)
	pygame.draw.rect(screen, data[1], rect)
	pygame.display.update()

def create_board(N, screen):
	coordinates = {}
	y = 0

	black = (0, 0, 0)
	white = (255, 255, 255)

	x_pos = 0
	y_pos = 50
	for x in range(N*N):


		if x % N == 0:
			x_pos = 200
			y_pos += 55
			y += 1
			if N % 2 == 0:
				temp= white
				white = black
				black = temp  

		if x % 2 == 0:
			color = black
		else:
			color = white
		rect = (x_pos, y_pos, 55, 55)
		coordinates[(y, x%N)] = [(x_pos, y_pos), color]
		pygame.draw.rect(screen, color, rect)
		x_pos += 55

	return coordinates

'''
rect = (50, 50, 55, 55)
pygame.draw.rect(screen, black, rect)
rect = (105, 50, 55, 55)
pygame.draw.rect(screen, white, rect)
rect = (160, 50, 55, 55)
pygame.draw.rect(screen, black, rect)
rect = (215, 50, 55, 55)
pygame.draw.rect(screen, white, rect)
'''
def visual(N):
	pygame.init()

	screen = pygame.display.set_mode((640,480))
	display_width = 800
	display_height = 800

	tan = (210, 180, 140)

	gameDisplay = pygame.display.set_mode((display_width, display_height))
	gameDisplay.fill(tan)
	
	pygame.display.set_caption('N-Queens Back Tracking Visual')
	clock = pygame.time.Clock()
	
	create_board(N, screen)
	pygame.display.update()
	time.sleep(8)
	crashed = False		
	
	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed = True
		
		
		clock.tick(60)

	pygame.quit()

visual(8)

