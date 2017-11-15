import pygame
from pygame.transform import scale2x

pygame.init()
SCREEN_WIDTH = (640/3+11)*2
SCREEN_HEIGHT = 248*2
screen = pygame.display.set_mode((900,900))

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Pacman MPA')
clock = pygame.time.Clock()

FONT_GREEN = (0,255,0)
FONT_SIZE = 18
font = pygame.font.SysFont(None, FONT_SIZE)

spritesheet = pygame.image.load('spritesheet.png')
sw, sh = screen.get_width(), screen.get_height()
ssw, ssh = spritesheet.get_width(), spritesheet.get_height()
maze = scale2x(spritesheet.subsurface(0,0, 640/3 + 11, 248))

blank_grid_padx = 15
blank_grid_startx = (640 / 3) + blank_grid_padx
blank_screen = scale2x(spritesheet.subsurface(blank_grid_startx ,0, 640/3 + 11, 248))


pellet = scale2x(spritesheet.subsurface(10, 10, 4, 4))
power_pellet = scale2x(spritesheet.subsurface(7, 23, 10, 10))

maze=scale2x(spritesheet.subsurface((228,0,224,248)))
MW= maze.get_width()
MH= maze.get_height()

Speedy= scale2x(spritesheet.subsurface ((ssw / 3 * 2) + 5, 80, 14, 16))
Bashful = scale2x(spritesheet.subsurface ((ssw / 3 * 2) + 5, 96, 14, 16))
Pokey = scale2x(spritesheet.subsurface ((ssw / 3 * 2) + 5, 112, 14, 16))
Shadow = scale2x(spritesheet.subsurface ((ssw / 3 * 2) + 5, 64, 14, 16))

def get_spritesheet_image(x,y):
    return scale2x(spritesheet.subsurface(x,y,16,16))

pacman_1r = get_spritesheet_image(455,0)
pacman_2r = get_spritesheet_image(471,0)
pacman_1l = get_spritesheet_image(455,16)
pacman_2l = get_spritesheet_image(471,16)
pacman_1u = get_spritesheet_image(455,32)
pacman_2u = get_spritesheet_image(471,32)
pacman_1d = get_spritesheet_image(455,48)
pacman_2d = get_spritesheet_image(471,48)

pacman_directions = {
    'right' : (pacman_1r, pacman_2r),
    'left'  : (pacman_1l, pacman_2l),
    'up'    : (pacman_1u, pacman_2u),
    'down'  : (pacman_1d, pacman_2d),
}

#Adjustments/ Variables
PELLET_PAD = (16-4)/2
pac_adjx, pac_adjy = 15, 30

pacman_startx, pacman_starty = MW/2-pac_adjx, MH*2/3+pac_adjy
print pacman_startx, pacman_starty

MOVEMENT_RATE = 3


class ThinSprite:
    def __init__(self, surface, startx, starty):
        self.image = surface
        self.x, self.y = startx, starty
        self.direction = 'right'

pacman = ThinSprite(pacman_2r, pacman_startx, pacman_starty)




# load starting pellet data from pellet_table.py
import pellet_table
pellets = pellet_table.data


def draw_pacman():
    img = pacman_directions[pacman.direction][anim_index]
    screen.blit(img, (pacman.x,pacman.y))


def draw_pellets():
    xinc = 16
    yinc = 16
    px, py = 0,0
    for row in pellets:
        px =0
        for value in row:
            if value == 1:
                xadjusted = px + PELLET_PAD
                yadjusted = py + PELLET_PAD
                screen.blit(pellet, (xadjusted, yadjusted))
            elif value == 9:
                screen.blit(power_pellet, (px, py))
            px += xinc
        py  += yinc




def draw_maze():
    screen.fill((0,0,0))
    screen.blit(maze, (0,0))


def draw_ghosts():
    screen.blit (Speedy, (MW/2-45, MH/2-30))
    screen.blit (Bashful, (MW/2-15, MH/2-30))
    screen.blit (Pokey, (MW/2+15, MH/2-30))
    screen.blit (Shadow, (MW/2-15, MH/2-80))




running = True
moving = False
while running:
    pygame.display.update()
    draw_maze()
    draw_pellets()
    draw_ghosts()
    draw_pacman()

    if moving:
        anim_change_count += 1
        if anim_change_count == ANIM_CHANGE_THRESHOLD:
            if anim_index == 0:
                anim_index = 1
            else:
                anim_index = 0
            anim_change_count = 0
        if pacman.direction == 'down':
            pacman.y += MOVEMENT_RATE
        if pacman.direction == 'up':
            pacman.y -= MOVEMENT_RATE
        if pacman.direction == 'left':
            pacman.x -= MOVEMENT_RATE
        if pacman.direction == 'right':
            pacman.x += MOVEMENT_RATE

    for e in pygame.event.get():
        if e.type ==pygame.QUIT:
            running= False
            pygame.quit()
        if e.type == pygame.KEYUP:
            moving = False
        if e.type == pygame.KEYDOWN:
            moving = True

            key = e.key

            kname = pygame.key.name(e.key)
            if kname in ('right', 'left', 'up', 'down'):
                moving= True
                pacman.direction = kname

