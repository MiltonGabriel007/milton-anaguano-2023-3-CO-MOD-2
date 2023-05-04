import pygame
from pygame.sprite import Sprite
from dino_runner.components.powerups.powerup import Powerup
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE #DEFAULT_TYPE

class Hammer(Powerup):
    def __init__(self):
        super().__init__(HAMMER, HAMMER_TYPE)