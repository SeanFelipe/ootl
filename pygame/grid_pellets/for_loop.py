import pygame
from pygame.transform import scale2x

SCREEN_WIDTH = (640/3+11)*2
SCREEN_HEIGHT = 248*2
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Pacman MPA')
spritesheet = pygame.image.load('spritesheet.png')
start_screen = scale2x(spritesheet.subsurface(0,0, 640/3 + 11, 248))
screen.blit(start_screen, (0,0))

NUM_COLUMNS = 28
NUM_ROWS = 30
LIGHT_GREY = (160,160,160)
LIGHT_GREEN = (84,178,84)
line_color = LIGHT_GREEN
#
#COLUMN_WIDTH = SCREEN_WIDTH / NUM_COLUMNS
COLUMN_WIDTH = 20
#ROW_HEIGHT = SCREEN_HEIGHT / NUM_ROWS
ROW_HEIGHT = 20

for i in range(10):
    linex = i * COLUMN_WIDTH
    pygame.draw.line(screen, line_color, (linex, 0), (linex, SCREEN_HEIGHT))

liney = 0
for i in range(10):
    liney = i * ROW_HEIGHT
    pygame.draw.line(screen, line_color, (0, liney), (SCREEN_WIDTH, liney))



clock = Pygame.time.Clock()

u = pygame.display.update
u()

running = True
while running:
    clock.tick(10)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

pygame.quit()
