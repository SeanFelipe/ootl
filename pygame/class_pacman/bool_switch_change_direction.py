import pygame
from pygame.transform import scale2x

SCREEN_WIDTH = (640/3+11)*2
SCREEN_HEIGHT = 248*2
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Pacman MPA')

spritesheet = pygame.image.load('spritesheet.png')

def get_spritesheet_image(x,y):
    return scale2x(spritesheet.subsurface(x,y,16,16))

pacman_r1 = get_spritesheet_image(455,0)
pacman_r2 = get_spritesheet_image(471,0)
pacman_l1 = get_spritesheet_image(455,16)
pacman_l2 = get_spritesheet_image(471,16)
pacman_u1 = get_spritesheet_image(455,32)
pacman_u2 = get_spritesheet_image(471,32)
pacman_d1 = get_spritesheet_image(455,48)
pacman_d2 = get_spritesheet_image(471,48)

# dictionary collection with two-tuple values
pacman_directions = {
    'right' : (pacman_r1, pacman_r2),
    'left'  : (pacman_l1, pacman_l2),
    'up'    : (pacman_u1, pacman_u2),
    'down'  : (pacman_d1, pacman_d2)
}

class Pacman:
    def __init__(self):
        self.x = 210
        self.y = 360
        self.direction = 'right'
        self.image = pacman_directions[self.direction][0]
        self.first_chomp = True
    def get_rect(self):
        return pygame.Rect(self.x, self.y, 16, 16)
    def change_direction(self, direction):
        self.direction = direction
        index = int(self.first_chomp)
        self.image = pacman_directions[self.direction][index]
    def chomp(self):
        pacman.first_chomp = not pacman.first_chomp
        index = int(self.first_chomp)
        self.image = pacman_directions[self.direction][index]


pacman = Pacman()


MOVEMENT_RATE = 3
moving = False

# GAME LOOP
running = True
while running:
    pygame.display.update()
    screen.fill((0,0,0))
    screen.blit(pacman.image, (pacman.x, pacman.y))

    pacman.chomp()

    if moving:
        if pacman.direction == 'down':
            pacman.y += MOVEMENT_RATE
        if pacman.direction == 'up':
            pacman.y -= MOVEMENT_RATE
        if pacman.direction == 'left':
            pacman.x -= MOVEMENT_RATE
        if pacman.direction == 'right':
            pacman.x += MOVEMENT_RATE

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running= False
            pygame.quit()
        if e.type == pygame.KEYUP:
            moving = False
        if e.type == pygame.KEYDOWN:
            kname = pygame.key.name(e.key)
            if kname in ('right', 'left', 'up', 'down'):
                moving = True
                pacman.change_direction(kname)

