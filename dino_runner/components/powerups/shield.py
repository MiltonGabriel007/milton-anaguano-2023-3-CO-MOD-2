import pygame
from dino_runner.components.powerups.powerup import Powerup
from dino_runner.utils.constants import SHIELD_RED, SHIELD_TYPE

class Shield(Powerup):
    def __init__(self):
        super().__init__(SHIELD_RED, SHIELD_TYPE)