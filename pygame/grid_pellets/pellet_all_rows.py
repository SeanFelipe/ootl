import pygame
from pygame.transform import scale2x

pygame.init()

SCREEN_WIDTH = (640/3+11)*2
SCREEN_HEIGHT = 248*2
#print SCREEN_WIDTH
#print SCREEN_HEIGHT
#448
#496
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Pacman MPA')
clock = pygame.time.Clock()

FONT_GREEN = (0,255,0)
FONT_SIZE = 18
font = pygame.font.SysFont(None, FONT_SIZE)

spritesheet = pygame.image.load('spritesheet.png')
start_screen = scale2x(spritesheet.subsurface(0,0, 640/3 + 11, 248))

blank_grid_padx = 15
blank_grid_startx = (640 / 3) + blank_grid_padx
blank_screen = scale2x(spritesheet.subsurface(blank_grid_startx ,0, 640/3 + 11, 248))


pellet = scale2x(spritesheet.subsurface(10, 10, 4, 4))


#screen.blit(start_screen, (0,0))
screen.blit(blank_screen, (0,0))

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


pellet_table = [
    [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
    [ 0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0 ],
    [ 0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0 ],
    [ 0,9,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,9,0 ],
    [ 0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0 ],
    [ 0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0 ],
    [ 0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0 ],
    [ 0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0 ],
    [ 0,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,0 ],
    [ 0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0 ],
    [ 0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0 ],
    [ 0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0 ],
    [ 0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0 ],
    [ 0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0 ],
    [ 0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0 ],
    [ 0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0 ],
    [ 0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0 ],
    [ 0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0 ],
    [ 0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0 ],
    [ 0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0 ],
    [ 0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0 ],
    [ 0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0 ],
    [ 0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0 ],
    [ 0,9,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,9,0 ],
    [ 0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0 ],
    [ 0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0 ],
    [ 0,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,0 ],
    [ 0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0 ],
    [ 0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0 ],
    [ 0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0 ],
    [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
]

PELLET_PAD = ((16 - 4) / 2 ) - 1

px, py = 0,0
for row in pellet_table:
    px = 0
    for value in row:
        if value == 1:
            xadjusted = px + PELLET_PAD
            yadjusted = py + PELLET_PAD
            screen.blit(pellet, (xadjusted, yadjusted))
        px += xinc
    py += yinc



u = pygame.display.update
u()

running = True
while running:
    clock.tick(10)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

pygame.quit()
