import pygame
from pygame.transform import scale2x

screen = pygame.display.set_mode((300,300))
spritesheet = pygame.image.load('spritesheet.png')

wall = scale2x(spritesheet.subsurface(448, 2, 5, 100))
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
            pygame.quit()
