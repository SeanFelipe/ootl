import pygame
from pygame.transform import scale2x

SCREEN_WIDTH = (640/3+11)*2
SCREEN_HEIGHT = 248*2
screen_width_at_2x = (640/3+11)*2
screen_height_at_2x = 248 * 2
blank_grid_padx = 15
blank_grid_startx = (640 / 3) + blank_grid_padx

screen = pygame.display.set_mode((screen_width_at_2x, screen_height_at_2x))
pygame.display.set_caption('Pacman and the Grid')
spritesheet = pygame.image.load('spritesheet.png')
start_screen = scale2x(spritesheet.subsurface(blank_grid_startx ,0, 640/3 + 11, 248))
screen.blit(start_screen, (0,0))

NUM_COLUMNS = 28
NUM_ROWS = 30
LIGHT_GREY = (160,160,160)
LIGHT_GREEN = (84,178,84)
line_color = LIGHT_GREEN

COLUMN_WIDTH = SCREEN_WIDTH / NUM_COLUMNS
ROW_HEIGHT = SCREEN_HEIGHT / NUM_ROWS

linex = 0
for i in range(NUM_COLUMNS):
    linex += COLUMN_WIDTH
    pygame.draw.line(screen, line_color, (linex, 0), (linex, SCREEN_HEIGHT))

liney = 0
for i in range(NUM_ROWS):
    liney += ROW_HEIGHT
    pygame.draw.line(screen, line_color, (0, liney), (SCREEN_WIDTH, liney))








u = pygame.display.update
u()

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

pygame.quit()
