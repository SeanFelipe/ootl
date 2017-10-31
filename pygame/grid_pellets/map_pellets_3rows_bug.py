import pygame
from pygame.transform import scale2x

pygame.init()

SCREEN_WIDTH = (640/3+11)*2
SCREEN_HEIGHT = 248*2
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Pacman MPA')
clock = pygame.time.Clock()

FONT_GREEN = (0,255,0)
FONT_SIZE = 22
font = pygame.font.SysFont(None, FONT_SIZE)

spritesheet = pygame.image.load('spritesheet.png')
start_screen = scale2x(spritesheet.subsurface(0,0, 640/3 + 11, 248))
screen.blit(start_screen, (0,0))

NUM_COLUMNS = 28
NUM_ROWS = 30
LIGHT_GREY = (160,160,160)
LIGHT_GREEN = (84,178,84)
line_color = LIGHT_GREEN

COLUMN_WIDTH = SCREEN_WIDTH / NUM_COLUMNS
ROW_HEIGHT = SCREEN_HEIGHT / NUM_ROWS
#print "column width: ", COLUMN_WIDTH
#print "column height: ", ROW_HEIGHT

linex = 0
for i in range(NUM_COLUMNS):
    linex += COLUMN_WIDTH
    pygame.draw.line(screen, line_color, (linex, 0), (linex, SCREEN_HEIGHT))

liney = 0
for i in range(NUM_ROWS):
    liney += ROW_HEIGHT
    pygame.draw.line(screen, line_color, (0, liney), (SCREEN_WIDTH, liney))


pellets = [
    [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, ],
    [ 0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0 ],
    [ 0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0 ],
]


pellety = 0


for row in pellets:
    row_string = ''
    for value in row:
        row_string += " %i " % value
    row_fonted = font.render(row_string, True, FONT_GREEN)
    screen.blit(row_fonted, (0,0))



#print row_string


#pellety += ROW_HEIGHT



print "screen dimensions: %s" % screen
print "font surface dimensions: %s" % row_fonted

message_text = 'If somebody built it, somebody can unbuild it.'
message = font.render(message_text, True, FONT_GREEN)
#screen.blit(message, (100,100))


u = pygame.display.update
u()

running = True
while running:
    clock.tick(10)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

pygame.quit()
