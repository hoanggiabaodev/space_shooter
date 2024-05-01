import pygame

# ========================================== SCREEN SETUP ==========================================

###### Setup kích thước cho Screen:
SCREEN_WIDTH = 420
SCREEN_HEIGHT = 650
BUTTON_WIDTH = 180
BUTTON_HEIGHT = 53

BACKGROUND_MUSIC_VOLUME = 0.5
###### Setup màn hình và ảnh, nhạc nền cho Game Loop Screen:
GAME_LOOP_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
GAME_LOOP_SCREEN_BACKGROUND = pygame.transform.scale(
    pygame.image.load("resources/images/Game_Loop_Background.png"),
    (SCREEN_WIDTH, SCREEN_HEIGHT),
)
GAME_LOOP_SCREEN_BACKGROUND_MUSIC = pygame.mixer.Sound(
    "resources/sounds/Game_Loop_Background_Music.wav"
)
GAME_LOOP_SCREEN_BACKGROUND_MUSIC.set_volume(BACKGROUND_MUSIC_VOLUME)

GAME_LOOP_SCREEN_BACKGROUND_SPEED = 2

###### Setup màn hình và ảnh nền cho Game Start Screen:
GAME_START_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
GAME_START_SCREEN_BACKGROUND = pygame.transform.scale(
    pygame.image.load("resources/images/Game_Start_Background.png"),
    (SCREEN_WIDTH, SCREEN_HEIGHT),
)

###### Setup màn hình và ảnh nền cho Game Over Screen:
GAME_STOP_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
GAME_STOP_SCREEN_BACKGROUND = pygame.transform.scale(
    pygame.image.load("resources/images/Game_Stop_Background.png"),
    (SCREEN_WIDTH, SCREEN_HEIGHT),
)

###### Setup màn hình và ảnh nền cho Game Pause:
GAME_PAUSE_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
GAME_PAUSE_SCREEN_BACKGROUND = pygame.transform.scale(
    pygame.image.load("resources/images/Game_Start_Background.png"),
    (SCREEN_WIDTH, SCREEN_HEIGHT),
)

GAME_HIGHTCORE_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
GAME_HIGHTCORE_SCREEN_BACKGROUND = pygame.transform.scale(
    pygame.image.load("resources/images/Game_Loop_Background.png"),
    (SCREEN_WIDTH, SCREEN_HEIGHT),
)

GAME_PLAY_BUTTON = pygame.transform.scale(
    pygame.image.load("resources/images/Game_Play_Button.png"),
    (BUTTON_WIDTH, BUTTON_HEIGHT),
)
GAME_REPLAY_BUTTON = pygame.transform.scale(
    pygame.image.load("resources/images/Game_Replay_Button.png"),
    (BUTTON_WIDTH, BUTTON_HEIGHT),
)
GAME_CONTINUE_BUTTON = pygame.transform.scale(
    pygame.image.load("resources/images/Game_Continue_Button.png"),
    (BUTTON_WIDTH, BUTTON_HEIGHT),
)
GAME_EXIT_BUTTON = pygame.transform.scale(
    pygame.image.load("resources/images/Game_Exit_Button.png"),
    (BUTTON_WIDTH, BUTTON_HEIGHT),
)
GAME_BACK_BUTTON = pygame.transform.scale(
    pygame.image.load("resources/images/Game_Back_Button.png"),
    (BUTTON_WIDTH, BUTTON_HEIGHT),
)
GAME_SELECT_BUTTON = pygame.transform.scale(
    pygame.image.load("resources/images/Game_Select_Button.png"),
    (BUTTON_WIDTH, BUTTON_HEIGHT),
)
GAME_RANKING_BUTTON = pygame.transform.scale(
    pygame.image.load("resources/images/Game_High_score_Button.png"),
    (BUTTON_WIDTH, BUTTON_HEIGHT),
)
GAME_COUNTDOWN_3 = pygame.transform.scale(
    pygame.image.load("resources/images/Number_3.png"), (78, 84)
)
GAME_COUNTDOWN_2 = pygame.transform.scale(
    pygame.image.load("resources/images/Number_2.png"), (78, 84)
)
GAME_COUNTDOWN_1 = pygame.transform.scale(
    pygame.image.load("resources/images/Number_1.png"), (78, 84)
)

###### Setup các item của chức năng chỉnh âm lượng

ITEMS_SOUND_WIDTH = 10
ITEMS_SOUND_HEIGHT = 30
ITEMS_SOUND_LEVEL_ONE_WIDTH = 4
ITEMS_SOUND_LEVEL_ONE_HEIGHT = 10
ITEMS_SOUND_LEVEL_TWO_WIDTH = 4
ITEMS_SOUND_LEVEL_TWO_HEIGHT = 15
ITEMS_SOUND_LEVEL_THREE_WIDTH = 4
ITEMS_SOUND_LEVEL_THREE_HEIGHT = 30

TRACK_WIDTH = 200
TRACK_HEIGHT = 8
THUMB_WIDTH = 17
THUMB_HEIGHT = 17

IMG_ITEMS_SOUND = pygame.transform.scale(
    pygame.image.load("resources/images/Sound.png"),
    (ITEMS_SOUND_WIDTH, ITEMS_SOUND_HEIGHT),
)
IMG_ITEMS_SL_ONE = pygame.transform.scale(
    pygame.image.load("resources/images/sound_one.png"),
    (ITEMS_SOUND_LEVEL_ONE_WIDTH, ITEMS_SOUND_LEVEL_ONE_HEIGHT),
)
IMG_ITEMS_SL_TWO = pygame.transform.scale(
    pygame.image.load("resources/images/sound_two.png"),
    (ITEMS_SOUND_LEVEL_TWO_WIDTH, ITEMS_SOUND_LEVEL_TWO_HEIGHT),
)
IMG_ITEMS_SL_THREE = pygame.transform.scale(
    pygame.image.load("resources/images/sound_three.png"),
    (ITEMS_SOUND_LEVEL_THREE_WIDTH, ITEMS_SOUND_LEVEL_THREE_HEIGHT),
)
IMG_TRACK = pygame.transform.scale(
    pygame.image.load("resources/images/Track.png"), (TRACK_WIDTH, TRACK_HEIGHT)
)
IMG_THUMB = pygame.transform.scale(
    pygame.image.load("resources/images/Thumb.png"), (THUMB_WIDTH, THUMB_HEIGHT)
)

ITEMS_SOUND_X = (SCREEN_WIDTH - ITEMS_SOUND_WIDTH) // 9
ITEMS_SOUND_Y = SCREEN_HEIGHT - 460
ITEMS_SOUND_ONE_X = (SCREEN_WIDTH - ITEMS_SOUND_LEVEL_ONE_WIDTH) // 7
ITEMS_SOUND_ONE_Y = SCREEN_HEIGHT - 450
ITEMS_SOUND_TWO_X = (SCREEN_WIDTH - ITEMS_SOUND_LEVEL_TWO_WIDTH) // 6 - 5.3
ITEMS_SOUND_TWO_Y = SCREEN_HEIGHT - 453
ITEMS_SOUND_THREE_X = (SCREEN_WIDTH - ITEMS_SOUND_LEVEL_THREE_WIDTH) // 5 - 16
ITEMS_SOUND_THREE_Y = SCREEN_HEIGHT - 460

EFFECT_SOUND_HIT_X = ITEMS_SOUND_X
EFFECT_SOUND_HIT_Y = ITEMS_SOUND_Y + 88
EFFECT_SOUND_ONE_X = ITEMS_SOUND_ONE_X
EFFECT_SOUND_ONE_Y = ITEMS_SOUND_ONE_Y + 88
EFFECT_SOUND_TWO_X = ITEMS_SOUND_TWO_X
EFFECT_SOUND_TWO_Y = ITEMS_SOUND_TWO_Y + 89
EFFECT_SOUND_THREE_X = ITEMS_SOUND_THREE_X
EFFECT_SOUND_THREE_Y = ITEMS_SOUND_THREE_Y + 88

TRACK_X = (SCREEN_WIDTH - TRACK_WIDTH) // 2
TRACK_Y = SCREEN_HEIGHT - 449
THUMB_X = TRACK_X + TRACK_WIDTH - THUMB_WIDTH // 2
THUMB_Y = SCREEN_HEIGHT - 453

TRACK_EFFECT_X = TRACK_X
TRACK_EFFECT_Y = TRACK_Y + 90
THUMB_EFFECT_X = THUMB_X
THUMB_EFFECT_Y = THUMB_Y + 89

GAME_PLAY_BUTTON_X = (SCREEN_WIDTH - BUTTON_WIDTH) // 2
GAME_PLAY_BUTTON_Y = SCREEN_HEIGHT - 220
GAME_REPLAY_BUTTON_X = (SCREEN_WIDTH - BUTTON_WIDTH) // 2
GAME_REPLAY_BUTTON_Y = SCREEN_HEIGHT - 220
GAME_CONTINUE_BUTTON_X = (SCREEN_WIDTH - BUTTON_WIDTH) // 2
GAME_CONTINUE_BUTTON_Y = SCREEN_HEIGHT - 150
GAME_EXIT_BUTTON_X = (SCREEN_WIDTH - BUTTON_WIDTH) // 2
GAME_EXIT_BUTTON_Y = SCREEN_HEIGHT - 150
GAME_BACK_BUTTON_X = (SCREEN_WIDTH - BUTTON_WIDTH) // 2
GAME_BACK_BUTTON_Y = SCREEN_HEIGHT - 290
GAME_SELECT_BUTTON_X = (SCREEN_WIDTH - BUTTON_WIDTH) // 2
GAME_SELECT_BUTTON_Y = SCREEN_HEIGHT - 223


START_IMAGE_WIDTH = 400
START_IMAGE_HEIGHT = 400
START_IMAGE = pygame.transform.scale(
    pygame.image.load("resources/images/Start_Image.png"),
    (START_IMAGE_WIDTH, START_IMAGE_HEIGHT),
)
HIGHTCORE_IMAGE = pygame.transform.scale(
    pygame.image.load("resources/images/Start_Image.png"),
    (START_IMAGE_WIDTH // 1.5, START_IMAGE_HEIGHT // 1.5),
)
START_IMAGE_X = 10
START_IMAGE_Y = 10

STOP_IMAGE_WIDTH = 400
STOP_IMAGE_HEIGHT = 400
STOP_IMAGE = pygame.transform.scale(
    pygame.image.load("resources/images/Stop_Image.png"),
    (STOP_IMAGE_WIDTH, STOP_IMAGE_HEIGHT),
)
STOP_IMAGE_X = 10
STOP_IMAGE_Y = 10
