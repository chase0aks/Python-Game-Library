def game():
	import pygame as pg
	import random
	from enum import Enum
	from pygame.locals import K_RETURN

	class Food:
		def __init__(self, block_size, bounds):
			self.block_size = block_size
			self.bounds = bounds
			self.color = (255, 0, 0)
			self.x = 0
			self.y = 0

			# Initialize the food in a random position
			self.respawn()
			
		def draw(self, game, window):
			game.draw.rect(window, self.color, (self.x, self.y, self.block_size, self.block_size))
			
		def respawn(self):
			blocks_in_x = (self.bounds[0]) / self.block_size
			blocks_in_y = (self.bounds[1]) / self.block_size
			self.x = random.randint(0, blocks_in_x - 1) * self.block_size
			self.y = random.randint(0, blocks_in_y - 1) * self.block_size


	class Direction(Enum):
		Up = 0
		Down = 1
		Left = 2
		Right = 3

	class Snake:
		def __init__(self, block_size, bounds):
			self.block_size = block_size
			self.bounds = bounds
			self.color = (0, 255, 0)
			self.length = 0
			self.direction = Direction.Down
			self.body = []
			self.score = 0

			# Initialize the snake in a default position
			self.respawn()
		
		def respawn(self):
			self.length = 3
			self.body = [(20, 20), (20, 40), (20, 60)]
			self.direction = Direction.Down
			self.score = 0

		def draw(self, game, window):
			for segment in self.body:
				game.draw.rect(window, self.color,
                           (segment[0], segment[1], self.block_size, self.block_size))
				for segment in self.body:
					x, y = segment
					game.draw.rect(window, (0, 0, 0),
                           (x - 1, y - 1, self.block_size + 2, self.block_size + 2), 1)

		def move(self):
			curr_head = self.body[-1]
			if self.direction == Direction.Down:
				next_head = (curr_head[0], curr_head[1] + self.block_size)
				self.body.append(next_head)
			elif self.direction == Direction.Up:
				next_head = (curr_head[0], curr_head[1] - self.block_size)
				self.body.append(next_head)
			elif self.direction == Direction.Right:
				next_head = (curr_head[0] + self.block_size, curr_head[1])
				self.body.append(next_head)
			elif self.direction == Direction.Left:
				next_head = (curr_head[0] - self.block_size, curr_head[1])
				self.body.append(next_head)
				
			if self.length < len(self.body):
				self.body.pop(0)
				
		def steer(self, direction):
			if self.direction == Direction.Down and direction != Direction.Up:
				self.direction = direction
			elif self.direction == Direction.Up and direction != Direction.Down:
				self.direction = direction
			elif self.direction == Direction.Left and direction != Direction.Right:
				self.direction = direction
			elif self.direction == Direction.Right and direction != Direction.Left:
				self.direction = direction
				
		def eat(self):
			self.length += 1
			self.score += 1

		def check_for_food(self, food):
			head = self.body[-1]
			if head[0] == food.x and head[1] == food.y:
				self.eat()
				food.respawn()

		def check_tail_collision(self):
			head = self.body[-1]
			has_eaten_tail = False

			for i in range(len(self.body) - 1):
				segment = self.body[i]
				if head[0] == segment[0] and head[1] == segment[1]:
					has_eaten_tail = True

			return has_eaten_tail

		def check_bounds(self):
			head = self.body[-1]
			if head[0] >= self.bounds[0]:
				return True
			if head[1] >= self.bounds[1]:
				return True

			if head[0] < 0:
				return True
			if head[1] < 0:
				return True

			return False


	pg.init()
	window = pg.display.set_mode()
	width, height = pg.display.get_window_size()
	pg.display.set_caption("Snake")

	snake = Snake(20, (width, height))
	food = Food(20, (500, 500))
	font = pg.font.SysFont('comicsans', 60, True)
	font2 = pg.font.SysFont('comicsans', 30, True)

	run = True
	while run:
		pg.time.delay(100)

		for event in pg.event.get():
			if event.type == pg.QUIT:
				run = False

		keys = pg.key.get_pressed()
		if keys[pg.K_LEFT]:
			snake.steer(Direction.Left)
		elif keys[pg.K_RIGHT]:
			snake.steer(Direction.Right)
		elif keys[pg.K_UP]:
			snake.steer(Direction.Up)
		elif keys[pg.K_DOWN]:
			snake.steer(Direction.Down)

		snake.move()
		snake.check_for_food(food)

		if snake.check_bounds() == True or snake.check_tail_collision() == True:
			score_text = font.render("Score: " + str(snake.score), True, (0, 0, 0))
			over = font.render('Game Over', True, (0, 0, 0))
			info = font2.render('Press Enter to Restart', True, (0, 0, 0))

			x1 = (width - score_text.get_width()) // 2
			x2 = (width - over.get_width()) // 2
			x3 = (width - info.get_width()) // 2

			window.blit(score_text, (x1, 20))
			window.blit(over, (x2, 120))
			window.blit(info, (x3, 220))
			pg.display.flip()

			snake.respawn()
			food.respawn()
			while True:
				event = pg.event.wait()
				if event.type == pg.KEYDOWN and event.key == K_RETURN:
					break
			with open('games/sscores.txt', 'a') as score:
				score.write(str(Snake.score))
				score.write('\n')
			snake.respawn()
			food.respawn()

		window.fill((255, 255, 255))
		snake.draw(pg, window)
		food.draw(pg, window)
		pg.display.update()
