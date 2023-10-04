import pygame, time
from sys import exit


def game():
    pygame.init()
    dvdLogoSpeed = [1, 1]
    backgroundColor = 0, 0, 0

    screen = pygame.display.set_mode()
    width, height = pygame.display.get_window_size()


    dvdLogo = pygame.image.load("games/images/dvdlogo.png")
    dvdLogo = pygame.transform.rotozoom(dvdLogo, 0, .5)
    dvdLogoRect = dvdLogo.get_rect()

    while True:
        screen.fill(backgroundColor)

        screen.blit(dvdLogo, dvdLogoRect)
        dvdLogoRect = dvdLogoRect.move(dvdLogoSpeed)

        if dvdLogoRect.left < 0 or dvdLogoRect.right > width:
            dvdLogoSpeed[0] = -dvdLogoSpeed[0]
        if dvdLogoRect.top < 0 or dvdLogoRect.bottom > height:
            dvdLogoSpeed[1] = -dvdLogoSpeed[1]

        pygame.display.flip()
        time.sleep(10 / 1000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
