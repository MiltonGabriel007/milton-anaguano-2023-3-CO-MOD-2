import pygame

from pygame.sprite import Sprite 
from dino_runner.utils.constants import RUNNING

class Dinosaur:
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = 80
        self.dino_rect.y = 310
        self.dino_run = True
        self.step_index = 0


    def update(self):
        if self.dino_run:
            self.run()
        
        if self.step_index > 10:
            self.step_index = 0  

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = 80
        self.dino_rect.y = 310
        self.step_index += 1

