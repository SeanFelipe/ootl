import pygame
import time
import os
import fnmatch
from pdb import set_trace

# change this to match your prefix from mogrifier
ANIM_SERIES_NAME = 'flip'



pygame.init()
clock = pygame.time.Clock()

FONT_SIZE = 16
FONT_GREEN = (0,255,0)
font = pygame.font.SysFont(None, FONT_SIZE)

anim_surfs = []
widest, tallest = 0,0

for fn in os.listdir('.'):
    if fnmatch.fnmatch(fn, "%s*" % ANIM_SERIES_NAME):
        sub = pygame.image.load(fn)
        sw, sh = sub.get_width(), sub.get_height()
        print 'loaded image w dimensions: ', sw, sh
        if sw > widest:
            widest = sw
        if sh > tallest:
            tallest = sh
        anim_surfs.append(sub)

#set_trace()

fw = widest * len(anim_surfs)
fh = tallest

final_surf = pygame.Surface((fw, fh))

screen = pygame.display.set_mode((fw,fh))
for ii, surf in enumerate(anim_surfs):
    dx = widest * ii
    final_surf.blit(surf, (dx, 0))

running = True
while running:
    clock.tick(20)
    pygame.display.update()
    screen.blit(final_surf, (0,0))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            kname = pygame.key.name(e.key)
            if kname == 'q':
                running = False
