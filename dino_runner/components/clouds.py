import pygame
import random

class Clouds:
    Height = [30, 60, 90]
    X_Space = [1100, 1200, 1300, 1400, 1500]
    def __init__(self, imagen):
        self.image = imagen
        self.type = random.randint(0,3)
        self.Y_POS = self.Height
        self.X_POS = self.X_Space
        self.rect = self.image[self.type].get_rect()
        self.rect.y = random.choice(self.Y_POS)
        self.rect.x = random.choice(self.X_Space)

    def update(self, game_speed):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            self.type = random.randint(0,3)
            self.rect.y = random.choice(self.Y_POS)
            self.rect.x = random.choice(self.X_Space)

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)