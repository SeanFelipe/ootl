import pygame
from pygame.transform import scale2x

screen = pygame.display.set_mode(((640/3+11)*2,248*2))
pygame.display.set_caption('Pacman MPA')
spritesheet = pygame.image.load('spritesheet.png')
start_screen = scale2x(spritesheet.subsurface(0,0, 640/3 + 11, 248))
screen.blit(start_screen, (0,0))

NUM_COLUMNS = 26
NUM_ROWS = 26
LINE_COLOR = (50, 255, 50)

linxx, liney = 0,0
for i in range(NUM_COLUMNS):
    pygame.draw.line(

    for j in range(NUM_ROWS):
        pygame.draw.line(



u = pygame.display.update
u()

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

pygame.quit()
