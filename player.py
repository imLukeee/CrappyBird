from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        
        self.image = pygame.Surface(PLAYER_SIZE)
        self.image.fill("#c0ffee")
        
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH/4, WINDOW_HEIGHT/2))
        
    def update(self, dt):
        self.rect.centery += PLAYER_FALL_SPEED * dt
        self.jump(dt)
    
    def jump(self, dt):
        keys = pygame.key.get_just_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            self.rect.centery -= PLAYER_JUMP_VAL * dt
