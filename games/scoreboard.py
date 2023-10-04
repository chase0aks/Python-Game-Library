def scores():
	import pygame as pg
	import pygame_menu as pgm
	from games import fbscoreboard as fb
	from games import sscoreboard as sn
	from games import pscoreboard as p

	pg.init()
	surface = pg.display.set_mode()
	width, height = pg.display.get_window_size()

	def choice(choice):
		if choice == 1:
			fb.scores()
		elif choice == 2:
			sn.scores()
		elif choice == 3:
			p.scores()
		else:
				pass

	menu = pgm.Menu('Please choose a games Leaderboard', width, height,
                       theme=pgm.themes.THEME_BLUE)

	menu.add.button('FlappyBird', choice, 1)
	menu.add.button('Snake', choice, 2)
	menu.add.button('Pong', choice, 3)
	menu.add.button('Quit', pgm.events.EXIT)

	menu.mainloop(surface)