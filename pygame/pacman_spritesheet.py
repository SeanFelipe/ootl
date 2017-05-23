import pygame
import sys

screen = pygame.display.set_mode((640,480))
# returns a Surface
spritesheet = pygame.image.load('spritesheet.png')
screen.blit(spritesheet, (0,0))
# get the pacman image
# study this method to find the argument sequence
# https://www.pygame.org/docs/ref/surface.html#pygame.Surface.subsurface
# then add the correct arguments to Surface.subsurface() to get a pacman image
# pacman = spritesheet.subsurface()
# spritesheet.blit(pacman, (300, 50))

u = pygame.display.update
u()

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.MOUSEMOTION:
            pass
        else:
            print e
            if e.type == pygame.QUIT:
                running = False
                pygame.quit()
