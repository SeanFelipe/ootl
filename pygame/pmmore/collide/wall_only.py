import pygame
from pygame.transform import scale2x

screen = pygame.display.set_mode((300,300))
spritesheet = pygame.image.load('spritesheet.png')

wallx = 680 / 3 * 2 - 4
wall_width = 5
wall_height = 100
wall = scale2x(spritesheet.subsurface(wallx, 2, wall_width, wall_height))
pacman = scale2x(spritesheet.subsurface(680 / 3 * 2, 0, 16, 16))


running = True
while running:
    pygame.display.update()
    screen.blit(wall, (200, 70))
    screen.blit(pacman, (50,120))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
