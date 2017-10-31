import pygame

screen_dimensions = (640, 480)
BLUE_ISH = (90,10,255)
BLUE  = (0,0,255)
YELLOW = (250,230,140)
LINE_COLOR = (119, 161, 229)
line_width = 4

screen = pygame.display.set_mode((screen_dimensions))

WIDTH = 100
HEIGHT = WIDTH
CIRCLE_RADIUS = WIDTH / 12


clock = pygame.time.Clock()

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
    pygame.draw.rect(screen, BLUE, rect)

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


'''
side2(175,50)
side1(50,50)
side1(175,50)
side1(300,50)
side1(50,175)
side1(175,175)
side1(300,175)
side2(175,50)
side3(300,50)
side4(50,175)
side5(175,175)
side6(300,175)
all_dots(250, 150)
'''


def draw_side(num, x, y):
    exec("side%i(x,y)" % num)

sw = screen_dimensions[0]
sh = screen_dimensions[1]
num_cols = 4
num_rows = 3
xinc = sw / num_cols
yinc = sh / num_rows

for row in range(num_rows -1):
    y_initial = yinc * (row + 1)
    y = y_initial - (line_width /2)
    pygame.draw.line(screen, LINE_COLOR, (0,y), (sw, y), line_width)

for col in range(num_cols -1):
    x_initial = xinc * (col + 1)
    x = x_initial - (line_width /2)
    pygame.draw.line(screen, LINE_COLOR, (x,0), (x, sh), line_width)

for row in range(num_rows):
    y = yinc * (row + 1)
    for col in range(num_cols):
        x = xinc * (col + 1)
        squarex = x - (WIDTH / 2)
        squarey = y - (WIDTH / 2)
        side_number = (row +1) * (col +1)
        #draw_side(side_number, squarex,squarey)

for i in range(1,4):
    x = xinc * i
    pygame.draw.circle(screen, (255,0,0), (x,yinc), 40)

for i in range(1,4):
    x = xinc * i
    pygame.draw.circle(screen, (255,0,0), (x,yinc*2), 40)


print xinc, yinc
xygrid = []   # square brackets are Python lists

for i in range(2):
    for j in range(3):
        circley = (i + 1) * yinc
        circlex = (j + 1) * xinc
        # now add to xygrid
        xygrid.append((circlex, circley))

print xygrid


pygame.display.update()


while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

