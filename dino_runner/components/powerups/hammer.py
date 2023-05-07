import pygame
from pygame.sprite import Sprite
from dino_runner.components.powerups.powerup import Powerup
from dino_runner.utils.constants import HAMMER_RED, HAMMER_TYPE, SCREEN_WIDTH

class Hammer(Powerup, Sprite):
    def __init__(self):
        super().__init__(HAMMER_RED, HAMMER_TYPE)

class Hammer1(Sprite):
    X_POS = 80
    def __init__(self):
        self.image = HAMMER_RED
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.X_POS

    def update(self, dino_y_pos, game_speed):
        self.image_rect.y = dino_y_pos
        self.image_rect.x += game_speed

    def reset_pos(self):
        self.image_rect.x = self.X_POS