import pygame
from pygamejr import loop

pygame.init()

spritesheet = pygame.image.load('explosion.png')
#spritesheet.convert()
#spritesheet.set_colorkey((248, 248, 248, 255))

sw, sh = spritesheet.get_width(), spritesheet.get_height()
screen = pygame.display.set_mode((sw, sh))

screen.blit(spritesheet, (0,0))

cols = 8
rows = 6
grid_width = sw / cols
grid_height = sh / rows

GREEN = (0,255,0)
LINE_WIDTH = 2
XPAD = 4

gx = 0
for c in range(cols):
    gy = sh
    gx = ( c * grid_width ) + XPAD
    startp = (gx, 0)
    endp = (gx, gy)
    pygame.draw.line(screen, GREEN, startp, endp, LINE_WIDTH)

loop()
