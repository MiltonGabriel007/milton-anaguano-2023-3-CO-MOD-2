import pygame
from dino_runner.utils.constants import FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT, FONDO1

class Menu:

    half_screen_width = SCREEN_WIDTH // 2
    half_screen_height = SCREEN_HEIGHT // 2
    
    def __init__(self, screen, message):
        screen.blit(FONDO1, (0, 0))
        #screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, 500)
        self.text_rect1 = self.text.get_rect()
        self.text_rect1.center = (self.half_screen_width, 315)
        
    def update(self, game):
        self.handle_event_on_menu(game)
        pygame.display.update()
    
    def draw(self, screen, score, deaths, max_score):
        font = pygame.font.Font(FONT_STYLE, 25)
        score_show = font.render(f"Score: {score}", True, (0, 0, 0))
        score_show_rect = score_show.get_rect()
        score_show_rect.center = (self.half_screen_width, 300)
        screen.blit(score_show, score_show_rect)

        max_score = font.render(f"Max Score: {max_score}", True, (0, 0, 0)) 
        max_score_rect = max_score.get_rect()
        max_score_rect.center = (self.half_screen_width, 330)
        screen.blit(max_score, max_score_rect)

        dino_deaths = font.render(f"Dino Deaths: {deaths}", True, (0, 0, 0))
        dino_deaths_rect = dino_deaths.get_rect()
        dino_deaths_rect.center = (self.half_screen_width, 360)
        screen.blit(dino_deaths, dino_deaths_rect)
        #screen.blit(self.text, (self.text_rect.x, self.text_rect.y))
        screen.blit(self.text, self.text_rect)

    def reset_screen_color(self, screen):
        screen.blit(FONDO1, (0, 0))
        #screen.fill((241, 240, 250))

    def handle_event_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.playing = False
            elif event.type == pygame.KEYDOWN:
                game.run()
    def draw1(self, screen):
        screen.blit(self.text, self.text_rect1)

    def draw2(self, screen, text, x_pos, y_pos):
        font = pygame.font.Font(FONT_STYLE, 25)
        show_power_time = font.render(f"{text}", True, (0, 0, 0))
        show_power_time1 = show_power_time.get_rect()
        show_power_time1.center = (x_pos, y_pos)
        screen.blit(show_power_time, show_power_time1.center)