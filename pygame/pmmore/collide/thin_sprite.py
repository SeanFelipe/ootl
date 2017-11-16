class ThinSprite:
    def __init__(self, surface, startxy):
        self.surface = surface
        self.image = self.surface
        self.direction = 'right'
        self.rect = self.surface.get_rect()
        self.rect.x = startxy[0]
        self.rect.y = startxy[1]


