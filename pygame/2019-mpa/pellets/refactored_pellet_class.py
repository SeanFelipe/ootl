import pygame
from pygame.transform import scale2x

screen = pygame.display.set_mode((300,300))
spritesheet = pygame.image.load('spritesheet.png')

pacman_right = scale2x(spritesheet.subsurface(455, 0, 16, 16))
pacman_left = scale2x(spritesheet.subsurface(455, 16, 16, 16))
pacman_up = scale2x(spritesheet.subsurface(455, 32, 16, 16))
pacman_down = scale2x(spritesheet.subsurface(455, 48, 16, 16))
pacmanx = 50
pacmany = 145

pellet_image = scale2x(scale2x(spritesheet.subsurface(10, 10, 5, 5)))

class Pellet:
    def __init__(self, xpos, ypos):
        self.x = xpos
        self.y = ypos
        self.image = pellet_image
        self.rect = pygame.Rect(xpos, ypos, 20, 20)
        self.show = True



def draw_screen():
    screen.fill((0,0,0))
    screen.blit(pacman, (pacmanx, pacmany))
    if pellet.show:
        screen.blit(pellet.image, (pellet.x, pellet.y))
    pygame.display.update()


def check_for_collision():
    rpac = rect_pacman()
    if rpac.colliderect(pellet.rect):
        print("collision")
        pellet.show = False


def update_positions():
    MOVE_INCREMENT = 5

    global pacmanx, pacmany, moving
    if moving:
        check_for_collision()
        if direction == 'right':
            pacmanx += MOVE_INCREMENT
        if direction == 'left':
            pacmanx -= MOVE_INCREMENT
        if direction == 'up':
            pacmany -= MOVE_INCREMENT
        if direction == 'down':
            pacmany += MOVE_INCREMENT



def handle_events():
    global running, moving, pacman, direction

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYUP:
            moving = False
        elif e.type == pygame.KEYDOWN:
            kname = pygame.key.name(e.key)
            moving = True
            if kname == 'right':
                pacman = pacman_right
                direction = 'right'
            elif kname == 'left':
                pacman = pacman_left
                direction = 'left'
            elif kname == 'up':
                pacman = pacman_up
                direction = 'up'
            elif kname == 'down':
                pacman = pacman_down
                direction = 'down'
            elif kname == 'q':
                running = False


def rect_pacman():
    return pygame.Rect(pacmanx, pacmany, 32, 32)



pellet = Pellet(150, 150)

# global state
pacman = pacman_right
direction = 'right'
moving = False
running = True

# GAME LOOP
while running:
    handle_events()
    update_positions()
    draw_screen()
