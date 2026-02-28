from settings import *

class Pipe(pygame.sprite.Sprite):
    def __init__(self, groups, type, height, x = WINDOW_WIDTH + 200):
        super().__init__(groups)
        self.image = pygame.Surface((PIPE_WIDTH, height))
        self.image.fill("#77DD77")
        if type == "top":
            self.rect = self.image.get_frect(midtop = (x, 0))
        elif type == "bottom":
            self.rect = self.image.get_frect(midbottom = (x, WINDOW_HEIGHT))


    def update(self, dt):
        self.rect.centerx -= GAME_SPEED * dt 
        
        if self.rect.right < -10:
            self.kill()
