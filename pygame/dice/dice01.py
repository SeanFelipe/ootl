import pygame

screen_dimensions = (640, 480)
BLUE = (0,0,255)
YELLOW = (250,230,140)

screen = pygame.display.set_mode((screen_dimensions))

x = 50
y = 50
w = 100
h = w
CIRCLE_RADIUS = w / 10

square_rect = pygame.Rect(x, y, w, h)

pygame.draw.rect(screen, BLUE, square_rect)
pygame.draw.circle(screen, YELLOW, (100,100), CIRCLE_RADIUS)

pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

