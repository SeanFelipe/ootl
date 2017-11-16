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

class ThinSprite:
    def __init__(self, surface, startx, starty):
        self.image = surface
        self.rect = self.image.get_rect()
        self.rect.x = startx
        self.rect.y = starty
        self.direction = 'right'


screen = pygame.display.set_mode((640,300))
spritesheet = pygame.image.load('../spritesheet.png').convert()

xpad = 4
pacman_right = spritesheet.subsurface(680 / 3 * 2 + xpad, 0, 16, 16).convert()
pacman_right.set_colorkey((0,0,0))
pellet_image_pre = spritesheet.subsurface(10, 10, 5, 5)
pellet_image = scale2x(scale2x(pellet_image_pre))

pellet_y = 150
PELLET_XINCR = 50
pellets = []
for i in range(2,6):
    x = i * PELLET_XINCR
    pellets.append(ThinSprite(pellet_image, x, pellet_y))

#pellet = ThinSprite(pellet_image, 25, 25)

pacman = ThinSprite(pacman_right, 50, 150)
INCREMENT = 2

moving = False

# GAME LOOP
running = True
while running:
    pygame.display.update()

    # process movement
    if moving:
        if pacman.direction == 'right':
            pacman.rect.x += 2
        if pacman.direction == 'left':
            pacman.rect.x -= 2
        if pacman.direction == 'up':
            pacman.rect.y -= 2
        if pacman.direction == 'down':
            pacman.rect.y += 2


    # clear the screen and draw
    screen.fill((0,0,0))
    #screen.fill((255,255,255))
    for pellet in pellets:
        if pellet.rect.colliderect(pacman.rect):
            print 'collided with pellet: ', pellet
            pellets.remove(pellet)
        screen.blit(pellet.image, (pellet.rect.x, pellet.rect.y))

    screen.blit(pacman.image, (pacman.rect.x, pacman.rect.y))

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
            if kname == 'right':
                pacman.image = pacman_right


pygame.quit()
