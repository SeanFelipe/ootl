import pygame
from pygame.transform import scale2x

pygame.display.set_caption('MPAPMFTW')
pygame.init()

spritesheet = scale2x(pygame.image.load('spritesheet.png'))
sw, sh = spritesheet.get_width(), spritesheet.get_height()
#screen = pygame.display.set_mode((sw,sh))
screen = pygame.display.set_mode((640,480))
spritesheet.convert()
spritesheet.set_colorkey((0,0,0))

BLUE_WALL_COLOR = (33, 33, 255, 255)
YELLOW_GREEN = (154,205,50)

#screen.blit(spritesheet, (0,0))
#screen = pygame.display.set_mode((sw / 3,sh))

maze = spritesheet.subsurface((sw /3,0,sw / 3, sh))
#screen.blit(maze, (0,0))

PSIZE = 32
xpad = 6
pacman_r = spritesheet.subsurface((sw / 3 * 2 + xpad, 0, PSIZE, PSIZE)).convert()
pacman_l = spritesheet.subsurface((sw / 3 * 2 + xpad, PSIZE -1, PSIZE, PSIZE)).convert()
pacman_u = spritesheet.subsurface((sw / 3 * 2 + xpad, PSIZE * 2 -1, PSIZE, PSIZE)).convert()
pacman_d = spritesheet.subsurface((sw / 3 * 2 + xpad, PSIZE * 3 -1, PSIZE, PSIZE)).convert()

ptrimx = 18
ptrimy = 17
#pstartx = ( sw / 3 / 2 ) - ptrimx # one-third spritesheet width, and half again of that, then trim
#pstarty = ( sh / 2 ) + ptrimy # half screen height
pstartx = 50
pstarty = 262

clock = pygame.time.Clock()


class ThinSprite:
    def __init__(self, surface, startx, starty):
        self.image = surface
        self.rect = self.image.get_rect()
        self.x, self.y = startx, starty
        self.direction = 'right'
    def get_center(self):
        rect = pygame.Rect(self.x, self.y, self.rect.width, self.rect.height)
        return rect.center
    def get_rect(self):
        x = self.x
        y = self.y
        w = self.image.get_width()
        h = self.image.get_height()
        rect = pygame.Rect(x, y, w, h)
        return rect
    def get_pixels_ahead(self, ahead=1):
        rect = pygame.Rect(self.x, self.y, self.rect.width, self.rect.height)
        xy_ahead = []
        if self.direction == 'right':
            xy_ahead = (rect.midright[0] + ahead, rect.midright[1])
        if self.direction == 'left':
            xy_ahead = (rect.midleft[0] - ahead, rect.midleft[1])
        if self.direction == 'up':
            xy_ahead = (rect.midtop[0], rect.midtop[1] - ahead)
        if self.direction == 'down':
            xy_ahead = (rect.midbottom[0], rect.midbottom[1] + ahead)
        return xy_ahead



pacman = ThinSprite(pacman_r, pstartx, pstarty)

points_list = [(200,300), (400,300), (400, 50)]
points_list_2 = [(200,250), (350,250), (350, 50)]

#screen.fill((127,127,127))

u = pygame.display.update
u()

peninsula = [ 640 / 4, 480 / 3, 640 / 2, 480 / 3 ]

MOVE_INCREMENT = 4




print '-----------------------------------'
print pacman.image
print '-----------------------------------'

# GAME LOOP
running = True
moving = False
while running:

    pacman_rect = pygame.Rect(pacman.x, pacman.y, 32, 32)
    print '-----------------------------------'
    print 'pacman_rect midright:', pacman_rect.midright
    print 'x value:', pacman_rect.midright[0]
       

    u()
    clock.tick(30)
    #screen.blit(spritesheet, (0,0))
    screen.fill((0,0,0))
    #screen.fill((255,255,255))
    screen.blit(pacman.image, (pacman.x, pacman.y))

    pygame.draw.lines(screen, BLUE_WALL_COLOR, False, points_list, 5)
    pygame.draw.lines(screen, BLUE_WALL_COLOR, False, points_list_2, 5)
    #pygame.draw.rect(screen, BLUE_WALL_COLOR, peninsula)





    pygame.draw.rect(screen, YELLOW_GREEN, (pacman.x, pacman.y, pacman.image.get_width(), pacman.image.get_height()), 3)

    if moving:
        if pacman.direction == 'right':
            pacman.image = pacman_r
            pacman.x += MOVE_INCREMENT
        if pacman.direction == 'left':
            pacman.image = pacman_l
            pacman.x -= MOVE_INCREMENT
        if pacman.direction == 'up':
            pacman.image = pacman_u
            pacman.y -= MOVE_INCREMENT
        if pacman.direction == 'down':
            pacman.image = pacman_d
            pacman.y += MOVE_INCREMENT
        xy_ahead = pacman.get_pixels_ahead()
        color_ahead = screen.get_at(xy_ahead)
        print "color ahead is:", color_ahead
        #if color_ahead == BLUE_WALL_COLOR:
            #print 'color_ahead is BLUE_WALL_COLOR'
            #moving = False

    pygame.draw.circle(screen, (255,0,0), pacman_rect.midright, 2)
    #pygame.draw.circle(screen, (255,200,200), pacman.get_pixels_ahead(15), 5)
    if pacman.direction == 'right':
        pacman.image = pacman_r
        #pygame.draw.circle(screen, (255,0,0), pacman.get_rect().midright, 2)
    if pacman.direction == 'left':
        pacman.image = pacman_l
        #pygame.draw.circle(screen, (255,0,0), pacman.get_rect().midleft, 2)
    if pacman.direction == 'up':
        pacman.image = pacman_u
        #pygame.draw.circle(screen, (255,0,0), pacman.get_rect().midtop, 2)
    if pacman.direction == 'down':
        pacman.image = pacman_d
        #pygame.draw.circle(screen, (255,0,0), pacman.get_rect().midbottom, 2)



    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            kname = pygame.key.name(e.key)
            if kname == 'q':
                running = False
            if kname == 's':
                moving = False
            if kname in ('right','left','up','down'):
                moving = True
                pacman.direction = kname
        elif e.type == pygame.KEYUP:
            moving = False


pygame.quit()
