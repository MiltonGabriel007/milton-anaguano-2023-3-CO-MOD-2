import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUDS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import Obstacle_manager
from dino_runner.components.menu import Menu
from dino_runner.components.counter import Counter
from dino_runner.components.clouds import Clouds

class Game:
    GAME_SPEED = 20
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = Obstacle_manager()
        self.menu = Menu(self.screen, "Press any key to start...")
        self.running = False
        self.score = Counter()
        self.clouds = Clouds(CLOUDS)

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.reset_game()
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        #pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.clouds.update(self.game_speed)
        self.update_score()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((241, 240, 250))
        self.draw_background()
        self.clouds.draw(self.screen)
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        self.screen.blit(ICON, (half_screen_width - 50, half_screen_height - 140))
        self.menu.draw(self.screen, self.score.count, self.obstacle_manager.dino_deaths, self.score.max_score)
        self.menu.update(self)

    def update_score(self):
        self.score.update()
        if self.score.count % 100 == 0 and self.game_speed < 500:
            self.game_speed += 5
        
    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.game_speed = self.GAME_SPEED
        self.score.reset()
        self.player.reset()
    