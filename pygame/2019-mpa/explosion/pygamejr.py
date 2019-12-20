# 3 Oct 2019
import pygame

RED = (255,0,0)
red = RED
GREEN = (0,255,0)
green = GREEN
BLUE = (0,0,255)
blue = BLUE

def update():
    pygame.display.update()


def start(res=(640,480)):
    global screen
    global font
    screen = pygame.display.set_mode(res)
    pygame.font.init()
    font = pygame.font.SysFont('Arial', 30)
    #print pygame.font.get_fonts()
    wait(250)
    return screen


def loop():
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.KEYDOWN:
                if pygame.key.name(e.key) == 'q':
                    running = False
        pygame.display.update()
    pygame.quit()


def clear():
    screen.fill((0,0,0))
    update()


def rect(color, xy, wh):
    pygame.draw.rect(screen, color, (xy, wh))
    update()


def circle(color, xy, radius):
    pygame.draw.circle(screen, color, xy, radius)
    update()


def wait(ms):
    pygame.time.wait(ms)

def write(t, xy, color=GREEN):
    s = font.render(t, True, color)
    screen.blit(s, xy)
    pygame.display.update()
