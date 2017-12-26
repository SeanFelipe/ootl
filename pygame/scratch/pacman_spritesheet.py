import pygame

screen = pygame.display.set_mode((680,480))
pygame.display.set_caption('Pacman MPA')
spritesheet = pygame.image.load('spritesheet.png')
screen.blit(spritesheet, (0,0))

u = pygame.display.update
u()

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
