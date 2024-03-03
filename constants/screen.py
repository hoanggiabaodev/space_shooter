import pygame

# ========================================== SCREEN SETUP ==========================================

###### Setup kích thước cho Screen:
SCREEN_WIDTH = 420
SCREEN_HEIGHT = 650
BUTTON_WIDTH = 180
BUTTON_HEIGHT = 53

###### Setup màn hình và ảnh, nhạc nền cho Game Loop Screen:
GAME_LOOP_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
GAME_LOOP_SCREEN_BACKGROUND = pygame.transform.scale(pygame.image.load("resources/images/Game_Loop_Background.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
GAME_LOOP_SCREEN_BACKGROUND_MUSIC = pygame.mixer.Sound("resources/sounds/Game_Loop_Background_Music.wav")
GAME_LOOP_SCREEN_BACKGROUND_SPEED = 2

###### Setup màn hình và ảnh nền cho Game Start Screen:
GAME_START_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
GAME_START_SCREEN_BACKGROUND = pygame.transform.scale(pygame.image.load("resources/images/Game_Start_Background.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))

###### Setup màn hình và ảnh nền cho Game Over Screen:
GAME_STOP_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
GAME_STOP_SCREEN_BACKGROUND = pygame.transform.scale(pygame.image.load("resources/images/Game_Stop_Background.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))

GAME_PLAY_BUTTON = pygame.transform.scale(pygame.image.load("resources/images/Game_Play_Button.png"),  (BUTTON_WIDTH, BUTTON_HEIGHT))
GAME_REPLAY_BUTTON = pygame.transform.scale(pygame.image.load("resources/images/Game_Replay_Button.png"),  (BUTTON_WIDTH, BUTTON_HEIGHT))
GAME_CONTINUE_BUTTON = pygame.transform.scale(pygame.image.load("resources/images/Game_Continue_Button.png"),  (BUTTON_WIDTH, BUTTON_HEIGHT))
GAME_EXIT_BUTTON = pygame.transform.scale(pygame.image.load("resources/images/Game_Exit_Button.png"),  (BUTTON_WIDTH, BUTTON_HEIGHT))

GAME_PLAY_BUTTON_X = (SCREEN_WIDTH - BUTTON_WIDTH) // 2
GAME_PLAY_BUTTON_Y = SCREEN_HEIGHT - 220
GAME_REPLAY_BUTTON_X = (SCREEN_WIDTH - BUTTON_WIDTH) // 2
GAME_REPLAY_BUTTON_Y = SCREEN_HEIGHT - 220
GAME_CONTINUE_BUTTON_X = (SCREEN_WIDTH - BUTTON_WIDTH) // 2
GAME_CONTINUE_BUTTON_Y = SCREEN_HEIGHT - 150
GAME_EXIT_BUTTON_X = (SCREEN_WIDTH - BUTTON_WIDTH) // 2
GAME_EXIT_BUTTON_Y = SCREEN_HEIGHT - 150

START_IMAGE_WIDTH = 400
START_IMAGE_HEIGHT = 400
START_IMAGE = pygame.transform.scale(pygame.image.load("resources/images/Start_Image.png"),  (START_IMAGE_WIDTH, START_IMAGE_HEIGHT))
START_IMAGE_X = 10
START_IMAGE_Y = 10

STOP_IMAGE_WIDTH = 400
STOP_IMAGE_HEIGHT = 400
STOP_IMAGE = pygame.transform.scale(pygame.image.load("resources/images/Stop_Image.png"),  (STOP_IMAGE_WIDTH, STOP_IMAGE_HEIGHT))
STOP_IMAGE_X = 10
STOP_IMAGE_Y = 10

