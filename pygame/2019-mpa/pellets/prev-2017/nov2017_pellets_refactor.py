import pygame
from pygame.transform import scale2x

pygame.init()

class ThinSprite:
    def __init__(self, surface, startx, starty):
        self.image = surface
        self.rect = self.image.get_rect()
        self.rect.x = startx
        self.rect.y = starty
        self.direction = 'right'


screen = pygame.display.set_mode((640,300))
spritesheet = pygame.image.load('../spritesheet.png').convert()
spritesheet.set_colorkey((0,0,0))

xpad = 4
pacman_right_pre = spritesheet.subsurface(680 / 3 * 2 + xpad, 0, 16, 16).convert()
pacman_right_pre.set_colorkey((0,0,0))
pacman_right_pre.convert_alpha()
pacman_right = scale2x(pacman_right_pre)
pacman_right.set_colorkey((0,0,0))
pacman_left = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 16, 16, 16))
pacman_up = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 32, 16, 16))
pacman_down = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 48, 16, 16))
pellet_image_pre = spritesheet.subsurface(10, 10, 5, 5)
pellet_image_pre.set_colorkey((0,0,0))
pellet_image_pre.convert_alpha()
pellet_image = scale2x(scale2x(pellet_image_pre))

pellet_y = 150
PELLET_XINCR = 55
pellets = []
for i in range(2,10):
    x = i * PELLET_XINCR
    pellets.append(ThinSprite(pellet_image, x, pellet_y))

#pellet = ThinSprite(pellet_image, 25, 25)

pacman = ThinSprite(pacman_right, 50, 150)
INCREMENT = 2

moving = False

# font for printing score
font = pygame.font.SysFont(None, 24)

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

    #screen.blit(pacman.image, (pacman.rect.x, pacman.rect.y))

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
            elif kname == 'left':
                pacman.image = pacman_left
            elif kname == 'up':
                pacman.image = pacman_up
            elif kname == 'down':
                pacman.image = pacman_down


pygame.quit()
