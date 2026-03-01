from settings import *
from player import Player
from pipe import Pipe
from random import randint

class Game():
    def __init__(self):
        #window setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.running = True
        self.clock = pygame.time.Clock()
        self.score = 0

        #sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.pipe_sprites = pygame.sprite.Group()
        self.passed_sprites = []
        #pipe spawn timer
        self.pipe_spawn = pygame.event.custom_type()
        pygame.time.set_timer(self.pipe_spawn, 2000)

        self.init_game()


    def init_game(self):
        self.player = Player(self.all_sprites)
        gap_top_height = randint(101, WINDOW_HEIGHT - 100 - PIPE_GAP)
        Pipe([self.all_sprites, self.pipe_sprites], "top", gap_top_height-1, 900)
        Pipe([self.all_sprites, self.pipe_sprites], "bottom", WINDOW_HEIGHT - gap_top_height - PIPE_GAP, 900)
        gap_top_height = randint(101, WINDOW_HEIGHT - 100 - PIPE_GAP)
        Pipe([self.all_sprites, self.pipe_sprites], "top", gap_top_height-1, 1500)
        Pipe([self.all_sprites, self.pipe_sprites], "bottom", WINDOW_HEIGHT - gap_top_height - PIPE_GAP, 1500)

    def check_player_bounds(self):
        if self.player.rect.bottom > WINDOW_HEIGHT:
            self.running = False
        if self.player.rect.top <= 0:
            self.player.rect.top = 5

    def check_collisions(self):
        for sprite in self.pipe_sprites:
            if sprite.rect.colliderect(self.player.rect):
                self.running = False

    def display_score(self):
        font = pygame.font.SysFont(name = "Arial", size = 32)
        score_text_surface = font.render(f"Score: {self.score:.0f}", True, "#FFFFFF")
        score_text_rect = score_text_surface.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT / 5))
        self.display_surface.blit(score_text_surface, score_text_rect)

    def increment_score(self):
        for sprite in self.pipe_sprites:
            if (sprite.rect.centerx <= self.player.rect.centerx) and (sprite not in self.passed_sprites):
                self.passed_sprites.append(sprite)
                self.score += 0.5

    def run(self):
        while self.running:
            delta_time = self.clock.tick(240)/1000

            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == self.pipe_spawn:
                    gap_top_height = randint(101, WINDOW_HEIGHT - 100 - PIPE_GAP)
                    Pipe([self.all_sprites, self.pipe_sprites], "top", gap_top_height-1)
                    Pipe([self.all_sprites, self.pipe_sprites], "bottom", WINDOW_HEIGHT - gap_top_height - PIPE_GAP)
                    
            
            self.all_sprites.update(delta_time)
            self.check_player_bounds()
            self.increment_score()
            self.check_collisions()

            #draw the game
            self.display_surface.fill(COLORS['bg'])
            self.all_sprites.draw(self.display_surface)
            self.display_score()
            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
