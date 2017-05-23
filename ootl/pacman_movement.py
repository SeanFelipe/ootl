import pygame
import sys

screen = pygame.display.set_mode((640,480)) # returns a Surface
spritesheet = pygame.image.load('spritesheet.png') # also returns a surface
#screen.blit(spritesheet, (0,0)) # draws spritesheet onto the screen
# the above ^^ will NOT display until you call pygame.display.update() !

# get the pacman image
# study this method to find the argument sequence
# https://www.pygame.org/docs/ref/surface.html#pygame.Surface.subsurface
# then add the correct arguments to Surface.subsurface() to get a pacman image
#pacman = spritesheet.subsurface()
# screen.blit(pacman, (300, 50))

x = 0
y = 0
w = 0
h = 0


first_screen = spritesheet.subsurface(x, y, w, h)

startx = 100
starty = 100
pacmanx, pacmany = startx, starty



running = True
while running:
    #screen.blit(pacman, pacmanx, pacmany)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
        # what is the event type for a keyboard press?
        # https://www.pygame.org/docs/ref/event.html
        '''
        elif e.type == pygame.?????:
            # how do we get which key was pressed?
            # what keys do we care about?
            # what direction to we need to adjust based on which key is pressed?
            # adjust pacmanx
            # adjust pacmany
        '''     
        pygame.display.update()
