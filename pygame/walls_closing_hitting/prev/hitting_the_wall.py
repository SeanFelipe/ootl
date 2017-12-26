import pygame
from pygame.transform import scale2x

SCREEN_WIDTH = (640/3+11)*2 + 100
SCREEN_HEIGHT = 248*2
WHITE = (255,255,255)
BLACK = (0,0,0)
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Hitting the Wall')

spritesheet = pygame.image.load('spritesheet.png')
blank_maze = scale2x(spritesheet.subsurface((228,0,224,248)))

def get_spritesheet_image(x,y,w=16,h=16):
    return scale2x(spritesheet.subsurface(x,y,w,h))

pacman_r1 = get_spritesheet_image(457,1,9,13)
starty1 = 20
pacman_r2 = get_spritesheet_image(473,1,12,13)
starty2 = starty1 + 60
pacman_l1 = get_spritesheet_image(461,17,9,13)
starty3 = starty1 + 110
pacman_l2 = get_spritesheet_image(474,17,12,13)
starty4 = starty1 + 160
pacman_u1 = get_spritesheet_image(457,37,13,9)
starty5 = starty1 + 210
pacman_u2 = get_spritesheet_image(473,34,13,12)
starty6 = starty1 + 260
pacman_d1 = get_spritesheet_image(457,49,13,9)
starty7 = starty1 + 310
pacman_d2 = get_spritesheet_image(473,49,13,12)
starty8 = starty1 + 360


pacman_images = {
    'right' :  pacman_r1,
    'left'  :  pacman_l1,
    'up'    :  pacman_u1,
    'down'  :  pacman_d1,
}


class ThinSprite:
    def __init__(self, startx, starty):
        self.x, self.y = startx, starty
        self.direction = 'right'
        self.image = pacman_images[self.direction]
    def set_direction(self, direction):
        self.direction = direction
        self.image = pacman_images[direction]


pacman_startx = 20
pstartx = pacman_startx
pacman_starty = SCREEN_HEIGHT /2 - 32
pacman = ThinSprite(pacman_startx, pacman_starty)


MOVEMENT_RATE = 3
running = True
moving = False
while running:
    pygame.display.update()
    screen.fill(WHITE)
    #screen.fill(BLACK)
    screen.blit(blank_maze, (99,0))
    screen.blit(pacman_r1, (pstartx, starty1))
    screen.blit(pacman_r2, (pstartx, starty2))
    screen.blit(pacman_l1, (pstartx, starty3))
    screen.blit(pacman_l2, (pstartx, starty4))
    screen.blit(pacman_u1, (pstartx, starty5))
    screen.blit(pacman_u2, (pstartx, starty6))
    screen.blit(pacman_d1, (pstartx, starty7))
    screen.blit(pacman_d2, (pstartx, starty8))
    #screen.blit(p2, (pacman_startx, pacman_starty + 50))

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
        if e.type == pygame.KEYUP:
            moving = False
        if e.type == pygame.KEYDOWN:
            kname = pygame.key.name(e.key)
            if kname == 'q':
                running = False
            if kname in ('right', 'left', 'up', 'down'):
                moving = True
                pacman.set_direction(kname)


pygame.quit()
