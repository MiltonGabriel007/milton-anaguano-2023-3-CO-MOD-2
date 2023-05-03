import pygame
import random
from dino_runner.components.cactus import Cactus, Cactus2
from dino_runner.components.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class Obstacle_manager:
    def __init__(self):
        self.obstacles = []
        self.dino_deaths = 0
        
    def update(self, game):
        if len(self.obstacles) == 0:        
            step_index = random.randint(1,3)
            
            if step_index % 3 == 0:
                bird = Bird(BIRD)
                self.obstacles.append(bird)

            elif step_index % 2 == 0:
                cactus = Cactus(SMALL_CACTUS)
                self.obstacles.append(cactus) 

            elif step_index % 2 == 1:
                cactus2 = Cactus2(LARGE_CACTUS)
                self.obstacles.append(cactus2)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles) 
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                self.dino_deaths += 1
                break  
        #print("Muertes ", self.dino_deaths)
               
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def reset_obstacles(self):
        self.obstacles = []
        