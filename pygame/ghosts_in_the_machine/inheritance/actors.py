class Actor:

    spritesheet = pygame.image.load('spritesheet.png')

    def get_spritesheet_image(self,x,y,w=16,h=16):
        return scale2x(Actor.spritesheet.subsurface(x,y,w,h))

    def get_start_image(self, name):
        if name == 'pacman':
            return get_spritesheet_image(457,1,9,13)
        if name == 'blinky':
            return get_spritesheet_image(455, 64)
        if name == 'pinky':
            return get_spritesheet_image(455, 80)
        if name == 'inky':
            return get_spritesheet_image(455, 96)
        if name == 'clyde':
            return get_spritesheet_image(455, 112)

    def __init__(self, name, startx, starty):
        self.x = startx
        self.y = starty
        self.direction = 'right'
        self.image = get_start_image(name)
    def get_rect(self):
        w = self.image.get_width()
        h = self.image.get_height()
        return pygame.Rect(self.x, self.y, w, h)
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
    def get_dxys(self, ahead=1):
        rect = self.get_rect()
        dxys = {
            'right' : (rect.midright[0] + ahead, rect.midright[1]),
            'left'  : (rect.midleft[0] - ahead, rect.midleft[1]),
            'up'    : (rect.midtop[0], rect.midtop[1] - ahead),
            'down'  : (rect.midbottom[0], rect.midbottom[1] + ahead),
        }
        return dxys



class Pacman(Actor):
    def __init__(self, name, startx, starty):
        super(name, startx, starty)
        self.first_chomp = True
    def chomp(self):
        pacman.first_chomp = not pacman.first_chomp
        index = int(self.first_chomp)
        self.image = pacman_directions[self.direction][index]



class Ghost:
    def __init__(self, name, startx, starty):
        super(name, startx, starty)

    def set_direction(self, direction):
        # need custom Ghost direction code
        #self.direction = direction

    # custom Ghost AI
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
