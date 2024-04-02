import pygame, sys, time

GAME_LOGO = pygame.image.load("resources/images/Game_Logo.png")

pygame.init()
pygame.display.set_caption("Space Shooter")
pygame.display.set_icon(GAME_LOGO)
clock = pygame.time.Clock()
current_username = None
FPS = 60

###### Setup kiểu bắn đạn:
NORMAL_TYPE = "normal"
SPECIAL_TYPE = "special"
SPREAD_TYPE = "spread"
AROUND_TYPE = "around"
LASER_TYPE = "laser"

###### Setup hình ảnh các con số:
NUMBER_WIDTH = 15
NUMBER_HEIGHT = 15
NUMBER_0 = pygame.transform.scale(pygame.image.load("resources/images/Number_0.png"), (NUMBER_WIDTH, NUMBER_HEIGHT))
NUMBER_1 = pygame.transform.scale(pygame.image.load("resources/images/Number_1.png"), (NUMBER_WIDTH, NUMBER_HEIGHT))
NUMBER_2 = pygame.transform.scale(pygame.image.load("resources/images/Number_2.png"), (NUMBER_WIDTH, NUMBER_HEIGHT))
NUMBER_3 = pygame.transform.scale(pygame.image.load("resources/images/Number_3.png"), (NUMBER_WIDTH, NUMBER_HEIGHT))
NUMBER_4 = pygame.transform.scale(pygame.image.load("resources/images/Number_4.png"), (NUMBER_WIDTH, NUMBER_HEIGHT))
NUMBER_5 = pygame.transform.scale(pygame.image.load("resources/images/Number_5.png"), (NUMBER_WIDTH, NUMBER_HEIGHT))
NUMBER_6 = pygame.transform.scale(pygame.image.load("resources/images/Number_6.png"), (NUMBER_WIDTH, NUMBER_HEIGHT))
NUMBER_7 = pygame.transform.scale(pygame.image.load("resources/images/Number_7.png"), (NUMBER_WIDTH, NUMBER_HEIGHT))
NUMBER_8 = pygame.transform.scale(pygame.image.load("resources/images/Number_8.png"), (NUMBER_WIDTH, NUMBER_HEIGHT))
NUMBER_9 = pygame.transform.scale(pygame.image.load("resources/images/Number_9.png"), (NUMBER_WIDTH, NUMBER_HEIGHT))
