import pygame
from pygame.transform import scale2x

class ThinSprite:
    def __init__(self, surface, startx, starty):
        self.image = surface
        self.x = startx
        self.y = starty
        self.direction = 'right'


screen = pygame.display.set_mode((300,300))
spritesheet = pygame.image.load('../spritesheet.png')

xpad = 4
pacman_right = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 0, 16, 16))
pacman_left = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 16, 16, 16))
pacman_up = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 32, 16, 16))
pacman_down = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 48, 16, 16))

wallx = 680 / 3 * 2 - 4
wall_width = 5
wall_height = 100
wall_surf = scale2x(spritesheet.subsurface(wallx, 2, wall_width, wall_height))
wall = ThinSprite(wall_surf, 200, 100)

pacman = ThinSprite(pacman_right, 100, 150)
INCREMENT = 2


moving = False

# GAME LOOP
running = True
while running:
    pygame.display.update()
    screen.fill((0,0,0))
    screen.blit(pacman.image, (pacman.x, pacman.y))
    screen.blit(wall.image, (wall.x, wall.y))


    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYUP:
            moving = False
        elif e.type == pygame.KEYDOWN:
            kname = pygame.key.name(e.key)
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


    if moving:
        if pacman.direction == 'right':
            pacman.x += 2
        if pacman.direction == 'left':
            pacman.x -= 2
        if pacman.direction == 'up':
            pacman.y -= 2
        if pacman.direction == 'down':
            pacman.y += 2


pygame.quit()
