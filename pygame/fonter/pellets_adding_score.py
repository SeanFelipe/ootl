'''
27apr2017 this transparency works.

Note the difference between convert() and convert_alpha().
The latter can defeat colorkey transparency perhaps?

What's going on with collisions is, the surface is a box,
so even though the pixels are transparent, the collision
is considering the full box and not the transparency.
Maybe need to use collidepoint()?
'''

import pygame
from pygame.transform import scale2x

pygame.init()

GREEN = (0,255,0)

#################################################################
# ThinSprite to combine image and position in one logical place #
#################################################################
class ThinSprite:
    def __init__(self, surface, startx, starty):
        self.image = surface
        self.rect = self.image.get_rect()
        self.rect.x = startx
        self.rect.y = starty
        self.direction = 'right'

###############
# SPRITESHEET #
###############
screen = pygame.display.set_mode((640,300))
spritesheet = pygame.image.load('../spritesheet.png').convert()

################
# PACMAN SETUP #
################
xpad = 4
x2pad = 4 + 16
pacman_1right = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 0, 16, 16))
pacman_1left = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 16, 16, 16))
pacman_1up = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 32, 16, 16))
pacman_1down = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 48, 16, 16))
pacman_right = scale2x(spritesheet.subsurface(680 / 3 * 2 + x2pad, 0, 16, 16))
pacman_left = scale2x(spritesheet.subsurface(680 / 3 * 2 + x2pad, 16, 16, 16))
pacman_up = scale2x(spritesheet.subsurface(680 / 3 * 2 + x2pad, 32, 16, 16))
pacman_down = scale2x(spritesheet.subsurface(680 / 3 * 2 + x2pad, 48, 16, 16))

pacman = ThinSprite(pacman_right, 50, 150)


###########
# PELLETS #
###########
PELLET_SCORE = 10
pellet_image_pre = spritesheet.subsurface(10, 10, 5, 5)
pellet_image = scale2x(scale2x(pellet_image_pre))

pellet_y = 150
PELLET_XINCR = 50
pellets = []
for i in range(2,10):
    x = i * PELLET_XINCR
    pellets.append(ThinSprite(pellet_image, x, pellet_y))

#pellet = ThinSprite(pellet_image, 25, 25)

########
# FONT #
########
font = pygame.font.SysFont(None, 24)

#############
# GAME LOOP #
#############
# game variables
score = 0
moving = False
running = True
# begin loop
while running:
    pygame.display.update()

    ##################
    # process movement
    if moving:
        if pacman.direction == 'right':
            pacman.image = pacman_right
            pacman.rect.x += 2
        if pacman.direction == 'left':
            pacman.image = pacman_left
            pacman.rect.x -= 2
        if pacman.direction == 'up':
            pacman.image = pacman_up
            pacman.rect.y -= 2
        if pacman.direction == 'down':
            pacman.image = pacman_down
            pacman.rect.y += 2


    ###########################
    # clear the screen and draw
    screen.fill((0,0,0))
    #screen.fill((255,255,255))
    for pellet in pellets:
        if pellet.rect.colliderect(pacman.rect):
            print 'collided with pellet: ', pellet
            pellets.remove(pellet)
            score += PELLET_SCORE
        screen.blit(pellet.image, (pellet.rect.x, pellet.rect.y))

    screen.blit(pacman.image, (pacman.rect.x, pacman.rect.y))


    ####################
    # display the score
    score_text = str(score)
    score_surface = font.render(score_text, True, GREEN)
    screen.blit(score_surface, (50, 50))


    ###################
    # process user input
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYUP:
            moving = False
        elif e.type == pygame.KEYDOWN:
            kname = pygame.key.name(e.key)
            if kname == 'q':
                running = False
            if kname in ('right','left','up','down'):
                moving = True
                pacman.direction = kname


pygame.quit()
