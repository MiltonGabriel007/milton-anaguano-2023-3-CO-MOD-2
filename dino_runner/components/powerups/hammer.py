import pygame
from pygame.sprite import Sprite
from dino_runner.components.powerups.powerup import Powerup
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE #DEFAULT_TYPE

class Hammer(Powerup):
    def __init__(self):
       # self.hammer_count = 1
     #   self.image = HAMMER
      #  self.image_rect = self.image.get_rect()
       # self.image_rect.x = 80
        #self.image_rect.y = 400
        super().__init__(HAMMER, HAMMER_TYPE)
    
    #def update1(self, user_input, game_speed, screen):
        
     #   if user_input[pygame.K_RIGHT]: # and type == HAMMER_TYPE:
      #      self.draw1(screen)
       #     print("prueba")
        #self.image_rect.x += game_speed

    #def draw1(self, screen):
     #   if type == HAMMER_TYPE:
       #  screen.blit(self.image, self.image_rect)
       #     if self.rect.x < -self.rect.width:
        #     obstacles.pop()

   # def hammer_power(self, game):
        #if self.image_rect.colliderect(obstacle.rect):
         #   self.powerups.remove(obstacle)
          #  game.player.has_power_up = False
           # game.player.type = DEFAULT_TYPE