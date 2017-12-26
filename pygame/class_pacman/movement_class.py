import pygame
import sys

screen = pygame.display.set_mode((680,480))
pygame.display.set_caption('Pacman MPA')
# returns a Surface
spritesheet = pygame.image.load('spritesheet.png')
start_screen = spritesheet.subsurface(0,0, 640/3 + 11, 248)
screen.blit(start_screen, (0,0))
screen.blit(spritesheet, (0,0))
# get the pacman image
# study this method to find the argument sequence
# https://www.pygame.org/docs/ref/surface.html#pygame.Surface.subsurface
# then add the correct arguments to Surface.subsurface() to get a pacman image
prepacman = spritesheet.subsurface(680 / 3 * 2, 0, 16, 16)
preblinky = spritesheet.subsurface(680 / 3 * 2, 64, 16, 16)
prepinky = spritesheet.subsurface(680 / 3 * 2, 80, 16, 16)
preinky = spritesheet.subsurface(680 / 3 * 2, 96, 16, 16)
preclyde = spritesheet.subsurface(680 / 3 * 2, 112, 16, 16)
pacman = pygame.transform.scale2x(prepacman)
blinky = pygame.transform.scale2x(preblinky)
pinky = pygame.transform.scale2x(prepinky)
inky = pygame.transform.scale2x(preinky)
clyde = pygame.transform.scale2x(preclyde)
screen.blit(pacman, (30, 400))
screen.blit(blinky, (70, 400))
screen.blit(pinky, (110, 400))
screen.blit(inky, (150, 400))
screen.blit(clyde, (200, 400))

print spritesheet

u = pygame.display.update
u()

class Pacman:
    def __init__(self):
        self.x = 210
        self.y = 360
        self.image = pacman_r
        self.direction = 'right'
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



running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
