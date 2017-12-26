import pygame
from pygame.transform import scale2x

screen = pygame.display.set_mode((500,300))
spritesheet = pygame.image.load('../spritesheet.png')

xpad = 4
pacman_right = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 0, 16, 16))
pacman_left = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 16, 16, 16))
pacman_up = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 32, 16, 16))
pacman_down = scale2x(spritesheet.subsurface(680 / 3 * 2 + xpad, 48, 16, 16))

pacman_x = 50
pacman_y = 50
facing = pacman_right

INCREMENT = 2
direction = 'right'
moving = False

running = True
while running:
    pygame.display.update()

    if moving:
        if direction == 'right':
            pacman_x += INCREMENT
        '''
        if direction == 'left':
            pacman_x -= INCREMENT
        if direction == 'up':
            pacman_y -= INCREMENT
        if direction == 'down':
            pacman_y += INCREMENT
        '''

    screen.fill((0,0,0))
    screen.blit(facing, (pacman_x, pacman_y))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        '''
        elif e.type == pygame.KEYUP:
            print 'keyup'
            moving = False
        '''
        if e.type == pygame.KEYDOWN:
            print 'keydown'
            moving = True
            kname = pygame.key.name(e.key)
            #print kname
            if kname == 'q':
                running = False
            elif kname in ('right','left','up','down'):
                #print "new direction: %s" % kname
                direction = kname
                if direction == 'right':
                    facing = pacman_right
                elif direction == 'left':
                    facing = pacman_left
                elif direction == 'up':
                    facing = pacman_up
                elif direction == 'down':
                    facing = pacman_down


pygame.quit()
