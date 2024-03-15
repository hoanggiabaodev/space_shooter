import pygame, random, gif_pygame
from constants.screen import SCREEN_WIDTH, SCREEN_HEIGHT

# ========================================== ENEMY SETUP ==========================================

###### Setup level của Enemy:
LEVEL_1 = "level_1"
LEVEL_2 = "level_2"
LEVEL_3 = "level_3"
LEVEL_4 = "level_4"
LEVEL_5 = "level_5"

###### Setup kích thước và hình ảnh của Enemy:
ENEMY_LEVEL_1_WIDTH = 30
ENEMY_LEVEL_1_HEIGHT = 30
ENEMY_LEVEL_2_WIDTH = 35
ENEMY_LEVEL_2_HEIGHT = 35
ENEMY_LEVEL_3_WIDTH = 40
ENEMY_LEVEL_3_HEIGHT = 40
ENEMY_LEVEL_4_WIDTH = 45
ENEMY_LEVEL_4_HEIGHT = 45
ENEMY_LEVEL_5_WIDTH = 50
ENEMY_LEVEL_5_HEIGHT = 50

ENEMY_LEVEL_1_IMAGE = pygame.transform.scale(
    pygame.image.load("resources/images/Enemy_Level_1.png"),
    (ENEMY_LEVEL_1_WIDTH, ENEMY_LEVEL_1_HEIGHT),
)
ENEMY_LEVEL_2_IMAGE = pygame.transform.scale(
    pygame.image.load("resources/images/Enemy_Level_2.png"),
    (ENEMY_LEVEL_2_WIDTH, ENEMY_LEVEL_2_HEIGHT),
)
ENEMY_LEVEL_3_IMAGE = pygame.transform.scale(
    pygame.image.load("resources/images/Enemy_Level_3.png"),
    (ENEMY_LEVEL_3_WIDTH, ENEMY_LEVEL_3_HEIGHT),
)
ENEMY_LEVEL_4_IMAGE = pygame.transform.scale(
    pygame.image.load("resources/images/Enemy_Level_4.png"),
    (ENEMY_LEVEL_4_WIDTH, ENEMY_LEVEL_4_HEIGHT),
)
ENEMY_LEVEL_5_IMAGE = pygame.transform.scale(
    pygame.image.load("resources/images/Enemy_Level_5.png"),
    (ENEMY_LEVEL_5_WIDTH, ENEMY_LEVEL_5_HEIGHT),
)

###### Setup vị trí bắt đầu của Enemy:
ENEMY_START_X = random.randint(0, SCREEN_WIDTH)
ENEMY_START_Y = 50

###### Setup tốc độ di chuyển của Enemy:
ENEMY_LEVEL_1_SPEED_X = 1
ENEMY_LEVEL_1_SPEED_Y = 0.2
ENEMY_LEVEL_2_SPEED_X = 1.5
ENEMY_LEVEL_2_SPEED_Y = 0.2
ENEMY_LEVEL_3_SPEED_X = 2
ENEMY_LEVEL_3_SPEED_Y = 0.23
ENEMY_LEVEL_4_SPEED_X = 2.5
ENEMY_LEVEL_4_SPEED_Y = 0.23
ENEMY_LEVEL_5_SPEED_X = 3
ENEMY_LEVEL_5_SPEED_Y = 0.23

###### Setup chỉ số của Enemy:
ENEMY_LEVEL_1_HEALTH = 20
ENEMY_LEVEL_2_HEALTH = 24
ENEMY_LEVEL_3_HEALTH = 32
ENEMY_LEVEL_4_HEALTH = 40
ENEMY_LEVEL_5_HEALTH = 45

ENEMY_LEVEL_1_DAMAGE = 10
ENEMY_LEVEL_2_DAMAGE = 15
ENEMY_LEVEL_3_DAMAGE = 20
ENEMY_LEVEL_4_DAMAGE = 25
ENEMY_LEVEL_5_DAMAGE = 30

ENEMY_LEVEL_1_DEFENSE = 0
ENEMY_LEVEL_2_DEFENSE = 2
ENEMY_LEVEL_3_DEFENSE = 3
ENEMY_LEVEL_4_DEFENSE = 5
ENEMY_LEVEL_5_DEFENSE = 7

ENEMY_LEVEL_1_FREQUENCY_RATE = 0.5
ENEMY_LEVEL_2_FREQUENCY_RATE = 0.2
ENEMY_LEVEL_3_FREQUENCY_RATE = 0.15
ENEMY_LEVEL_4_FREQUENCY_RATE = 0.1
ENEMY_LEVEL_5_FREQUENCY_RATE = 0.05

ENEMY_GENETATE_DELAY = 2

ENEMY_LEVEL_1_EXPLOSION_EFFECT = gif_pygame.load(
    "resources/images/Enemy_Level_1_Explosion_Effect.gif"
)
ENEMY_LEVEL_2_EXPLOSION_EFFECT = gif_pygame.load(
    "resources/images/Enemy_Level_2_Explosion_Effect.gif"
)
ENEMY_LEVEL_3_EXPLOSION_EFFECT = gif_pygame.load(
    "resources/images/Enemy_Level_3_Explosion_Effect.gif"
)
ENEMY_LEVEL_4_EXPLOSION_EFFECT = gif_pygame.load(
    "resources/images/Enemy_Level_4_Explosion_Effect.gif"
)
ENEMY_LEVEL_5_EXPLOSION_EFFECT = gif_pygame.load(
    "resources/images/Enemy_Level_5_Explosion_Effect.gif"
)
###### Danh sách Enemy:
ENEMY_LIST = pygame.sprite.Group()
