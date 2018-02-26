import pygame
from pygame.transform import scale2x
from pdb import set_trace
import random
BLUE_WALL_COLOR = (33,33,255,255)


spritesheet = pygame.image.load('spritesheet.png')

def get_spritesheet_image(x,y,w=16,h=16):
    return scale2x(spritesheet.subsurface(x,y,w,h))

ghost_images = {
    'blinky' : get_spritesheet_image(455, 64),
    'pinky'  : get_spritesheet_image(455, 80),
    'inky'   : get_spritesheet_image(455, 96),
    'clyde'  : get_spritesheet_image(455, 112),
}


class Ghost:
    def __init__(self, name, startx, starty):
        self.x = startx
        self.y = starty
        self.image = ghost_images[name]
        self.direction = 'right'
        self.moving = True

    def move(self):
        speed = 3
        if self.moving:
            if self.direction == 'down':
                self.y += speed
            if self.direction == 'up':
                self.y -= speed
            if self.direction == 'left':
                self.x -= speed
            if self.direction == 'right':
                self.x += speed



    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
    def set_direction(self, direction):
        self.direction = direction
    def get_dots_ahead(self, ahead=1):
        rect = self.get_rect()
        dots_ahead = []
        dots_ahead.append((rect.midright[0] + ahead, rect.midright[1]))
        dots_ahead.append((rect.midleft[0] - ahead, rect.midleft[1]))
        dots_ahead.append((rect.midtop[0], rect.midtop[1] - ahead))
        dots_ahead.append((rect.midbottom[0], rect.midbottom[1] + ahead))
        return dots_ahead
    def dots_corners(self):
        dots_corners = []
    def get_dots_xy(self, ahead=0):
        da = self.get_dots_ahead(ahead)
        out = {
            'up'     : da[2],
            'right'  : da[0],
            'down'   : da[3],
            'left'   : da[1],
        }
        return out

    def check_for_wall(self, screen):
        dotxy = self.get_dots_xy()
        color_in_direction = screen.get_at(dotxy[self.direction])
        if color_in_direction == BLUE_WALL_COLOR:
            self.choose_new_direction(screen)

    def choose_new_direction(self, screen):
        all_directions = ['right','left','up','down']

        valid_directions = []
        dotxy = self.get_dots_xy()
        for direction in all_directions:
            direction_is_valid = True
            color_in_direction = screen.get_at(dotxy[direction])
            if color_in_direction == BLUE_WALL_COLOR:
                direction_is_valid = False
            if direction_is_valid:
                valid_directions.append(direction)

        number_of_valid_directions = len(valid_directions)
        random_index = random.randint(0, number_of_valid_directions - 1)
        new_direction = valid_directions[random_index]
        self.set_direction(new_direction)



pacman_r1 = get_spritesheet_image(457,1,9,13)
pacman_r2 = get_spritesheet_image(473,1,12,13)
pacman_l1 = get_spritesheet_image(461,17,9,13)
pacman_l2 = get_spritesheet_image(474,17,12,13)
pacman_u1 = get_spritesheet_image(457,37,13,9)
pacman_u2 = get_spritesheet_image(473,34,13,12)
pacman_d1 = get_spritesheet_image(457,49,13,9)
pacman_d2 = get_spritesheet_image(473,49,13,12)



pacman_directions = {
    'right' : (pacman_r1, pacman_r2),
    'left'  : (pacman_l1, pacman_l2),
    'up'    : (pacman_u1, pacman_u2),
    'down'  : (pacman_d1, pacman_d2)
    }


class Pacman:
    def __init__(self):
        self.x = 210
        self.y = 362
        self.direction = 'right'
        self.image = pacman_directions[self.direction][1]
        self.first_chomp = True
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
    def set_direction(self, direction):
        self.direction = direction
        index = int(self.first_chomp)
        self.image = pacman_directions[self.direction][index]
    def chomp(self):
        pacman.first_chomp = not pacman.first_chomp
        index = int(self.first_chomp)
        self.image = pacman_directions[self.direction][index]
    def get_dots_ahead(self, ahead=1):
        rect = self.get_rect()
        dots_ahead = []
        dots_ahead.append((rect.midright[0] + ahead, rect.midright[1]))
        dots_ahead.append((rect.midleft[0] - ahead, rect.midleft[1]))
        dots_ahead.append((rect.midtop[0], rect.midtop[1] - ahead))
        dots_ahead.append((rect.midbottom[0], rect.midbottom[1] + ahead))
        return dots_ahead
    def dots_corners(self):
        dots_corners = []
    def get_dots_xy(self, ahead=0):
        da = self.get_dots_ahead(ahead)
        out = {
            'up'     : da[2],
            'right'  : da[0],
            'down'   : da[3],
            'left'   : da[1],
        }
        return out

