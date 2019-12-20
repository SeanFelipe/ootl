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

pellet = scale2x(scale2x(spritesheet.subsurface(10, 10, 5, 5)))
pelletx = 150
pellety = 150


def draw_screen():
    screen.fill((0,0,0))
    screen.blit(pacman, (pacmanx, pacmany))
    screen.blit(pellet, (pelletx, pellety))
    pygame.display.update()


def handle_events():
    global running
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False


# global game state
pacman = pacman_right
running = True

# GAME LOOP
while running:
    draw_screen()
    handle_events()

