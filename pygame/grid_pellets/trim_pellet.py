import pygame
from pygame.transform import scale2x

SCREEN_WIDTH = (640/3+11)*2
SCREEN_HEIGHT = 248*2

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

spritesheet = pygame.image.load('spritesheet.png')
sp2 = scale2x(pygame.image.load('spritesheet.png'))
#pellet = scale2x(spritesheet.subsurface(10, 10, 5, 5))
pellet = scale2x(scale2x(scale2x(spritesheet.subsurface(10, 10, 4, 4))))
power_pellet = scale2x(spritesheet.subsurface(7, 23, 10, 10))
#power_pellet = scale2x(spritesheet.subsurface(8, 24, 8, 8))


#screen.fill((255,255,255))

#screen.blit(pellet, (50,50))
screen.blit(power_pellet, (50,50))
#screen.blit(sp2, (0,0))


NUM_COLUMNS = 28
NUM_ROWS = 30

LIGHT_GREY = (160,160,160)
LIGHT_GREEN = (84,178,84)
line_color = LIGHT_GREEN

COLUMN_WIDTH = SCREEN_WIDTH / NUM_COLUMNS
xinc = COLUMN_WIDTH
ROW_HEIGHT = SCREEN_HEIGHT / NUM_ROWS
yinc = ROW_HEIGHT

#print "column width: ", COLUMN_WIDTH
#print "column height: ", ROW_HEIGHT

linex = 0
for i in range(NUM_COLUMNS):
    linex += COLUMN_WIDTH
    #pygame.draw.line(screen, line_color, (linex, 0), (linex, SCREEN_HEIGHT))

liney = 0
for i in range(NUM_ROWS):
    liney += ROW_HEIGHT
    #pygame.draw.line(screen, line_color, (0, liney), (SCREEN_WIDTH, liney))

u = pygame.display.update
u()

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

pygame.quit()
