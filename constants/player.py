import pygame, gif_pygame
from constants.screen import SCREEN_WIDTH, SCREEN_HEIGHT

# ========================================== PLAYER SETUP ==========================================

###### Setup kích thước và hình ảnh của Player:
PLAYER_NORMAL_WIDTH = 60
PLAYER_NORMAL_HEIGHT = 60
PLAYER_SPECIAL_WIDTH = 60
PLAYER_SPECIAL_HEIGHT = 60
PLAYER_SPREAD_WIDTH = 60
PLAYER_SPREAD_HEIGHT = 60
PLAYER_AROUND_WIDTH = 60
PLAYER_AROUND_HEIGHT = 60
PLAYER_LASER_WIDTH = 60
PLAYER_LASER_HEIGHT = 60

PLAYER_NORMAL_IMAGE = pygame.transform.scale(pygame.image.load("resources/images/Player_Normal.png"), (PLAYER_NORMAL_WIDTH, PLAYER_NORMAL_HEIGHT))
PLAYER_SPECIAL_IMAGE = pygame.transform.scale(pygame.image.load("resources/images/Player_Special.png"), (PLAYER_SPECIAL_WIDTH, PLAYER_SPECIAL_HEIGHT))
PLAYER_SPREAD_IMAGE = pygame.transform.scale(pygame.image.load("resources/images/Player_Spread.png"), (PLAYER_SPREAD_WIDTH, PLAYER_SPREAD_HEIGHT))
PLAYER_AROUND_IMAGE = pygame.transform.scale(pygame.image.load("resources/images/Player_Around.png"), (PLAYER_AROUND_WIDTH, PLAYER_AROUND_HEIGHT))
PLAYER_LASER_IMAGE = pygame.transform.scale(pygame.image.load("resources/images/Player_Laser.png"), (PLAYER_LASER_WIDTH, PLAYER_LASER_HEIGHT))

###### Setup kích thước và hình ảnh hit box của Player:
PLAYER_HIT_BOX_WIDTH = 15
PLAYER_HIT_BOX_HEIGHT = 15
PLAYER_NORMAL_HIT_BOX_IMAGE = pygame.transform.scale(pygame.image.load("resources/images/Player_Normal_Hit_Box.png"), (PLAYER_HIT_BOX_WIDTH, PLAYER_HIT_BOX_HEIGHT))
PLAYER_SPECIAL_HIT_BOX_IMAGE = pygame.transform.scale(pygame.image.load("resources/images/Player_Special_Hit_Box.png"), (PLAYER_HIT_BOX_WIDTH, PLAYER_HIT_BOX_HEIGHT))
PLAYER_SPREAD_HIT_BOX_IMAGE = pygame.transform.scale(pygame.image.load("resources/images/Player_Spread_Hit_Box.png"), (PLAYER_HIT_BOX_WIDTH, PLAYER_HIT_BOX_HEIGHT))
PLAYER_AROUND_HIT_BOX_IMAGE = pygame.transform.scale(pygame.image.load("resources/images/Player_Around_Hit_Box.png"), (PLAYER_HIT_BOX_WIDTH, PLAYER_HIT_BOX_HEIGHT))
PLAYER_LASER_HIT_BOX_IMAGE = pygame.transform.scale(pygame.image.load("resources/images/Player_Laser_Hit_Box.png"), (PLAYER_HIT_BOX_WIDTH, PLAYER_HIT_BOX_HEIGHT))

###### Setup kích thước và hình ảnh skin của Player:

PLAYER_SPECIAL_SKIN_1_WIDTH = 120
PLAYER_SPECIAL_SKIN_1_HEIGHT = 120
PLAYER_SPREAD_SKIN_1_WIDTH = 100
PLAYER_SPREAD_SKIN_1_HEIGHT = 100
PLAYER_AROUND_SKIN_1_WIDTH = 260
PLAYER_AROUND_SKIN_1_HEIGHT = 200
PLAYER_LASER_SKIN_1_WIDTH = 120
PLAYER_LASER_SKIN_1_HEIGHT = 120
PLAYER_SPECIAL_SKIN_1_IMAGE = pygame.transform.scale(pygame.image.load("resources/images/Player_Special_Skin_1.png"), (PLAYER_SPECIAL_SKIN_1_WIDTH, PLAYER_SPECIAL_SKIN_1_HEIGHT))
PLAYER_SPREAD_SKIN_1_IMAGE = pygame.transform.scale(pygame.image.load("resources/images/Player_Spread_Skin_1.png"), (PLAYER_SPREAD_SKIN_1_WIDTH, PLAYER_SPREAD_SKIN_1_HEIGHT))
PLAYER_AROUND_SKIN_1_IMAGE = pygame.transform.scale(pygame.image.load("resources/images/Player_Around_Skin_1.png"), (PLAYER_AROUND_SKIN_1_WIDTH, PLAYER_AROUND_SKIN_1_HEIGHT))
PLAYER_LASER_SKIN_1_IMAGE = pygame.transform.scale(pygame.image.load("resources/images/Player_Laser_Skin_1.png"), (PLAYER_LASER_SKIN_1_WIDTH, PLAYER_LASER_SKIN_1_HEIGHT))


PLAYER_SPECIAL_SKIN_2_WIDTH = 220
PLAYER_SPECIAL_SKIN_2_HEIGHT = 100
PLAYER_SPREAD_SKIN_2_WIDTH = 140
PLAYER_SPREAD_SKIN_2_HEIGHT = 140
PLAYER_AROUND_SKIN_2_WIDTH = 100
PLAYER_AROUND_SKIN_2_HEIGHT = 100
PLAYER_LASER_SKIN_2_WIDTH = 220
PLAYER_LASER_SKIN_2_HEIGHT = 160
PLAYER_SPECIAL_SKIN_2_IMAGE = pygame.transform.scale(pygame.image.load("resources/images/Player_Special_Skin_2.png"), (PLAYER_SPECIAL_SKIN_2_WIDTH, PLAYER_SPECIAL_SKIN_2_HEIGHT))
PLAYER_SPREAD_SKIN_2_IMAGE = pygame.transform.scale(pygame.image.load("resources/images/Player_Spread_Skin_2.png"), (PLAYER_SPREAD_SKIN_2_WIDTH, PLAYER_SPREAD_SKIN_2_HEIGHT))
PLAYER_AROUND_SKIN_2_IMAGE = pygame.transform.scale(pygame.image.load("resources/images/Player_Around_Skin_2.png"), (PLAYER_AROUND_SKIN_2_WIDTH, PLAYER_AROUND_SKIN_2_HEIGHT))
PLAYER_LASER_SKIN_2_IMAGE = pygame.transform.scale(pygame.image.load("resources/images/Player_Laser_Skin_2.png"), (PLAYER_LASER_SKIN_2_WIDTH, PLAYER_LASER_SKIN_2_HEIGHT))

###### Setup vị trí bắt đầu của Player:
PLAYER_START_X = SCREEN_WIDTH / 2 - PLAYER_NORMAL_WIDTH / 2
PLAYER_START_Y = SCREEN_HEIGHT - PLAYER_NORMAL_HEIGHT - 10

###### Setup tốc độ di chuyển của Player:
PLAYER_SPEED_X = 5
PLAYER_SPEED_Y = 3

###### Setup chỉ số của Player:
PLAYER_HEALTH = 500

PLAYER_NORMAL_DAMAGE = 10
PLAYER_SPECIAL_DAMAGE = 12
PLAYER_SPREAD_DAMAGE = 15
PLAYER_AROUND_DAMAGE = 17
PLAYER_LASER_DAMAGE = 20

PLAYER_NORMAL_DEFENSE = 0
PLAYER_SPECIAL_DEFENSE = 5
PLAYER_SPREAD_DEFENSE = 7
PLAYER_AROUND_DEFENSE = 12
PLAYER_LASER_DEFENSE = 15

###### Setup health bar của Player:

PLAYER_HEALTH_BAR_FULL_WIDTH = 149
PLAYER_HEALTH_BAR_FULL_HEIGHT = 11
PLAYER_HEALTH_BAR_EMPTY_WIDTH = 150
PLAYER_HEALTH_BAR_EMPTY_HEIGHT = 12
PLAYER_HEALTH_BAR_FULL_POSITION = (11, 11)
PLAYER_HEALTH_BAR_EMPTY_POSITION = (10, 10)

PLAYER_HEALTH_BAR_FULL = pygame.transform.scale(pygame.image.load("resources/images/Player_Health_Bar_Full.png"), (PLAYER_HEALTH_BAR_FULL_WIDTH, PLAYER_HEALTH_BAR_FULL_HEIGHT))
PLAYER_HEALTH_BAR_EMPTY = pygame.transform.scale(pygame.image.load("resources/images/Player_Health_Bar_Empty.png"), (PLAYER_HEALTH_BAR_EMPTY_WIDTH, PLAYER_HEALTH_BAR_EMPTY_HEIGHT))

PLAYER_HEALTH_ICON_WIDTH = 30
PLAYER_HEALTH_ICON_HEIGHT = 20
PLAYER_HEALTH_ICON_POSITION = (10, 25)
PLAYER_HEALTH_ICON = pygame.transform.scale(pygame.image.load("resources/images/Player_Health_Icon.png"), (PLAYER_HEALTH_ICON_WIDTH, PLAYER_HEALTH_ICON_HEIGHT))

PLAYER_DEFENSE_ICON_WIDTH = 25
PLAYER_DEFENSE_ICON_HEIGHT = 25
PLAYER_DEFENSE_ICON_POSITION = (SCREEN_WIDTH - PLAYER_HEALTH_ICON_WIDTH - 10, 10)
PLAYER_DEFENSE_ICON = pygame.transform.scale(pygame.image.load("resources/images/Player_Defense_Icon.png"), (PLAYER_DEFENSE_ICON_WIDTH, PLAYER_DEFENSE_ICON_HEIGHT))

PLAYER_DAMAGE_ICON_WIDTH = 28
PLAYER_DAMAGE_ICON_HEIGHT = 28
PLAYER_DAMAGE_ICON_POSITION = (SCREEN_WIDTH - PLAYER_HEALTH_ICON_WIDTH - 10, 45)
PLAYER_DAMAGE_ICON = pygame.transform.scale(pygame.image.load("resources/images/Player_Damage_Icon.png"), (PLAYER_DAMAGE_ICON_WIDTH, PLAYER_DAMAGE_ICON_HEIGHT))

PLAYER_KILL_ICON_WIDTH = 28
PLAYER_KILL_ICON_HEIGHT = 24
PLAYER_KILL_ICON_POSITION = (SCREEN_WIDTH - PLAYER_HEALTH_ICON_WIDTH - 10, 80)
PLAYER_KILL_ICON = pygame.transform.scale(pygame.image.load("resources/images/Player_Kill_Icon.png"), (PLAYER_KILL_ICON_WIDTH, PLAYER_KILL_ICON_HEIGHT))

PLAYER_EXPLOSION_EFFECT = gif_pygame.load("resources/images/Player_Explosion_Effect.gif")
PLAYER_DEATH_EFFECT = gif_pygame.load("resources/images/Player_Kill_Effect.gif")

PLAYER_EXPLOSION_EFFECT_TIME = 50
PLAYER_DEATH_EFFECT_TIME = 2000

PLAYER_DEATH_SOUND = pygame.mixer.Sound("resources/sounds/Player_Death.wav")
PLAYER_DEATH_SOUND.set_volume(0.5)

PLAYER_LIST = pygame.sprite.Group()