import pygame
from pygame.transform import scale2x

screen = pygame.display.set_mode((300,300))
spritesheet = pygame.image.load('../spritesheet.png')

'''
from pdb import set_trace

pygame.display.set_caption('Pacman MPA')
# returns a Surface
start_screen = pygame.transform.scale2x(spritesheet.subsurface(0,0, 640/3 + 11, 248))
#screen.blit(start_screen, (0,0))
#screen.blit(spritesheet, (0,0))
xpad = 4
x2pad = 4 + 16
pacman_right = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 0, 16, 16))
pacman_left = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 16, 16, 16))
pacman_up = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 32, 16, 16))
pacman_down = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 48, 16, 16))
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

ghosty = 200
pacman_x = 75
pacman_y = ghosty

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

pacman_directions = {
    'right' : pacman_right,
    'left'  : pacman_left,
    'up'    : pacman_up,
    'down'  : pacman_down,
}

direction = 'right'
'''


xpad = 4
pacman_right = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 0, 16, 16))
pacman_left = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 16, 16, 16))
pacman_up = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 32, 16, 16))
pacman_down = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 48, 16, 16))

pacman_x = 50
pacman_y = 50
pacman = pacman_right

running = True
while running:

    screen.blit(pacman, (pacman_x, pacman_y))
            
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif e.type == pygame.KEYDOWN:
            kname = pygame.key.name(e.key)
            print kname
            #############################################################
            # figure out what x/y values to change, and add or subtract #
            #############################################################
            if kname == 'right':
                pacman = pacman_right
                pacman_x += 1
            elif kname == 'left': 
                pacman = pacman_left
                # ????
            # and so on

    pygame.display.update()
            

