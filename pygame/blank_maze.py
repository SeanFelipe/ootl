import pygame
from pygame.transform import scale2x

loc = (640/3 + 15) * 2
w = (640/3 + 8) * 2
sw = loc - 12
sh = 248 * 2
screen = pygame.display.set_mode((sw, sh))
# returns a Surface
spritesheet = scale2x(pygame.image.load('spritesheet.png'))
blank = spritesheet.subsurface(loc,0,w,248 * 2)
screen.blit(blank, (0,0))
# get the pacman image
# study this method to find the argument sequence
# https://www.pygame.org/docs/ref/surface.html#pygame.Surface.subsurface
# then add the correct arguments to Surface.subsurface() to get a pacman image
# pacman = spritesheet.subsurface()
# spritesheet.blit(pacman, (300, 50))

u = pygame.display.update
u()

print spritesheet

pygame.image.save(screen, 'maze_blank.png')

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
