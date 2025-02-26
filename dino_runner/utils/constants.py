import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoRED/DINO1.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Shield.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Hammer1.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Shield.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Hammer.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"

SHIELD_TYPE = "shield"

HAMMER_TYPE = "hammer"

FONT_STYLE = "freesansbold.ttf"

CLOUDS = [
    pygame.image.load(os.path.join(IMG_DIR, "Clouds/Cloud1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Clouds/Cloud2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Clouds/Cloud3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Clouds/Cloud4.png")),
]

DINORED = [
    pygame.image.load(os.path.join(IMG_DIR, "DinoRED/DINO1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "DinoRED/DINO2.png")),
]

DINORED_JUMP = pygame.image.load(os.path.join(IMG_DIR, "DinoRED/DINO.png"))

DUCKING_RED = [
    pygame.image.load(os.path.join(IMG_DIR, "DinoRED/DINO3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "DinoRED/DINO4.png")),
]

DINORED_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "DinoRED/DINO_HAMMER3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "DinoRED/DINO_HAMMER4.png")),
]

DUCKING_HAMMER_RED = [
    pygame.image.load(os.path.join(IMG_DIR, "DinoRED/DINO_HAMMER1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "DinoRED/DINO_HAMMER2.png")),
]

JUMP_HAMMER_RED = pygame.image.load(os.path.join(IMG_DIR, "DinoRED/DINO_HAMMER5.png"))    

DINORED_SHIELD = [ 
    pygame.image.load(os.path.join(IMG_DIR, "DinoRED/DINO_SHIELD3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "DinoRED/DINO_SHIELD4.png")),
]

DUCKING_SHIELD_RED = [
    pygame.image.load(os.path.join(IMG_DIR, "DinoRED/DINO_SHIELD1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "DinoRED/DINO_SHIELD2.png")),
]

JUMP_SHIELD_RED = pygame.image.load(os.path.join(IMG_DIR, "DinoRED/DINO_SHIELD5.png"))

DINOMONSTER = [
    pygame.image.load(os.path.join(IMG_DIR, "DinoRED/Dinomonster1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "DinoRED/Dinomonster2.png")),
]

GAMEOVER = pygame.image.load(os.path.join(IMG_DIR, "Other/GameOver.png"))

SHIELD_RED = pygame.image.load(os.path.join(IMG_DIR, "DinoRED/SHIELD.png"))
HAMMER_RED =pygame.image.load(os.path.join(IMG_DIR, "DinoRED/HAMMER1.png"))

HAMMER_RED2 = [
    pygame.image.load(os.path.join(IMG_DIR, "DinoRED/HAMMER1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "DinoRED/HAMMER2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "DinoRED/HAMMER3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "DinoRED/HAMMER4.png")),
]

FONDO1 = pygame.image.load(os.path.join(IMG_DIR, "DinoRED/FONDO.png"))
FONDO2 = pygame.image.load(os.path.join(IMG_DIR, "DinoRED/FONDO2.png"))
FONDO3 = pygame.image.load(os.path.join(IMG_DIR, "DinoRED/FONDO3.png"))

os.chdir(r"C:\Users\USER\Documents\Jala-University\milton-anaguano-2023-3-CO-MOD-2")
pygame.mixer.init()
MUSIC = pygame.mixer.Sound(os.path.join(IMG_DIR, "DinoRED/Like_Dino!.mp3"))