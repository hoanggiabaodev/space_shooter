import pygame

ITEM_HEALTH = "item_health"
ITEM_SPECIAL = "item_special"
ITEM_SPREAD = "item_spread"
ITEM_AROUND = "item_around"
ITEM_LASER = "item_laser"
ITEM_UPDATE = "item_update"


ITEM_WIDTH = 30
ITEM_HEIGHT = 30

ITEM_SPEED_X = 0
ITEM_SPEED_Y = 2

ITEM_FREQUENCY_RATE = 0.3

ITEM_HEALTH_FREQUENCY_RATE = 0.3
ITEM_SPECIAL_FREQUENCY_RATE = 0.1
ITEM_SPREAD_FREQUENCY_RATE = 0.2
ITEM_AROUND_FREQUENCY_RATE = 0.1
ITEM_LASER_FREQUENCY_RATE = 0.1
ITEM_UPDATE_FREQUENCY_RATE = 0.3

ITEM_HEALTH_IMAGE = pygame.transform.scale(
    pygame.image.load("resources/images/Item_Health.png"), (ITEM_WIDTH, ITEM_HEIGHT)
)
ITEM_SPECIAL_IMAGE = pygame.transform.scale(
    pygame.image.load("resources/images/Item_Special.png"), (ITEM_WIDTH, ITEM_HEIGHT)
)
ITEM_SPREAD_IMAGE = pygame.transform.scale(
    pygame.image.load("resources/images/Item_Spread.png"), (ITEM_WIDTH, ITEM_HEIGHT)
)
ITEM_AROUND_IMAGE = pygame.transform.scale(
    pygame.image.load("resources/images/Item_Around.png"), (ITEM_WIDTH, ITEM_HEIGHT)
)
ITEM_LASER_IMAGE = pygame.transform.scale(
    pygame.image.load("resources/images/Item_Laser.png"), (ITEM_WIDTH, ITEM_HEIGHT)
)

ITEM_UPDATE_IMAGE = pygame.transform.scale(
    pygame.image.load("resources/images/Player_Update_Bullet_Normal.png"),
    (ITEM_WIDTH, ITEM_HEIGHT),
)

ITEM_HEALTH_REGENERATION = 50
ITEM_SPECIAL_DURATION = 6000
ITEM_SPREAD_DURATION = 4000
ITEM_AROUND_DURATION = 6000
ITEM_LASER_DURATION = 4000
ITEM_UPDATE_LEVEL_UP = 1

ITEM_LIST = pygame.sprite.Group()
