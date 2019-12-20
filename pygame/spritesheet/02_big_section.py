import pygame
import sys

screen = pygame.display.set_mode((680,480))
spritesheet = pygame.image.load('spritesheet.png')
screen.blit(spritesheet, (0,0))

pacman_r = spritesheet.subsurface((455,0,16,16))
pacman_l = spritesheet.subsurface((455,16,16,16))
pacman_u = spritesheet.subsurface((455,32,16,16))
pacman_d = spritesheet.subsurface((455,48,16,16))

screen.blit(pacman_r, (455,325))
screen.blit(pacman_l, (475,325))
screen.blit(pacman_u, (495,325))
screen.blit(pacman_d, (515,325))



u = pygame.display.update
u()

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif e.type == pygame.KEYDOWN:
            kname = pygame.key.name(e.key)
            if kname == 'q':
                running = False
