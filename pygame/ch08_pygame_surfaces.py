import pygame
import sys

screen = pygame.display.set_mode((640,480))

red_square = pygame.Surface((100,100))
red_square.fill((255,0,0))
pygame.draw.circle(red_square, (0,0,0), (50,50), 20)

screen.blit(red_square, (0,0))

u = pygame.display.update
u()

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
