import pygame
import sys

screen = pygame.display.set_mode((680,480))
pygame.display.set_caption('Pacman MPA')
# returns a Surface
spritesheet = pygame.image.load('spritesheet.png')
start_screen = spritesheet.subsurface(0,0, 640/3 + 11, 248)
screen.blit(start_screen, (0,0))
# get the pacman image
# study this method to find the argument sequence
# https://www.pygame.org/docs/ref/surface.html#pygame.Surface.subsurface
# then add the correct arguments to Surface.subsurface() to get a pacman image
xpad = 3
pacman = spritesheet.subsurface(680 / 3 * 2 + xpad, 0, 16, 16)
blinky = spritesheet.subsurface(680 / 3 * 2 + xpad, 64, 16, 16)
pinky = spritesheet.subsurface(680 / 3 * 2 + xpad, 80, 16, 16)
inky = spritesheet.subsurface(680 / 3 * 2 + xpad, 96, 16, 16)
clyde = spritesheet.subsurface(680 / 3 * 2 + xpad, 112, 16, 16)

ghosty = 280
ghostx = 30

screen.blit(pacman, (ghostx + 30, ghosty))
screen.blit(blinky, (ghostx + 50, ghosty))
screen.blit(pinky, (ghostx + 70, ghosty))
screen.blit(inky, (ghostx + 90, ghosty))
screen.blit(clyde, (ghostx + 110, ghosty))

print spritesheet

u = pygame.display.update
u()

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
