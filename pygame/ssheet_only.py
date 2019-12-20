import pygame
import sys

loc = 640/3 + 15
w = 640/3 + 12
screen = pygame.display.set_mode((loc -4,248))
# returns a Surface
spritesheet = pygame.image.load('spritesheet.png')
blank = spritesheet.subsurface(loc,0,w,248)
screen.blit(blank, (0,0))
# get the pacman image
# study this method to find the argument sequence
# https://www.pygame.org/docs/ref/surface.html#pygame.Surface.subsurface
# then add the correct arguments to Surface.subsurface() to get a pacman image
# pacman = spritesheet.subsurface()
# spritesheet.blit(pacman, (300, 50))

u = pygame.display.update
u()

print(spritesheet)

pygame.image.save(screen, 'maze_blank.png')

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
