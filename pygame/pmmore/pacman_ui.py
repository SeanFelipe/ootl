import pygame
from pygame.transform import scale2x
from pdb import set_trace

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

pacman = scale2x(scale2x(prepacman))
pacmanup = scale2x(scale2x(prepacmanup))

blinky = pygame.transform.scale2x(preblinky)
pinky = pygame.transform.scale2x(prepinky)
inky = pygame.transform.scale2x(preinky)
clyde = pygame.transform.scale2x(preclyde)

pacmanx = 200
ghosty = 100

screen.blit(pacmanr, (70, ghosty))
screen.blit(pacmanl, (110, ghosty))
screen.blit(pacmanu, (150, ghosty))
screen.blit(pacmand, (200, ghosty))

ghost2y = 150
screen.blit(pacman2r, (70, ghost2y))
screen.blit(pacman2l, (110, ghost2y))
screen.blit(pacman2u, (150, ghost2y))
screen.blit(pacman2d, (200, ghost2y))

screen.blit(pacmanr, (500, ghosty))

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
            key = pygame.event.key(e.key)
            set_trace()
