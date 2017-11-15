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
print blank_grid_startx
blank_screen = scale2x(spritesheet.subsurface(blank_grid_startx ,0, 640/3 + 11, 248))


pellet = scale2x(spritesheet.subsurface(10, 10, 4, 4))
power_pellet = scale2x(spritesheet.subsurface(7, 23, 10, 10))



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
        elif value == 9:
            screen.blit(power_pellet, (px, py))
        px += xinc
    py += yinc


sw, sh = screen.get_width(), screen.get_height()
ssw, ssh = spritesheet.get_width(), spritesheet.get_height()
print ssw, ssh
xpad = 3
pacman = scale2x(spritesheet.subsurface((ssw / 3 * 2) + 3, 0, 16, 16))

blinky = scale2x(spritesheet.subsurface((ssw / 3 * 2) + 3, 16 * 4, 16, 16))
pinky = scale2x(spritesheet.subsurface((ssw / 3 * 2) + 3, 16 * 5, 16, 16))
inky = scale2x(spritesheet.subsurface((ssw / 3 * 2) + 3, 16 * 6, 16, 16))
clyde = scale2x(spritesheet.subsurface((ssw / 3 * 2) + 3, 16 * 7, 16, 16))


ghostx = sw / 2 - 50
ghosty = sh / 2 - 32

blinkyx = ghostx + 31
blinkyy = ghosty - 47

# a bunch of math but it makes sense, sort of
# as long as Pacman is in the right place we're happy
pacx = screen.get_width() / 2 - 16
pacy = (screen.get_height() / 4 * 3) - 11

print pacx, pacy
screen.blit(pacman, (pacx, pacy))

GINC = 32
screen.blit(blinky, (blinkyx, blinkyy))
screen.blit(pinky, (ghostx, ghosty))
screen.blit(inky, (ghostx + GINC, ghosty))
screen.blit(clyde, (ghostx + GINC * 2, ghosty))





u = pygame.display.update
u()

running = True
while running:
    clock.tick(10)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

pygame.quit()
