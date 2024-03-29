import pygame

# ========================================== BULLET PLAYER SETUP ==========================================

###### Setup đạn "normal" của Player:
PLAYER_BULLET_NORMAL_WIDTH = 12
PLAYER_BULLET_NORMAL_HEIGHT = 70
PLAYER_BULLET_NORMAL_DELAY = 500
PLAYER_BULLET_NORMAL_SPEED = 15
PLAYER_BULLET_NORMAL_COUNT = 1
PLAYER_BULLET_NORMAL_START_ANGLE = -3
PLAYER_BULLET_NORMAL_END_ANGLE = 3
PLAYER_BULLET_NORMAL_IMAGE = pygame.transform.scale(
    pygame.image.load("resources/images/Player_Bullet_Normal.png"),
    (PLAYER_BULLET_NORMAL_WIDTH, PLAYER_BULLET_NORMAL_HEIGHT),
)
HIT_VOLUME = 0.5
PLAYER_BULLET_NORMAL_SOUND = pygame.mixer.Sound(
    "resources/sounds/Player_Bullet_Normal.wav"
)
PLAYER_BULLET_NORMAL_SOUND.set_volume(0.5)

###### Setup đạn "special" của Player:
PLAYER_BULLET_SPECIAL_WIDTH = 15
PLAYER_BULLET_SPECIAL_HEIGHT = 30
PLAYER_BULLET_SPECIAL_DELAY = 300
PLAYER_BULLET_SPECIAL_SPEED = 12
PLAYER_BULLET_SPECIAL_COUNT = 3
PLAYER_BULLET_SPECIAL_START_ANGLE = -10
PLAYER_BULLET_SPECIAL_END_ANGLE = 10
PLAYER_BULLET_SPECIAL_IMAGE = pygame.transform.scale(
    pygame.image.load("resources/images/Player_Bullet_Special.png"),
    (PLAYER_BULLET_SPECIAL_WIDTH, PLAYER_BULLET_SPECIAL_HEIGHT),
)
PLAYER_BULLET_SPECIAL_SOUND = pygame.mixer.Sound(
    "resources/sounds/Player_Bullet_Special.wav"
)
PLAYER_BULLET_SPECIAL_SOUND.set_volume(HIT_VOLUME)

###### Setup đạn "spread" của Player:
PLAYER_BULLET_SPREAD_WIDTH = 12
PLAYER_BULLET_SPREAD_HEIGHT = 50
PLAYER_BULLET_SPREAD_DELAY = 150
PLAYER_BULLET_SPREAD_SPEED = 8
PLAYER_BULLET_SPREAD_COUNT = 10
PLAYER_BULLET_SPREAD_START_ANGLE = -20
PLAYER_BULLET_SPREAD_END_ANGLE = 20
PLAYER_BULLET_SPREAD_IMAGE = pygame.transform.scale(
    pygame.image.load("resources/images/Player_Bullet_Spread.png"),
    (PLAYER_BULLET_SPREAD_WIDTH, PLAYER_BULLET_SPREAD_HEIGHT),
)
PLAYER_BULLET_SPREAD_SOUND = pygame.mixer.Sound(
    "resources/sounds/Player_Bullet_Spread.wav"
)
PLAYER_BULLET_SPREAD_SOUND.set_volume(HIT_VOLUME)

###### Setup đạn "around" của Player:
PLAYER_BULLET_AROUND_WIDTH = 25
PLAYER_BULLET_AROUND_HEIGHT = 25
PLAYER_BULLET_AROUND_DELAY = 300
PLAYER_BULLET_AROUND_SPEED = 5
PLAYER_BULLET_AROUND_COUNT = 30
PLAYER_BULLET_AROUND_START_ANGLE = 5
PLAYER_BULLET_AROUND_END_ANGLE = 355
PLAYER_BULLET_AROUND_IMAGE = pygame.transform.scale(
    pygame.image.load("resources/images/Player_Bullet_Around.png"),
    (PLAYER_BULLET_AROUND_WIDTH, PLAYER_BULLET_AROUND_HEIGHT),
)
PLAYER_BULLET_AROUND_SOUND = pygame.mixer.Sound(
    "resources/sounds/Player_Bullet_Around.wav"
)
PLAYER_BULLET_AROUND_SOUND.set_volume(HIT_VOLUME)

###### Setup đạn "laser" của Player:
PLAYER_BULLET_LASER_WIDTH = 20
PLAYER_BULLET_LASER_HEIGHT = 40
PLAYER_BULLET_LASER_DELAY = 30
PLAYER_BULLET_LASER_SPEED = 10
PLAYER_BULLET_LASER_COUNT = 3
PLAYER_BULLET_LASER_START_ANGLE = 0
PLAYER_BULLET_LASER_END_ANGLE = 0
PLAYER_BULLET_LASER_IMAGE = pygame.transform.scale(
    pygame.image.load("resources/images/Player_Bullet_Laser.png"),
    (PLAYER_BULLET_LASER_WIDTH, PLAYER_BULLET_LASER_HEIGHT),
)
PLAYER_BULLET_LASER_SOUND = pygame.mixer.Sound(
    "resources/sounds/Player_Bullet_Laser.wav"
)
PLAYER_BULLET_LASER_SOUND.set_volume(HIT_VOLUME)

###### Danh sách đạn của Player:
PLAYER_BULLET_LIST = pygame.sprite.Group()
