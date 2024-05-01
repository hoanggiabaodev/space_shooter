from constants.setup import *
from constants.screen import (
    GAME_COUNTDOWN_1,
    GAME_COUNTDOWN_2,
    GAME_COUNTDOWN_3,
    GAME_HIGHTCORE_SCREEN,
    GAME_HIGHTCORE_SCREEN_BACKGROUND,
    GAME_RANKING_BUTTON,
    HIGHTCORE_IMAGE,
    SCREEN_HEIGHT,
    GAME_LOOP_SCREEN,
    GAME_LOOP_SCREEN_BACKGROUND,
    GAME_LOOP_SCREEN_BACKGROUND_SPEED,
    GAME_LOOP_SCREEN_BACKGROUND_MUSIC,
    SCREEN_WIDTH,
)
from constants.screen import GAME_START_SCREEN, GAME_START_SCREEN_BACKGROUND
from constants.screen import GAME_STOP_SCREEN, GAME_STOP_SCREEN_BACKGROUND
from constants.screen import GAME_PAUSE_SCREEN, GAME_PAUSE_SCREEN_BACKGROUND
from constants.screen import BUTTON_WIDTH, BUTTON_HEIGHT
from constants.screen import GAME_PLAY_BUTTON, GAME_PLAY_BUTTON_X, GAME_PLAY_BUTTON_Y
from constants.screen import (
    GAME_REPLAY_BUTTON,
    GAME_REPLAY_BUTTON_X,
    GAME_REPLAY_BUTTON_Y,
)
from constants.screen import (
    GAME_REPLAY_BUTTON,
    GAME_REPLAY_BUTTON_X,
    GAME_REPLAY_BUTTON_Y,
)
from constants.screen import GAME_EXIT_BUTTON, GAME_EXIT_BUTTON_X, GAME_EXIT_BUTTON_Y
from constants.screen import GAME_CONTINUE_BUTTON_X, GAME_CONTINUE_BUTTON_Y
from constants.screen import GAME_BACK_BUTTON, GAME_BACK_BUTTON_X, GAME_BACK_BUTTON_Y
from constants.screen import (
    GAME_SELECT_BUTTON,
    GAME_SELECT_BUTTON_X,
    GAME_SELECT_BUTTON_Y,
)
from constants.screen import IMG_ITEMS_SOUND, ITEMS_SOUND_X, ITEMS_SOUND_Y
from constants.screen import IMG_ITEMS_SL_ONE, ITEMS_SOUND_ONE_X, ITEMS_SOUND_ONE_Y
from constants.screen import IMG_ITEMS_SL_TWO, ITEMS_SOUND_TWO_X, ITEMS_SOUND_TWO_Y
from constants.screen import (
    IMG_ITEMS_SL_THREE,
    ITEMS_SOUND_THREE_X,
    ITEMS_SOUND_THREE_Y,
)
from constants.screen import IMG_TRACK, TRACK_X, TRACK_Y, TRACK_WIDTH, TRACK_HEIGHT
from constants.screen import IMG_THUMB, THUMB_X, THUMB_Y, THUMB_WIDTH, THUMB_HEIGHT
from constants.screen import START_IMAGE, START_IMAGE_X, START_IMAGE_Y
from constants.screen import STOP_IMAGE, STOP_IMAGE_X, STOP_IMAGE_Y
from constants.screen import (
    EFFECT_SOUND_HIT_X,
    EFFECT_SOUND_HIT_Y,
    EFFECT_SOUND_ONE_X,
    EFFECT_SOUND_ONE_Y,
    EFFECT_SOUND_TWO_X,
    EFFECT_SOUND_TWO_Y,
    EFFECT_SOUND_THREE_X,
    EFFECT_SOUND_THREE_Y,
)
from constants.screen import (
    TRACK_EFFECT_X,
    TRACK_EFFECT_Y,
    THUMB_EFFECT_X,
    THUMB_EFFECT_Y,
)
from constants.bullet_player import PLAYER_BULLET_LIST, HIT_VOLUME
from constants.bullet_enemy import (
    ENEMY_LEVEL_1_BULLET_LIST,
    ENEMY_LEVEL_2_BULLET_LIST,
    ENEMY_LEVEL_3_BULLET_LIST,
    ENEMY_LEVEL_4_BULLET_LIST,
    ENEMY_LEVEL_5_BULLET_LIST,
)
from constants.enemy import ENEMY_LIST, ENEMY_GENETATE_DELAY
from constants.player import (
    PLAYER_LIST,
    BUTTON_HEIGHT_OF_PAUSE,
    BUTTON_WIDTH_OF_PAUSE,
    BUTTON_POSITION_WIDTH,
    BUTTON_POSITION_HEIGHT,
)
from constants.item import ITEM_LIST
from src.player import Player
from src.enemy import Enemy
from constants.screen import BACKGROUND_MUSIC_VOLUME
from constants.bullet_player import (
    PLAYER_BULLET_NORMAL_SOUND,
    PLAYER_BULLET_SPECIAL_SOUND,
    PLAYER_BULLET_SPREAD_SOUND,
    PLAYER_BULLET_AROUND_SOUND,
    PLAYER_BULLET_LASER_SOUND,
)
import mysql.connector

# ================================ Game Start Loop ================================


def game_start_loop():

    while True:
        GAME_START_SCREEN.blit(GAME_START_SCREEN_BACKGROUND, (0, 0))
        GAME_START_SCREEN.blit(START_IMAGE, (START_IMAGE_X, START_IMAGE_Y))
        GAME_START_SCREEN.blit(
            GAME_PLAY_BUTTON, (GAME_PLAY_BUTTON_X, GAME_PLAY_BUTTON_Y - 20)
        )
        GAME_START_SCREEN.blit(
            GAME_RANKING_BUTTON, (GAME_SELECT_BUTTON_X, GAME_SELECT_BUTTON_Y + 54)
        )
        GAME_START_SCREEN.blit(
            GAME_EXIT_BUTTON, (GAME_EXIT_BUTTON_X, GAME_EXIT_BUTTON_Y + 50)
        )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pygame.Rect(
                    GAME_PLAY_BUTTON_X,
                    GAME_PLAY_BUTTON_Y - 20,
                    BUTTON_WIDTH,
                    BUTTON_HEIGHT,
                ).collidepoint(pos):
                    GAME_LOOP_SCREEN_BACKGROUND_MUSIC.play()
                    game_loop()
                elif pygame.Rect(
                    GAME_SELECT_BUTTON_X,
                    GAME_SELECT_BUTTON_Y + 54,
                    BUTTON_WIDTH,
                    BUTTON_HEIGHT,
                ).collidepoint(pos):
                    show_ranking = True  # Biến để kiểm soát việc hiển thị bảng xếp hạng

                    while show_ranking:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                sys.exit()
                            elif event.type == pygame.MOUSEBUTTONUP:
                                pos = pygame.mouse.get_pos()
                                if pygame.Rect(
                                    GAME_EXIT_BUTTON_X,
                                    GAME_EXIT_BUTTON_Y + 50,
                                    BUTTON_WIDTH,
                                    BUTTON_HEIGHT,
                                ).collidepoint(pos):
                                    show_ranking = False  # Người dùng chọn nút "Back" => thoát khỏi vòng lặp

                        # Vẽ nền và bảng xếp hạng
                        GAME_HIGHTCORE_SCREEN.blit(
                            GAME_HIGHTCORE_SCREEN_BACKGROUND, (0, 0)
                        )
                        draw_ranking_table(GAME_HIGHTCORE_SCREEN, current_username)

                        # Vẽ nút "Back"
                        GAME_HIGHTCORE_SCREEN.blit(
                            GAME_BACK_BUTTON,
                            (GAME_EXIT_BUTTON_X, GAME_EXIT_BUTTON_Y + 50),
                        )

                        pygame.display.update()

                elif pygame.Rect(
                    GAME_EXIT_BUTTON_X,
                    GAME_EXIT_BUTTON_Y + 50,
                    BUTTON_WIDTH,
                    BUTTON_HEIGHT,
                ).collidepoint(pos):
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loop()
        pygame.display.update()


# ================================ Game Stop Loop ================================
def game_stop_loop(player):
    PLAYER_LIST.empty()
    PLAYER_BULLET_LIST.empty()
    ENEMY_LIST.empty()
    ITEM_LIST.empty()
    ENEMY_LEVEL_1_BULLET_LIST.empty()
    ENEMY_LEVEL_2_BULLET_LIST.empty()
    ENEMY_LEVEL_3_BULLET_LIST.empty()
    ENEMY_LEVEL_4_BULLET_LIST.empty()
    ENEMY_LEVEL_5_BULLET_LIST.empty()
    GAME_LOOP_SCREEN_BACKGROUND_MUSIC.stop()
    while True:
        GAME_STOP_SCREEN.blit(GAME_STOP_SCREEN_BACKGROUND, (0, 0))
        GAME_STOP_SCREEN.blit(STOP_IMAGE, (STOP_IMAGE_X, STOP_IMAGE_Y))
        GAME_STOP_SCREEN.blit(
            GAME_REPLAY_BUTTON, (GAME_REPLAY_BUTTON_X, GAME_REPLAY_BUTTON_Y)
        )
        GAME_STOP_SCREEN.blit(
            GAME_EXIT_BUTTON, (GAME_EXIT_BUTTON_X, GAME_EXIT_BUTTON_Y)
        )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pygame.Rect(
                    GAME_REPLAY_BUTTON_X,
                    GAME_REPLAY_BUTTON_Y,
                    BUTTON_WIDTH,
                    BUTTON_HEIGHT,
                ).collidepoint(pos):
                    game_loop()
                elif pygame.Rect(
                    GAME_EXIT_BUTTON_X, GAME_EXIT_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT
                ).collidepoint(pos):
                    sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loop()
        Enemy.save_highscore(username=current_username, score=player.score)

        pygame.display.update()


# ================================ Game Pause ===============================


def Game_pause(screen):
    countdown_screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    countdown_screen.blit(screen, (0, 0))
    pygame.display.update()
    while True:
        GAME_PAUSE_SCREEN.blit(GAME_PAUSE_SCREEN_BACKGROUND, (0, 0))
        GAME_PAUSE_SCREEN.blit(
            GAME_BACK_BUTTON, (GAME_BACK_BUTTON_X, GAME_BACK_BUTTON_Y)
        )
        GAME_PAUSE_SCREEN.blit(
            GAME_SELECT_BUTTON, (GAME_SELECT_BUTTON_X, GAME_SELECT_BUTTON_Y)
        )
        GAME_PAUSE_SCREEN.blit(
            GAME_EXIT_BUTTON, (GAME_EXIT_BUTTON_X, GAME_EXIT_BUTTON_Y)
        )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pygame.Rect(
                    GAME_BACK_BUTTON_X, GAME_BACK_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT
                ).collidepoint(pos):
                    screen.blit(countdown_screen, (0, 0))
                    numbers = [
                        GAME_COUNTDOWN_3,
                        GAME_COUNTDOWN_2,
                        GAME_COUNTDOWN_1,
                    ]
                    for number_image in numbers:
                        number_width, number_height = number_image.get_size()
                        x = (SCREEN_WIDTH - number_width) // 2
                        y = (SCREEN_HEIGHT - number_height) // 2
                        screen.blit(number_image, (x, y))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        screen.blit(countdown_screen, (0, 0))
                    return False
                elif pygame.Rect(
                    GAME_EXIT_BUTTON_X, GAME_EXIT_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT
                ).collidepoint(pos):
                    sys.exit()
                elif pygame.Rect(
                    GAME_SELECT_BUTTON_X,
                    GAME_SELECT_BUTTON_Y,
                    BUTTON_WIDTH,
                    BUTTON_HEIGHT,
                ).collidepoint(pos):
                    game_select()
        pygame.display.update()


# ================================ Game Select ================================


def game_select():
    dragging = False
    dragging_effect = False
    global THUMB_X
    global BACKGROUND_MUSIC_VOLUME
    global HIT_VOLUME

    # Vẽ lại track và thumb dựa trên BACKGROUND_MUSIC_VOLUME ban đầu
    TRACK_NEW_WIDTH = int(TRACK_WIDTH * BACKGROUND_MUSIC_VOLUME)
    TRACK_RECT = pygame.Rect(0, 0, TRACK_NEW_WIDTH, TRACK_HEIGHT)
    THUMB_X = TRACK_X + TRACK_NEW_WIDTH - THUMB_WIDTH // 2
    # Vẽ lại track và thumb dựa trên HIT_VOLUME ban đầu
    TRACK_NEW_EFF_WIDTH = int(TRACK_WIDTH * HIT_VOLUME)
    TRACK_RECT_ = pygame.Rect(0, 0, TRACK_NEW_EFF_WIDTH, TRACK_HEIGHT)
    THUMB_EFFECT_X = TRACK_EFFECT_X + TRACK_NEW_EFF_WIDTH - THUMB_WIDTH // 2

    # tạo chuỗi hiển thị số của âm lượng
    font = pygame.font.Font(None, 23)  # Khởi tạo font với kích thước 23

    # Màu sắc của văn bản (ví dụ: màu trắng)
    color = (255, 255, 255)

    # Tạo chữ âm lượng nhạc nền
    text_vari_ = "Soundtrack"
    text_surface_ = font.render(text_vari_, True, color)
    text_rect_ = text_surface_.get_rect()
    text_rect_.x = ITEMS_SOUND_X  # Đặt văn bản ở tọa độ x
    text_rect_.y = ITEMS_SOUND_Y - 40  # Đặt văn bản ở tọa độ y

    # Tạo chữ âm lượng hiệu ứng
    text_vari__ = "Soundeffect"
    text_surface__ = font.render(text_vari__, True, color)
    text_rect__ = text_surface__.get_rect()
    text_rect__.x = EFFECT_SOUND_HIT_X
    text_rect__.y = EFFECT_SOUND_HIT_Y - 40

    while True:
        GAME_PAUSE_SCREEN.blit(GAME_PAUSE_SCREEN_BACKGROUND, (0, 0))
        GAME_PAUSE_SCREEN.blit(IMG_ITEMS_SOUND, (ITEMS_SOUND_X, ITEMS_SOUND_Y))
        GAME_PAUSE_SCREEN.blit(
            IMG_ITEMS_SOUND, (EFFECT_SOUND_HIT_X, EFFECT_SOUND_HIT_Y)
        )
        GAME_LOOP_SCREEN.blit(text_surface_, text_rect_)
        GAME_LOOP_SCREEN.blit(text_surface__, text_rect__)

        if BACKGROUND_MUSIC_VOLUME >= 0.75:
            GAME_PAUSE_SCREEN.blit(
                IMG_ITEMS_SL_ONE, (ITEMS_SOUND_ONE_X, ITEMS_SOUND_ONE_Y)
            )
            GAME_PAUSE_SCREEN.blit(
                IMG_ITEMS_SL_TWO, (ITEMS_SOUND_TWO_X, ITEMS_SOUND_TWO_Y)
            )
            GAME_PAUSE_SCREEN.blit(
                IMG_ITEMS_SL_THREE, (ITEMS_SOUND_THREE_X, ITEMS_SOUND_THREE_Y)
            )
        elif 0.5 <= BACKGROUND_MUSIC_VOLUME < 0.75:
            GAME_PAUSE_SCREEN.blit(
                IMG_ITEMS_SL_ONE, (ITEMS_SOUND_ONE_X, ITEMS_SOUND_ONE_Y)
            )
            GAME_PAUSE_SCREEN.blit(
                IMG_ITEMS_SL_TWO, (ITEMS_SOUND_TWO_X, ITEMS_SOUND_TWO_Y)
            )
        elif 0 < BACKGROUND_MUSIC_VOLUME < 0.5:
            GAME_PAUSE_SCREEN.blit(
                IMG_ITEMS_SL_ONE, (ITEMS_SOUND_ONE_X, ITEMS_SOUND_ONE_Y)
            )
        # Không vẽ gì nếu HIT_VOLUME < 0.25

        if HIT_VOLUME >= 0.75:
            GAME_PAUSE_SCREEN.blit(
                IMG_ITEMS_SL_ONE, (EFFECT_SOUND_ONE_X, EFFECT_SOUND_ONE_Y)
            )
            GAME_PAUSE_SCREEN.blit(
                IMG_ITEMS_SL_TWO, (EFFECT_SOUND_TWO_X, EFFECT_SOUND_TWO_Y)
            )
            GAME_PAUSE_SCREEN.blit(
                IMG_ITEMS_SL_THREE, (EFFECT_SOUND_THREE_X, EFFECT_SOUND_THREE_Y)
            )
        elif 0.5 <= HIT_VOLUME < 0.75:
            GAME_PAUSE_SCREEN.blit(
                IMG_ITEMS_SL_ONE, (EFFECT_SOUND_ONE_X, EFFECT_SOUND_ONE_Y)
            )
            GAME_PAUSE_SCREEN.blit(
                IMG_ITEMS_SL_TWO, (EFFECT_SOUND_TWO_X, EFFECT_SOUND_TWO_Y)
            )
        elif 0 < HIT_VOLUME < 0.5:
            GAME_PAUSE_SCREEN.blit(
                IMG_ITEMS_SL_ONE, (EFFECT_SOUND_ONE_X, EFFECT_SOUND_ONE_Y)
            )

        GAME_PAUSE_SCREEN.blit(
            GAME_BACK_BUTTON, (GAME_BACK_BUTTON_X, GAME_BACK_BUTTON_Y + 100)
        )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                if pygame.Rect(
                    THUMB_X, THUMB_Y, THUMB_WIDTH, THUMB_HEIGHT
                ).collidepoint(pos):
                    dragging = True
                if pygame.Rect(
                    THUMB_EFFECT_X, THUMB_EFFECT_Y, THUMB_WIDTH, THUMB_HEIGHT
                ).collidepoint(pos):
                    dragging_effect = True  # Bắt đầu kéo trượt TRACK_EFFECT
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    dragging = False
                    dragging_effect = False
                    pos = pygame.mouse.get_pos()
                    if pygame.Rect(
                        GAME_BACK_BUTTON_X,
                        GAME_BACK_BUTTON_Y + 100,
                        BUTTON_WIDTH,
                        BUTTON_HEIGHT,
                    ).collidepoint(pos):
                        return
            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    pos = pygame.mouse.get_pos()
                    # Giới hạn vị trí mới của thumb trong phạm vi của track
                    new_thumb_x = pos[0]
                    if new_thumb_x < TRACK_X:
                        new_thumb_x = TRACK_X - THUMB_WIDTH // 2
                    elif new_thumb_x > TRACK_X + TRACK_WIDTH - THUMB_WIDTH // 2:
                        new_thumb_x = TRACK_X + TRACK_WIDTH - THUMB_WIDTH // 2
                    THUMB_X = new_thumb_x

                    # Tính toán lại giá trị của HIT_VOLUME
                    BACKGROUND_MUSIC_VOLUME = (
                        THUMB_X - TRACK_X + THUMB_WIDTH // 2
                    ) / TRACK_WIDTH

                    # Tính toán lại kích thước mới của TRACK và TRACK_RECT
                    TRACK_NEW_WIDTH = int(TRACK_WIDTH * BACKGROUND_MUSIC_VOLUME)
                    TRACK_RECT = pygame.Rect(0, 0, TRACK_NEW_WIDTH, TRACK_HEIGHT)
                if dragging_effect:
                    pos = pygame.mouse.get_pos()
                    new_thumb_x = pos[0]
                    if new_thumb_x < TRACK_EFFECT_X:
                        new_thumb_x = TRACK_EFFECT_X - THUMB_WIDTH // 2
                    elif new_thumb_x > TRACK_EFFECT_X + TRACK_WIDTH - THUMB_WIDTH // 2:
                        new_thumb_x = TRACK_EFFECT_X + TRACK_WIDTH - THUMB_WIDTH // 2

                    THUMB_EFFECT_X = new_thumb_x
                    HIT_VOLUME = (
                        THUMB_EFFECT_X - TRACK_EFFECT_X + THUMB_WIDTH // 2
                    ) / TRACK_WIDTH
                    TRACK_NEW_EFF_WIDTH = int(TRACK_WIDTH * HIT_VOLUME)
                    TRACK_RECT_ = pygame.Rect(0, 0, TRACK_NEW_EFF_WIDTH, TRACK_HEIGHT)

        text_variable = str(int(BACKGROUND_MUSIC_VOLUME * 100))
        # Vẽ văn bản lên màn hình
        text_surface = font.render(text_variable, True, color)

        # Vị trí của văn bản trên màn hình
        text_rect = text_surface.get_rect()
        text_rect.x = TRACK_X + TRACK_WIDTH + THUMB_WIDTH + 10  # Đặt văn bản ở tọa độ x
        text_rect.y = THUMB_Y  # Đặt văn bản ở tọa độ y
        GAME_LOOP_SCREEN.blit(text_surface, text_rect)
        # đặt lại âm lương của nhạc nền và hiệu ứng
        GAME_LOOP_SCREEN_BACKGROUND_MUSIC.set_volume(BACKGROUND_MUSIC_VOLUME)

        text_variable_ = str(int(HIT_VOLUME * 100))
        text_surface___ = font.render(text_variable_, True, color)
        text_rect___ = text_surface___.get_rect()
        text_rect___.x = TRACK_EFFECT_X + TRACK_WIDTH + THUMB_WIDTH + 10
        text_rect___.y = THUMB_EFFECT_Y
        GAME_LOOP_SCREEN.blit(text_surface___, text_rect___)

        PLAYER_BULLET_NORMAL_SOUND.set_volume(HIT_VOLUME)
        PLAYER_BULLET_SPECIAL_SOUND.set_volume(HIT_VOLUME)
        PLAYER_BULLET_SPREAD_SOUND.set_volume(HIT_VOLUME)
        PLAYER_BULLET_AROUND_SOUND.set_volume(HIT_VOLUME)
        PLAYER_BULLET_LASER_SOUND.set_volume(HIT_VOLUME)
        # Vẽ lại toàn bộ IMG_TRACK, nhưng chỉ hiển thị phần tương ứng với TRACK_RECT
        GAME_PAUSE_SCREEN.blit(IMG_TRACK, (TRACK_X, TRACK_Y), TRACK_RECT)
        # Vẽ lại IMG_THUMB
        GAME_PAUSE_SCREEN.blit(IMG_THUMB, (THUMB_X, THUMB_Y))

        GAME_PAUSE_SCREEN.blit(IMG_TRACK, (TRACK_EFFECT_X, TRACK_EFFECT_Y), TRACK_RECT_)

        GAME_PAUSE_SCREEN.blit(IMG_THUMB, (THUMB_EFFECT_X, THUMB_EFFECT_Y))

        pygame.display.update()


# ================================ Game Loop ================================


def game_loop():
    player = Player()
    PLAYER_LIST.add(player)
    game_over = False
    SKIN_ANGLE = 0
    game_pause = False
    enemy_spawn_time = 0.0
    GAME_LOOP_SCREEN_BACKGROUND_Y = 0
    enemy_bullet_list = [
        ENEMY_LEVEL_1_BULLET_LIST,
        ENEMY_LEVEL_2_BULLET_LIST,
        ENEMY_LEVEL_3_BULLET_LIST,
        ENEMY_LEVEL_4_BULLET_LIST,
        ENEMY_LEVEL_5_BULLET_LIST,
    ]
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pygame.Rect(
                    BUTTON_POSITION_WIDTH,
                    BUTTON_POSITION_HEIGHT,
                    BUTTON_WIDTH_OF_PAUSE,
                    BUTTON_HEIGHT_OF_PAUSE,
                ).collidepoint(pos):
                    screen = pygame.display.get_surface()
                    game_pause = True
                elif pygame.Rect(
                    GAME_CONTINUE_BUTTON_X,
                    GAME_CONTINUE_BUTTON_Y - (SCREEN_HEIGHT // 3),
                    BUTTON_WIDTH,
                    BUTTON_HEIGHT,
                ).collidepoint(pos):
                    game_pause = False
        if game_pause:
            game_pause = Game_pause(screen)
            if not game_pause:
                game_pause = False

        else:
            clock.tick(FPS)
            # ====================================== SCREEN ======================================
            GAME_LOOP_SCREEN_BACKGROUND_Y += GAME_LOOP_SCREEN_BACKGROUND_SPEED
            if GAME_LOOP_SCREEN_BACKGROUND_Y >= 0:
                GAME_LOOP_SCREEN_BACKGROUND_Y = -SCREEN_HEIGHT
            GAME_LOOP_SCREEN.blit(
                GAME_LOOP_SCREEN_BACKGROUND, (0, GAME_LOOP_SCREEN_BACKGROUND_Y)
            )
            GAME_LOOP_SCREEN.blit(
                GAME_LOOP_SCREEN_BACKGROUND,
                (0, GAME_LOOP_SCREEN_BACKGROUND_Y + SCREEN_HEIGHT),
            )
            # ====================================== ENEMY ====================================== #
            enemy_spawn_time += 1 / FPS

            if enemy_spawn_time >= ENEMY_GENETATE_DELAY:
                Enemy.generate_enemies()
                enemy_spawn_time = 0.0

            for enemy in ENEMY_LIST:
                enemy.update()

            for enemy in ENEMY_LIST:
                enemy.update()
                player.player_collide(enemy)

            # ====================================== PLAYER ====================================== #
            SKIN_ANGLE += 1
            if SKIN_ANGLE >= 360:
                SKIN_ANGLE = 0

            player.update(SKIN_ANGLE)

            # ====================================== ENEMY BULLET ====================================== #
            for bullet in PLAYER_BULLET_LIST:
                for enemy in ENEMY_LIST:
                    enemy.enemy_hit(bullet, player)
            for bullet_list in enemy_bullet_list:
                for bullet in bullet_list:
                    bullet.update()
                    player.player_hit(bullet)

            # ====================================== PLAYER BULLET ====================================== #
            for bullet in PLAYER_BULLET_LIST:
                bullet.update(player)

            # ====================================== ITEM ====================================== #
            for item in ITEM_LIST:
                item.update()
                player.get_item(item)

            pygame.display.update()

            if len(PLAYER_LIST) == 0:
                game_over = True

    if game_over:
        game_stop_loop(player)


# def draw_ranking_table(screen):
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",  # Thay bằng mật khẩu MySQL của bạn
#         database="solar_system_protection",
#     )
#     cursor = conn.cursor()
#     # Vẽ nền mờ cho bảng xếp hạng
#     ranking_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

#     # Tiêu đề cho các cột
#     columns = ["STT", "Tài khoản", "Điểm số"]

#     font = pygame.font.Font(None, 16)  # Font chữ
#     text_color = (255, 255, 255)  # Màu chữ trắng

#     # Tính toán vị trí y của tiêu đề
#     title_y = 50

#     # Tính toán số lượng cột và kích thước của mỗi cột
#     num_columns = len(columns)
#     column_width = SCREEN_WIDTH // num_columns

#     # Tính toán vị trí x của mỗi cột
#     column_x_positions = [i * column_width for i in range(num_columns)]

#     # Vẽ tiêu đề
#     for i, col in enumerate(columns):
#         text = font.render(col, True, text_color)
#         # Tính toán vị trí x cho từng cột để căn giữa tiêu đề
#         x = column_x_positions[i] + (column_width - text.get_width()) // 2
#         ranking_surface.blit(text, (x, title_y))  # Đặt vị trí của tiêu đề

#     # Lấy dữ liệu từ cơ sở dữ liệu và vẽ lên bảng xếp hạng
#     cursor.execute(
#         "SELECT username, highest_score FROM users ORDER BY highest_score DESC LIMIT 10"
#     )
#     top_10_users = cursor.fetchall()

#     # ranking_data = cursor.fetchall()

#     # Tính toán vị trí y của hàng đầu tiên
#     data_y = title_y + 20

#     # Vẽ dữ liệu lên bảng xếp hạng
#     for i, row_data in enumerate(top_10_users):
#         # Vẽ số thứ tự
#         stt_text = font.render(str(i + 1), True, text_color)
#         # Tính toán vị trí x cho số thứ tự sao cho nó ở giữa cột "STT"
#         stt_x = column_x_positions[0] + (column_width - stt_text.get_width()) // 2
#         ranking_surface.blit(stt_text, (stt_x, data_y))  # Đặt vị trí của số thứ tự

#         # Tính toán vị trí x cho từng cột dữ liệu
#         for j, col_data in enumerate(row_data):
#             text = font.render(str(col_data), True, text_color)
#             # Tính toán vị trí x cho từng cột để căn giữa dữ liệu
#             x = column_x_positions[j + 1] + (column_width - text.get_width()) // 2
#             ranking_surface.blit(text, (x, data_y))  # Đặt vị trí của dữ liệu
#         data_y += 20  # Di chuyển xuống hàng tiếp theo

#     # Hiển thị bảng xếp hạng lên màn hình
#     screen.blit(ranking_surface, (0, 0))


def draw_ranking_table(screen, current_username):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Thay bằng mật khẩu MySQL của bạn
        database="solar_system_protection",
    )
    cursor = conn.cursor()

    # Vẽ nền mờ cho bảng xếp hạng
    ranking_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    ranking_surface.blit(GAME_HIGHTCORE_SCREEN_BACKGROUND, (0, 0))
    image_x = (SCREEN_WIDTH - HIGHTCORE_IMAGE.get_width()) // 2
    ranking_surface.blit(HIGHTCORE_IMAGE, (image_x, START_IMAGE_Y * 2))
    # Tiêu đề cho các cột
    columns = ["Top", "Username", "Score"]

    font = pygame.font.Font(None, 20)  # Font chữ
    text_color = (255, 255, 255)  # Màu chữ trắng
    # Tính toán vị trí y của tiêu đề
    title_y = 300

    # Tính toán số lượng cột và kích thước của mỗi cột
    num_columns = len(columns)
    column_width = SCREEN_WIDTH // num_columns

    # Tính toán vị trí x của mỗi cột
    column_x_positions = [i * column_width for i in range(num_columns)]

    # Vẽ tiêu đề
    for i, col in enumerate(columns):
        text = font.render(col, True, text_color)
        # Tính toán vị trí x cho từng cột để căn giữa tiêu đề
        x = column_x_positions[i] + (column_width - text.get_width()) // 2
        ranking_surface.blit(text, (x, title_y))  # Đặt vị trí của tiêu đề

    # Lấy dữ liệu từ cơ sở dữ liệu và vẽ lên bảng xếp hạng
    cursor.execute(
        "SELECT username, highest_score FROM users ORDER BY highest_score DESC LIMIT 10"
    )
    top_10_users = cursor.fetchall()

    # Tính điểm của người chơi hiện tại
    cursor.execute(
        "SELECT highest_score FROM users WHERE username = %s", (current_username,)
    )
    current_user_score = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM users WHERE highest_score > %s", (current_user_score,)
    )
    higher_score_count = cursor.fetchone()[0]

    # ranking_data = cursor.fetchall()

    # Tính toán vị trí y của hàng đầu tiên
    data_y = title_y + 20

    # Vẽ dữ liệu lên bảng xếp hạng
    for i, (username, highest_score) in enumerate(top_10_users):
        # Vẽ số thứ tự
        stt_text = font.render(str(i + 1), True, text_color)
        # Tính toán vị trí x cho số thứ tự sao cho nó ở giữa cột "STT"
        stt_x = column_x_positions[0] + (column_width - stt_text.get_width()) // 2
        ranking_surface.blit(stt_text, (stt_x, data_y))  # Đặt vị trí của số thứ tự

        # Tính toán vị trí x cho tên người chơi
        username_text = font.render(username, True, text_color)
        username_x = (
            column_x_positions[1] + (column_width - username_text.get_width()) // 2
        )
        ranking_surface.blit(
            username_text, (username_x, data_y)
        )  # Đặt vị trí của tên người chơi

        # Tính toán vị trí x cho điểm số
        score_text = font.render(str(highest_score), True, text_color)
        score_x = column_x_positions[2] + (column_width - score_text.get_width()) // 2
        ranking_surface.blit(score_text, (score_x, data_y))  # Đặt vị trí của điểm số

        data_y += 20  # Di chuyển xuống hàng tiếp theo

    text_color1 = (255, 0, 0)
    stt_text = font.render(str(higher_score_count + 1), True, text_color1)
    # Tính toán vị trí x cho số thứ tự sao cho nó ở giữa cột "STT"
    stt_x = column_x_positions[0] + (column_width - stt_text.get_width()) // 2
    ranking_surface.blit(stt_text, (stt_x, data_y))  # Đặt vị trí của số thứ tự

    # Tính toán vị trí x cho tên người chơi
    username_text = font.render("Your Score", True, text_color1)
    username_x = column_x_positions[1] + (column_width - username_text.get_width()) // 2
    ranking_surface.blit(
        username_text, (username_x, data_y)
    )  # Đặt vị trí của tên người chơi

    # Tính toán vị trí x cho điểm số
    score_text = font.render(str(current_user_score), True, text_color1)
    score_x = column_x_positions[2] + (column_width - score_text.get_width()) // 2
    ranking_surface.blit(score_text, (score_x, data_y))  # Đặt vị trí của điểm số
    screen.blit(ranking_surface, (0, 0))
