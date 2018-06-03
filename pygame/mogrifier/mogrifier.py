import pygame
import time
#from pygame import set_trace

pygame.init()
clock = pygame.time.Clock()

FONT_SIZE = 16
FONT_GREEN = (0,255,0)
font = pygame.font.SysFont(None, FONT_SIZE)

#SF2 = '60224.png'
SF2 = 'saved_1528035307.png'
#full = pygame.image.load(SF2)
#fullw, fullh = full.get_width(), full.get_height()
#ss = full.subsurface((fullw/4 -75,100,fullw/3 + 100,fullh/5))
ss = pygame.image.load(SF2)
sw, sh = ss.get_width(), ss.get_height()


screen = pygame.display.set_mode((sw,sh))

rx, ry = 0,0
rw = 16
rh = 16
rthickness = 2
INC = 2

rcolor = (175,175,175)

expanding = False
translating = False
kex = None

def store_subsurface_image(rx, ry, rw, rh):
    sub = ss.subsurface((rx, ry, rw, rh))
    fn = "saved_%s.png" % int(time.time())
    pygame.image.save(sub, fn)


running = True
while running:
    clock.tick(20)
    pygame.display.update()
    screen.blit(ss, (0,0))
    pygame.draw.rect(screen, rcolor, (rx, ry, rw, rh), rthickness)
    rc = pygame.Rect(rx, ry, rw, rh)
    rect_fonted = font.render(str(rc), True, FONT_GREEN)
    screen.blit(rect_fonted, (5,5))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            kname = pygame.key.name(e.key)
            if kname == 'q':
                running = False
            elif kname == 'p':
                print "current rect: " + str(rc)
            elif kname == 'k':
                store_subsurface_image(rx, ry, rw, rh)
            elif kname in ('right','down','left','up'):
                expanding = True
                kex = kname
            elif kname in ('w','a','s','d'):
                translating = True
                ktr = kname
        elif e.type == pygame.KEYUP:
            kname = pygame.key.name(e.key)
            if kname in ('right','down','left','up'):
                expanding = False;
                kex = None
            elif kname in ('w','a','s','d'):
                translating = False
                ktr = None
        elif e.type == pygame.MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos()
            rx = mpos[0]
            ry = mpos[1]
            expanding = False
            translating = False

    if translating:
        if ktr == 'd':
            rx += INC
        elif ktr == 's':
            ry += INC
        elif ktr == 'a':
            rx -= INC
        elif ktr == 'w':
            ry -= INC

    if expanding:
        if kex == 'right':
            rw += INC
        elif kex == 'down':
            rh += INC
        elif kex == 'left':
            rw -= INC
        elif kex == 'up':
            rh -= INC



pygame.quit()
