import pygame
import random
from dino_runner.components.cactus import Cactus, Cactus2
from dino_runner.components.bird import Bird
from dino_runner.components.dinomonster import DinoMonster
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, SHIELD_TYPE, HAMMER_TYPE, HAMMER, SCREEN_WIDTH, DINOMONSTER
#from dino_runner.components.powerups.hammer import Hammer

class Obstacle_manager:
    def __init__(self, game):
        self.image1 = HAMMER
        self.image1_rect = self.image1.get_rect()
        self.image1_rect.x = game.player.X_POS 
        #self.image1_rect.y = 310
        self.obstacles = []
        self.dino_deaths = 0
        self.hammer_active = False
        
    def update(self, game):
        self.image1_rect.y= game.player.dino_rect.y

        user_input = pygame.key.get_pressed()
            
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
            
        if user_input[pygame.K_RIGHT] and game.player.type == HAMMER_TYPE: #and self.hammer_active == False:
            self.hammer_active = True
            #game.player.has_power_up == False
            #print("prueba")
            
        if self.hammer_active:
            self.image1_rect.x += game.game_speed
            if self.image1_rect.x > SCREEN_WIDTH:
                self.hammer_active = False
                #game.player.has_power_up = True
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            #if game.player.type == HAMMER_TYPE: # and self.hammer_count > 0 : #and game.player.has_power_up == True:
            if self.hammer_active:
                if self.image1_rect.colliderect(obstacle.rect):
                    self.obstacles.remove(obstacle)
                    self.hammer_active = False
                    #game.player.type = DEFAULT_TYPE
                    #game.player.has_power_up == False

            if game.player.dino_rect.colliderect(obstacle.rect):
                #controlando si el dino tiene shield o no
                if game.player.type != SHIELD_TYPE:
                    game.playing = False
                    self.dino_deaths += 1
                    break 
                else:
                    self.obstacles.remove(obstacle) 
        #print("Muertes ", self.dino_deaths)
               
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

        if self.hammer_active:
            screen.blit(self.image1, self.image1_rect)
    
    def reset_obstacles(self):
        self.obstacles = []
        self.hammer_active = False
        
        