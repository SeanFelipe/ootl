import pygame
from pygame.transform import scale2x

screen = pygame.display.set_mode((300,300))
spritesheet = pygame.image.load('spritesheet.png')

wall_width = 5
wall_height = 100
wall = scale2x(spritesheet.subsurface(448, 2, wall_width, wall_height))
pacman = scale2x(spritesheet.subsurface(453, 0, 16, 16))

wallx, wally = 200, 70
pacmanx, pacmany = 50, 120

running = True
while running:
    pygame.display.update()
    screen.blit(wall, (wallx, wally))
    screen.blit(pacman, (pacmanx, pacmany))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
