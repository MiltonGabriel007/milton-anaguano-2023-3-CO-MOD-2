import pygame
import random
from dino_runner.components.powerups.shield import Shield
from dino_runner.components.powerups.hammer import Hammer
from dino_runner.utils.constants import SHIELD_TYPE, HAMMER_TYPE

class PowerupManager:
    def __init__(self):
        self.powerups = []
        self.duration = random.randint(3, 5)
        self.appears_when = random.randint(50, 70)
        self.index = 0

    def update(self, game):
        #controlamos las apariciones del powerup
        if len(self.powerups) == 0 and self.appears_when == game.score.count:
            self.generate_powerup()
        #llamamos a la animacion del powerup
        for powerup in self.powerups:
            powerup.update(game.game_speed, self.powerups)
            #si el dino colisiona con el powerup, el powerup desaparece
            if game.player.dino_rect.colliderect(powerup.rect) and self.index == 0:
                self.index = random.randint(0,1) 
                self.powerups.remove(powerup)
                powerup.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.type = SHIELD_TYPE
                game.player.power_up_time = powerup.start_time + (self.duration * 1000)
                #######################
            elif game.player.dino_rect.colliderect(powerup.rect) and self.index == 1:
                self.index = random.randint(0,1) 
                self.powerups.remove(powerup)
                powerup.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.type = HAMMER_TYPE
                game.player.power_up_time = powerup.start_time + (self.duration * 1000)

    def draw(self, screen):
        for powerup in self.powerups:
            powerup.draw(screen)

    def reset_powerups(self):
        self.powerups = []
        self.appears_when = random.randint(50, 70)
        self.index = 1
        
    def generate_powerup(self):
        self.appears_when = random.randint(100, 300)
        if self.index  == 0:
            powerup = Shield()
        elif self.index == 1: 
            powerup = Hammer()
        self.powerups.append(powerup)       