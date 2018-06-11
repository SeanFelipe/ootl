import pygame
#from pygame import set_trace


pygame.init()
screen = pygame.display.set_mode((900,600))

#fn = 'IoriYagamiv.2.png'
fn = 'ryu_spritesheet.png'
img = pygame.image.load(fn)
color = None


running = True
while running:
    pygame.display.update()
    screen.fill((0,0,255))
    screen.blit(img, (50,50))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos()
            rx = mpos[0]
            ry = mpos[1]
            colorkey = screen.get_at((rx, ry))
            print "color at click: " + str(colorkey)
            running = False

w, h = img.get_width(), img.get_height()

destination = pygame.Surface((w, h)).convert_alpha()


colorkey = pygame.Color(0,0,248,255)

for yy in range(h):
    for xx in range(w):
        destination_color = None
        loaded_color = img.get_at((xx,yy))
        print "%i %i loaded color: %s" % (xx, yy, str(loaded_color))
        if loaded_color == colorkey:
            destination_color = pygame.Color(0,0,0,0)
            print 'color updated'
        else:
            destination_color = loaded_color
        destination.set_at((xx,yy), destination_color)

running = True
while running:
    pygame.display.update()
    screen.fill((0,0,0))
    #screen.blit(img, (50,50))
    screen.blit(destination, (0,0))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False


pygame.image.save(destination, 'output.png')

pygame.quit()
