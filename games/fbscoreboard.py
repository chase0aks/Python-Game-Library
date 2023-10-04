def scores():
	import pygame as pg
	final_list = []
	with open('games/fbscores.txt', 'r') as f:
		score = f.read()
		score_ints = [int(x) for x in score.split()]
		for i in range(0, 5):
			max1 = 0

			for j in range(len(score_ints)):
				if score_ints[j] > max1:
					max1 = score_ints[j]

			score_ints.remove(max1)
			final_list.append(max1)

	pg.init()
	surface = pg.display.set_mode()
	width, height = pg.display.get_window_size()
	mid = width / 2
	list = [80, 150, 220, 290, 360]

	black = (0, 0, 0)
	white = (255, 255, 255)
	blue = (0, 0, 255)
	red = (255, 0, 0)

	running = True
	while running:
		surface.fill(black)
		font = pg.font.Font(None, 74)
		sfont = pg.font.Font(None, 37)
		title = font.render('Top 5 Scores', 1, blue)
		end = sfont.render('Press ESC to return', 1, red)
		surface.blit(title, (mid - 150, 10))
		surface.blit(end, (mid - 110, 430))
		for i in range(5):
			text = font.render(str(final_list[i]), 1, white)
			surface.blit(text, (mid - 20, list[i]))
		pg.display.flip()

		for event in pg.event.get():
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					running = False
