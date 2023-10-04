#importing the games
from games import forfunsies as ff
from games import snake as sn
from games import pong as p
from games import flappbird as flap
from games import scoreboard as sb

#whatever someone clicks on makes this do that game
def choice(choice):
	if choice == 0:
		p.game()
	elif choice == 1:
		flap.Game()
	elif choice == 2:
		sn.game()
	elif choice == 3:
		ff.game()		
	elif choice == 4:
		sb.scores()
	else:
			pass


#whatever i googled suggested this so it wouldnt run the forfunsies by itself
def main():

    #pygame for the main function
    #pygame menu so it lets the user choose
    import pygame as pg
    import pygame_menu as pgm

    pg.init()

    #dont need to set the height and width manually, autoadjusts to the opened window
    surface = pg.display.set_mode()

    #need this because menu will not work without a given width and height though so this sets it to the opened window
    width, height = pg.display.get_window_size()

    menu = pgm.Menu('Please Choose a Game', width, height)

    menu.add.button('Pong', choice, 0)
    menu.add.button('FlappyBird', choice, 1)
    menu.add.button('Snake', choice, 2)
    menu.add.button('Scores', choice, 4)
    menu.add.button('Quit', pgm.events.EXIT)

    #changed the font color to match the background
    #i want a better method but idk
    menu.add.button('Funsies', choice, 3, font_color=(219, 219, 219))

    menu.mainloop(surface)


if __name__ == '__main__':
    main()
