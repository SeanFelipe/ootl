import pygame
import sys

screen = pygame.display.set_mode((640,480)) # returns a Surface
spritesheet = pygame.image.load('spritesheet.png') # also returns a surface
screen.blit(spritesheet, (0,0)) # draws spritesheet onto the screen
# the above ^^ will NOT display until you call pygame.display.update() !

# get the pacman image
# study this method to find the argument sequence
# https://www.pygame.org/docs/ref/surface.html#pygame.Surface.subsurface
# then add the correct arguments to Surface.subsurface() to get a pacman image
# pacman = spritesheet.subsurface()
# screen.blit(pacman, (300, 50))

startx = 100
starty = 100
pacmanx, pacmany = startx, starty



running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
        # what is the event type for a keyboard press?
        # https://www.pygame.org/docs/ref/event.html
        if e.type == pygame.?????:
            print e
            # how do we get which key was pressed?

