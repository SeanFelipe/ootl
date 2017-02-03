import pygame
import sys

screen = pygame.display.set_mode((640,480))

# this gets you a red square, with a white dot in the middle
# CHALLENGE:
# - make all six sides of a six-sided die
# - change the DICE_SIDE_LENGTH amount and have the circle adjust automatically
DICE_SIDE_LENGTH = 100

# https://www.pygame.org/docs/ref/surface.html
side1 = pygame.Surface((DICE_SIDE_LENGTH, DICE_SIDE_LENGTH))
side1.fill((255,0,0)) # red, green, blue

# uncomment and update the position for side 2
# but why doesn't it display?
#side2 = pygame.Surface((DICE_SIDE_LENGTH, DICE_SIDE_LENGTH))
#side2.fill((255,0,0)) # red, green, blue

# https://www.pygame.org/docs/ref/draw.html
pygame.draw.circle(red_square, (255,255,255), (50,50), 10)

# get to know Surface and Surface.blit()
# https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit
screen.blit(red_square, (0,0))

# always need this to make stuff actually update! Think like a computer!
u = pygame.display.update
u()

# this gets us a screen that sticks around, until we click the X window button
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
