import pygame
import random
from dino_runner.components.cactus import Cactus, Cactus2
from dino_runner.components.bird import Bird
from dino_runner.components.dinomonster import DinoMonster
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, SHIELD_TYPE, HAMMER_TYPE, HAMMER, SCREEN_WIDTH, DINOMONSTER

class Obstacle_manager:
    def __init__(self, game):
        self.image1 = HAMMER
        self.image1_rect = self.image1.get_rect()
        self.image1_rect.x = game.player.X_POS 
        self.obstacles = []
        self.dino_deaths = 0
        
    def update(self, game):
        self.image1_rect.y= game.player.dino_rect.y
            
        if len(self.obstacles) == 0:        
            step_index = random.randint(0,3)

            if step_index == 3:
                monster = DinoMonster(DINOMONSTER)
                self.obstacles.append(monster)

            if step_index  == 0:
                bird = Bird(BIRD)
                self.obstacles.append(bird)

            elif step_index  == 1:
                cactus = Cactus(SMALL_CACTUS)
                self.obstacles.append(cactus) 

            elif step_index  == 2:
                cactus2 = Cactus2(LARGE_CACTUS)
                self.obstacles.append(cactus2)

        if game.player.hammer_active:
            self.image1_rect.x += game.game_speed
            if self.image1_rect.x > SCREEN_WIDTH:
                game.player.hammer_active = False
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.hammer_active:
                if self.image1_rect.colliderect(obstacle.rect):
                    self.obstacles.remove(obstacle)
                    game.player.hammer_active= False

            if game.player.dino_rect.colliderect(obstacle.rect):
                #controlando si el dino tiene shield o no
                if game.player.type != SHIELD_TYPE:
                    game.playing = False
                    self.dino_deaths += 1
                    break 
                else:
                    self.obstacles.remove(obstacle) 
               
    def draw(self, game, screen ):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

        if game.player.hammer_active:
            screen.blit(self.image1, self.image1_rect)
    
    def reset_obstacles(self):
        self.obstacles = []     