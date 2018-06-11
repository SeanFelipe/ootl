import pygame

screen_dimensions = (640, 480)
screen = pygame.display.set_mode((screen_dimensions))

pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

