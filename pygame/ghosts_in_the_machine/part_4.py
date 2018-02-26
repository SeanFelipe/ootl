import pygame
from pygame.transform import scale2x
from ghosts import Ghost
from pdb import set_trace


SCREEN_WIDTH = (640/3+11)*2
SCREEN_HEIGHT = 248*2
WHITE = (255,255,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
BRIGHT_RED = (245,50,41)
DOT_COLOR = (255,200,200)
BLUE_WALL_COLOR = (33,33,255,255)
DOT_SIZE = 3

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Ghosts in the Machine')

spritesheet = pygame.image.load('spritesheet.png')
blank_maze = scale2x(spritesheet.subsurface((228,0,224,248)))

def get_spritesheet_image(x,y,w=16,h=16):
    return scale2x(spritesheet.subsurface(x,y,w,h))

pacman_r1 = get_spritesheet_image(457,1,9,13)
pacman_r2 = get_spritesheet_image(473,1,12,13)
pacman_l1 = get_spritesheet_image(461,17,9,13)
pacman_l2 = get_spritesheet_image(474,17,12,13)
pacman_u1 = get_spritesheet_image(457,37,13,9)
pacman_u2 = get_spritesheet_image(473,34,13,12)
pacman_d1 = get_spritesheet_image(457,49,13,9)
pacman_d2 = get_spritesheet_image(473,49,13,12)



pacman_directions = {
    'right' : (pacman_r1, pacman_r2),
    'left'  : (pacman_l1, pacman_l2),
    'up'    : (pacman_u1, pacman_u2),
    'down'  : (pacman_d1, pacman_d2)
    }


class Pacman:
    def __init__(self):
        self.x = 210
        self.y = 362
        self.direction = 'right'
        self.image = pacman_directions[self.direction][1]
        self.first_chomp = True
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
    def set_direction(self, direction):
        self.direction = direction
        index = int(self.first_chomp)
        self.image = pacman_directions[self.direction][index]
    def chomp(self):
        pacman.first_chomp = not pacman.first_chomp
        index = int(self.first_chomp)
        self.image = pacman_directions[self.direction][index]
    def get_dots_ahead(self, ahead=1):
        rect = self.get_rect()
        dots_ahead = []
        dots_ahead.append((rect.midright[0] + ahead, rect.midright[1]))
        dots_ahead.append((rect.midleft[0] - ahead, rect.midleft[1]))
        dots_ahead.append((rect.midtop[0], rect.midtop[1] - ahead))
        dots_ahead.append((rect.midbottom[0], rect.midbottom[1] + ahead))
        return dots_ahead
    def dots_corners(self):
        dots_corners = []
    def get_dots_xy(self, ahead=0):
        da = self.get_dots_ahead(ahead)
        out = {
            'up'     : da[2],
            'right'  : da[0],
            'down'   : da[3],
            'left'   : da[1],
        }
        return out

pacman = Pacman()

blinky = Ghost('blinky', 205, 169)
pinky = Ghost('pinky', 50,50)
inky = Ghost('inky', 50,50)
clyde = Ghost('clyde', 50,50)


MOVEMENT_RATE = 3
moving = False

running = True
while running:

    clock.tick(30)
    pygame.display.update()
    screen.blit(blank_maze, (0,0))
    #screen.blit(pacman.image, (pacman.x, pacman.y))
    screen.blit(blinky.image, (blinky.x, blinky.y))

    if moving:
        if pacman.direction == 'down':
            pacman.y += MOVEMENT_RATE
        if pacman.direction == 'up':
            pacman.y -= MOVEMENT_RATE
        if pacman.direction == 'left':
            pacman.x -= MOVEMENT_RATE
        if pacman.direction == 'right':
            pacman.x += MOVEMENT_RATE




    blinky.move()
    blinky.check_for_wall(screen)
    # we'll be moving the other ghosts too.
    # some repetition here we might want to clean up, maybe with a SpriteGroup.
    #inky.move()
    #pinky.move()
    #clyde.move()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYUP:
            moving = False
        if e.type == pygame.KEYDOWN:
            kname = pygame.key.name(e.key)
            if kname == 'q':
                running = False
            if kname == 's':
                blinky.moving = not blinky.moving
            if kname in ('right', 'left', 'up', 'down'):
                blinky.moving = True
                blinky.set_direction(kname)


pygame.quit()
