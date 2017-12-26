import pygame
from pygame.transform import scale2x

SCREEN_WIDTH = (640/3+11)*2
SCREEN_HEIGHT = 248*2
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Pacman MPA')

spritesheet = pygame.image.load('spritesheet.png')

def get_spritesheet_image(x,y):
    return scale2x(spritesheet.subsurface(x,y,16,16))

pacman_r = get_spritesheet_image(455,0)
pacman_l = get_spritesheet_image(455,16)
pacman_u = get_spritesheet_image(455,32)
pacman_d = get_spritesheet_image(455,48)

pacman_images = {
    'right' :  pacman_r,
    'left'  :  pacman_l,
    'up'    :  pacman_u,
    'down'  :  pacman_d,
}


class Pacman:
    def __init__(self):
        self.x = 210
        self.y = 360
        self.direction = 'right'
        self.image = pacman_directions[self.direction]
        self.first_chomp = True
    def get_rect(self):
        return pygame.Rect(self.x, self.y, 16, 16)
    def change_direction(self, direction):
        self.direction = direction
        if direction == 'right':
            self.image = pacman_r
        elif direction == 'left':
            self.image = pacman_l
        elif direction == 'up':
            self.image = pacman_u
        elif direction == 'down':
            self.image = pacman_d


pacman = Pacman()


MOVEMENT_RATE = 3
running = True
moving = False
while running:
    pygame.display.update()
    screen.fill((0,0,0))
    screen.blit(pacman.image, (pacman.x, pacman.y))

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

