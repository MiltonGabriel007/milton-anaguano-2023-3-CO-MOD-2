import pygame
import random
from dino_runner.components.obstacles.obstacle import Obstacle

class DinoMonster(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,1)
        super().__init__(image, self.type)
        self.rect.y = 300