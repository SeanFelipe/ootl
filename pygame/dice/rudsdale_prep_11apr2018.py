import pygame

screen_dimensions = (640, 480)
BLUE_ISH = (90,10,255)
YELLOW = (250,230,140)

screen = pygame.display.set_mode((screen_dimensions))
pygame.display.set_caption("Dice ... for great justice")

WIDTH = 100
HEIGHT = WIDTH
CIRCLE_RADIUS = WIDTH / 12


def build_xymap(rect):
    between = rect.width / 4
    xymap = {}
    for i in range(1,4):
        x = rect.x + between
        y = rect.y + ( between * i )
        xymap[i] = (x,y)
    xymap[4] = (rect.x + (between * 2), rect.y + (between * 2))
    for i in range(1,4):
        x = rect.x + (between * 3)
        y = rect.y + (between * i)
        xymap[i+4] = (x,y)
    return xymap

def draw_square(rect):
    pygame.draw.rect(screen, BLUE_ISH, rect)

def draw_circles(numap, xym):
    for key in numap:
        pygame.draw.circle(screen, YELLOW, (xym[key][0], xym[key][1]), CIRCLE_RADIUS)


def base(x,y):
    rect = pygame.Rect(x, y, WIDTH, HEIGHT)
    draw_square(rect)
    xymap = build_xymap(rect)
    return xymap

def side1(x, y):
    xymap = base(x,y)
    draw_circles([4], xymap)


def side2(x, y):
    xymap = base(x,y)
    draw_circles([3,5], xymap)

def side3(x, y):
    xymap = base(x,y)
    draw_circles([3,4,5], xymap)

def side4(x, y):
    xymap = base(x,y)
    draw_circles([1,3,5,7], xymap)

def side5(x, y):
    xymap = base(x,y)
    draw_circles([1,3,4,5,7], xymap)

def side6(x, y):
    xymap = base(x,y)
    draw_circles([1,2,3,5,6,7], xymap)

def all_dots(x, y):
    xymap = base(x,y)
    draw_circles([1,2,3,4,5,6,7], xymap)


side1(50,50)

'''
#side2(175,50)
side1(50,50)
#side1(175,50)
#side1(300,50)
#side1(50,175)
#side1(175,175)
#side1(300,175)
side2(175,50)
side3(300,50)
side4(50,175)
side5(175,175)
side6(300,175)
#all_dots(250, 150)
'''

#base(50,50)
#base(175,50)
#base(300,50)
#base(50,175)
#base(175,175)
#base(300,175)

pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

