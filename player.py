from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.Surface(PLAYER_SIZE)
        self.image.fill("#c0ffee")
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH/5, WINDOW_HEIGHT/2))
        self.jump_speed = PLAYER_JUMP_VAL
        self.fall_speed = 600
        self.fall_multiplier = 1
        self.jump_time = 0
        self.acceleration_time = 500


    def update(self, dt):
        self.rect.centery += self.fall_speed * dt * self.fall_multiplier
        self.jump(dt)
        self.get_fall_acceleration()

    def get_fall_acceleration(self):
        percent = float((pygame.time.get_ticks() - self.jump_time) / self.acceleration_time)
        if (pygame.time.get_ticks() - self.jump_time <= self.acceleration_time):
            self.fall_multiplier = percent

    def jump(self, dt):
        keys = pygame.key.get_just_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            self.rect.centery -= self.jump_speed * dt
            self.jump_time = pygame.time.get_ticks()
