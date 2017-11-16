import pygame
from pygame.transform import scale2x

screen = pygame.display.set_mode((300,300))
spritesheet = pygame.image.load('spritesheet.png')

wall_width = 5
wall_height = 100
wall = scale2x(spritesheet.subsurface(448, 2, wall_width, wall_height))

pacman_right = scale2x(spritesheet.subsurface(457, 0, 16, 16))
pacman_left = scale2x(spritesheet.subsurface(457, 16, 16, 16))
pacman_up = scale2x(spritesheet.subsurface(457, 32, 16, 16))
pacman_down = scale2x(spritesheet.subsurface(457, 48, 16, 16))
pacman = pacman_right

wallx, wally = 200, 70
pacmanx, pacmany = 50, 120

direction = 'right'
moving = False
running = True
while running:
    pygame.display.update()
    
    screen.fill((0,0,0))
    screen.blit(pacman, (pacmanx, pacmany))
    screen.blit(wall, (wallx, wally))

    if moving:
        if direction == 'right':
            pacmanx += 1
        elif direction == 'left':
            pacmanx -= 1
        elif direction == 'up':
            pacmany -= 1
        elif direction == 'down':
            pacmany += 1

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        elif e.type == pygame.KEYUP:
            moving = False
        elif e.type == pygame.KEYDOWN:
            moving = True
            kname = pygame.key.name(e.key)
            if kname == 'right':
                pacman = pacman_right
                direction = 'right'
            elif kname == 'left':
                pacman = pacman_left
                direction = 'left'
            elif kname == 'up':
                pacman = pacman_up
                direction = 'up'
            elif kname == 'down':
                pacman = pacman_down
                direction = 'down'
