import pygame
from pygame.transform import scale2x

screen_width_at_2x = (640/3+11)*2
screen_height_at_2x = 248 * 2
blank_grid_padx = 15
blank_grid_startx = (640 / 3) + blank_grid_padx

screen = pygame.display.set_mode((screen_width_at_2x, screen_height_at_2x))
pygame.display.set_caption('Pacman and the Grid')
spritesheet = pygame.image.load('spritesheet.png')
start_screen = scale2x(spritesheet.subsurface(blank_grid_startx ,0, 640/3 + 11, 248))
screen.blit(start_screen, (0,0))

u = pygame.display.update
u()

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

pygame.quit()
