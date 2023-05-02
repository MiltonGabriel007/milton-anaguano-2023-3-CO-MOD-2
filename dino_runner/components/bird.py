import pygame
import random
from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    Height = [170, 220, 260]
    def __init__(self, image):
        self.Y_POS = self.Height
        self.type = random.randint(0,1)
        super().__init__(image, self.type)
        self.rect.y = random.choice(self.Y_POS)