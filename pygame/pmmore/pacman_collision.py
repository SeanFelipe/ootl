import pygame
from pygame.transform import scale2x
import sys

screen = pygame.display.set_mode((680,600))
pygame.display.set_caption('Pacman MPA')
# returns a Surface
spritesheet = pygame.image.load('spritesheet.png')
start_screen = pygame.transform.scale2x(spritesheet.subsurface(0,0, 640/3 + 11, 248))
#screen.blit(start_screen, (0,0))
#screen.blit(spritesheet, (0,0))

xpad = 4
x2pad = 4 + 16

pacmanr = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 0, 16, 16))
pacmanl = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 16, 16, 16))
pacmanu = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 32, 16, 16))
pacmand = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 48, 16, 16))
pacman2r = scale2x(spritesheet.subsurface(680 / 3 * 2 + x2pad, 0, 16, 16))
pacman2l = scale2x(spritesheet.subsurface(680 / 3 * 2 + x2pad, 16, 16, 16))
pacman2u = scale2x(spritesheet.subsurface(680 / 3 * 2 + x2pad, 32, 16, 16))
pacman2d = scale2x(spritesheet.subsurface(680 / 3 * 2 + x2pad, 48, 16, 16))

prepacman = spritesheet.subsurface(680 / 3 * 2, 0, 16, 16)
prepacmanup = spritesheet.subsurface(680 / 3 * 2 + 16, 0, 16, 16)
preblinky = spritesheet.subsurface(680 / 3 * 2, 64, 16, 16)
prepinky = spritesheet.subsurface(680 / 3 * 2, 80, 16, 16)
preinky = spritesheet.subsurface(680 / 3 * 2, 96, 16, 16)
preclyde = spritesheet.subsurface(680 / 3 * 2, 112, 16, 16)
pacman = scale2x(prepacman)
pacmanup = scale2x(prepacmanup)
blinky = pygame.transform.scale2x(preblinky)
pinky = pygame.transform.scale2x(prepinky)
inky = pygame.transform.scale2x(preinky)
clyde = pygame.transform.scale2x(preclyde)

wallx = 0
wall_width = 680 / 3
wall_height = 248 / 3
wall = scale2x(spritesheet.subsurface(wallx, 0, wall_width, wall_height))

screen.blit(wall, (80, 20))

ghostx = 168
ghosty = 200
screen.blit(pacmanu, (ghostx, ghosty))
#screen.blit(blinky, (70, ghosty))
#screen.blit(pinky, (110, ghosty))
#screen.blit(inky, (150, ghosty))
#screen.blit(clyde, (200, ghosty))

u = pygame.display.update
u()

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
