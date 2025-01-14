import pygame
from pygame.sprite import Sprite 
from dino_runner.utils.constants import DEFAULT_TYPE, SHIELD_TYPE, HAMMER_TYPE, DINORED_JUMP, DUCKING_RED, DINORED, DINORED_HAMMER, DINORED_SHIELD, DUCKING_HAMMER_RED, DUCKING_SHIELD_RED, JUMP_HAMMER_RED, JUMP_SHIELD_RED

RUN_IMAGE = {DEFAULT_TYPE: DINORED, SHIELD_TYPE: DINORED_SHIELD, HAMMER_TYPE: DINORED_HAMMER}
DUCK_IMAGE = {DEFAULT_TYPE: DUCKING_RED, SHIELD_TYPE: DUCKING_SHIELD_RED, HAMMER_TYPE: DUCKING_HAMMER_RED}
JUMP_IMAGE = {DEFAULT_TYPE: DINORED_JUMP, SHIELD_TYPE: JUMP_SHIELD_RED, HAMMER_TYPE: JUMP_HAMMER_RED}

class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Ducking_Y_POS = 330
    JUMP_SPEED = 8.5

    def __init__(self):
        self.image = DINORED[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.dino_run = True
        self.step_index = 0
        self.dino_jump = False
        self.jump_speed = self.JUMP_SPEED
        self.dino_ducking = False
        self.Y_POS_ducking = self.Ducking_Y_POS
        self.type = DEFAULT_TYPE
        self.image = RUN_IMAGE[self.type][0]
        self.has_power_up = False
        self.power_up_time = 0 
        self.hammer_active = False

    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_ducking:
            self.ducking()

        if self.step_index >= 5:
            self.step_index = 0

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
        elif user_input[pygame.K_DOWN] and not self.dino_ducking:
            self.dino_ducking = True
            self.dino_run = False
        elif not self.dino_ducking and not self.dino_jump:
            self.dino_ducking = False
            self.dino_jump = False
            self.dino_run = True

        if user_input[pygame.K_RIGHT] and self.type == HAMMER_TYPE: 
            self.hammer_active = True
        
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def run(self):
        #self.image = DINORED[0] if self.step_index < 5 else DINORED[1]
        self.image = RUN_IMAGE[self.type][self.step_index//3]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        #self.image = DINORED_JUMP
        self.image = JUMP_IMAGE[self.type]
        self.dino_rect.y -= self.jump_speed*4
        self.jump_speed -= 0.7
        
        if self.jump_speed < -self.JUMP_SPEED:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_speed = self.JUMP_SPEED

    def ducking(self):
        #self.image = DUCKING_RED[0] if self.step_index < 5 else DUCKING_RED[1]
        self.image = DUCK_IMAGE[self.type][self.step_index//3]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_ducking
        self.dino_ducking = False
        self.step_index += 1

    def reset(self):
        self.image = DINORED[0]
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.dino_run = True
        self.step_index = 0
        self.dino_jump = False
        self.jump_speed = self.JUMP_SPEED
        self.dino_ducking = False
        self.Y_POS_ducking = self.Ducking_Y_POS
        self.type = DEFAULT_TYPE
        self.has_power_up = False
        self.power_up_time = 0 
        self.hammer_active = False