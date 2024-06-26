import pygame

CELL_SIZE = 20
WHITE = (150,75,25)

def snaker(screen, territories, startx, starty, color):
	snake_speed = 15
	dead = False

	fps = pygame.time.Clock()

	# defining snake default position
	snake_position = [100, 50]

	# defining first 4 blocks of snake body
	snake_body = [
		[100, 50],[100, 50],[100, 50],[100, 50],[110, 50],
		[100, 50],[100, 50],[100, 50],[100, 50],[100, 50],[100, 50],[100, 50],[100, 50],[100, 50],[100, 50],[100, 50],[100, 50],[100, 50],[100, 50],[100, 50],[100, 50],[100, 50],[100, 50],
				[90, 50],
				[80, 50],
				[70, 50],
				[60, 50],
				[50, 50],
				[40, 50],
				[30, 50],
				[20, 50],
				[10, 50],
				[0, 50],
				]
	# fruit position
	fruit_position = [startx, starty]

	# setting default snake direction towards
	# right
	direction = 'NONE'
	change_to = direction

	snakedir = 'RIGHT'

	# Main Function
	while True:

		# handling key events
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					change_to = 'UP'
				if event.key == pygame.K_DOWN:
					change_to = 'DOWN'
				if event.key == pygame.K_LEFT:
					change_to = 'LEFT'
				if event.key == pygame.K_RIGHT:
					change_to = 'RIGHT'

		# If two keys pressed simultaneously
		# we don't want snake to move into two
		# directions simultaneously
		if change_to == 'UP':
			direction = 'UP'
		if change_to == 'DOWN':
			direction = 'DOWN'
		if change_to == 'LEFT':
			direction = 'LEFT'
		if change_to == 'RIGHT':
			direction = 'RIGHT'

		# Moving the fruit
		if direction == 'UP':
			fruit_position[1] -= 15
		if direction == 'DOWN':
			fruit_position[1] += 15
		if direction == 'LEFT':
			fruit_position[0] -= 15
		if direction == 'RIGHT':
			fruit_position[0] += 15

		if fruit_position[1] > snake_position[1] and snakedir != 'DOWN':
			snakedir = 'UP'
			snake_position[1] += 7
		if fruit_position[1] < snake_position[1] and snakedir != 'UP':
			snakedir = "DOWN"
			snake_position[1] -= 7
		if fruit_position[0] > snake_position[0] and snakedir != "LEFT":
			snakedir = "RIGHT"
			snake_position[0] += 7
		if fruit_position[0] < snake_position[0] and snakedir!= "RIGHT":
			snakedir = "LEFT"
			snake_position[0] -= 7

		snake_body.pop()

		snake_body.insert(0, list(snake_position))

		if fruit_position[0] >= 799:
			fruit_position[0] = 0
		elif fruit_position[0] <= 0:
			fruit_position[0] = 790
		if fruit_position[1] >= 599:
			fruit_position[1] = 0
		elif fruit_position[1] <= 0:
			fruit_position[1] = 599

		cell_x = fruit_position[0] // CELL_SIZE
		cell_y = fruit_position[1] // CELL_SIZE


		if territories[cell_y][cell_x].continent != 0:
			return (cell_y, cell_x)


		for y, row in enumerate(territories):
			for x, territory in enumerate(row):
				if not territory.continent:
					pygame.draw.rect(screen, territory.color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
					continue


		for pos in snake_body:
			cell_x = pos[0] // CELL_SIZE
			cell_y = pos[1] // CELL_SIZE
			if territories[cell_y][cell_x].continent == 0:
				pygame.draw.rect(screen, WHITE, pygame.Rect(pos[0], pos[1], 20, 20))

		pygame.draw.rect(screen, color, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

		for block in snake_body:
			if abs(block[0] - fruit_position[0]) < 20 and abs(block[1] - fruit_position[1]) < 20:
				dead = True
				break

		if dead:
			return 0

		# Refresh game screen
		pygame.display.update()

		# Frame Per Second /Refresh Rate
		fps.tick(snake_speed)