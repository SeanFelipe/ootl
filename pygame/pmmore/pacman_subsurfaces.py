import pygame
from pygame.transform import scale2x
import sys

screen = pygame.display.set_mode((680,600))
pygame.display.set_caption('Pacman MPA')
# returns a Surface
spritesheet = pygame.image.load('spritesheet.png')
start_screen = pygame.transform.scale2x(spritesheet.subsurface(0,0, 640/3 + 11, 248))
#screen.blit(start_screen, (0,0))
screen.blit(spritesheet, (0,0))
prepacman = spritesheet.subsurface(680 / 3 * 2, 0, 16, 16)
prepacmanup = spritesheet.subsurface(680 / 3 * 2 + 16, 0, 16, 16)
preblinky = spritesheet.subsurface(680 / 3 * 2, 64, 16, 16)
prepinky = spritesheet.subsurface(680 / 3 * 2, 80, 16, 16)
preinky = spritesheet.subsurface(680 / 3 * 2, 96, 16, 16)
preclyde = spritesheet.subsurface(680 / 3 * 2, 112, 16, 16)
pacman = scale2x(scale2x(prepacman))
pacmanup = scale2x(scale2x(prepacmanup))
blinky = pygame.transform.scale2x(preblinky)
pinky = pygame.transform.scale2x(prepinky)
inky = pygame.transform.scale2x(preinky)
clyde = pygame.transform.scale2x(preclyde)

wallx = ( 680 / 3 * 2 ) - 4
wall_width = 5
wall_height = 680 / 8
wall = scale2x(scale2x(spritesheet.subsurface(wallx, 0, wall_width, wall_height)))

screen.blit(wall, (550, 300))

pacmanx = 200
ghosty = 450
#screen.blit(blinky, (70, ghosty))
#screen.blit(pinky, (110, ghosty))
#screen.blit(inky, (150, ghosty))
#screen.blit(clyde, (200, ghosty))

u = pygame.display.update

running = True
while running:
    #screen.blit(pacman, (pacmanx, ghosty))
    u()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif e.type == pygame.KEYDOWN:
            keynum = e.__dict__['key']
            print keynum
            if keynum == 275:
                pacmanx += 5
