import pygame

GREEN = (0,255,0)
screen = pygame.display.set_mode((640,480))

pygame.init()
font = pygame.font.SysFont(None, 24)

message = 'If somebody built it, somebody can unbuild it.'
text_surface = font.render(message, True, GREEN)

running = True
while running:
    pygame.display.update()

    screen.blit(text_surface, (50,50))


    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
