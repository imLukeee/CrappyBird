from settings import *
from player import Player

class Game():
    def __init__(self):
        #window setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.running = True
        self.clock = pygame.time.Clock()

        #sprite groups
        self.all_sprites = pygame.sprite.Group()

        self.player = Player(self.all_sprites)

    def check_bounds(self):
        if self.player.rect.bottom > WINDOW_HEIGHT:
            self.running = False
        if self.player.rect.top <= 0:
            self.player.rect.top = 5

    def run(self):
        while self.running:
            delta_time = self.clock.tick(240)/1000

            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.all_sprites.update(delta_time)
            self.check_bounds()

            #draw the game
            self.display_surface.fill(COLORS['bg'])
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
