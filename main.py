from constants.setup import *
from constants.screen import SCREEN_HEIGHT, GAME_LOOP_SCREEN, GAME_LOOP_SCREEN_BACKGROUND, GAME_LOOP_SCREEN_BACKGROUND_SPEED, GAME_LOOP_SCREEN_BACKGROUND_MUSIC
from constants.screen import GAME_START_SCREEN, GAME_START_SCREEN_BACKGROUND
from constants.screen import GAME_STOP_SCREEN, GAME_STOP_SCREEN_BACKGROUND
from constants.screen import BUTTON_WIDTH, BUTTON_HEIGHT
from constants.screen import GAME_PLAY_BUTTON, GAME_PLAY_BUTTON_X, GAME_PLAY_BUTTON_Y
from constants.screen import GAME_REPLAY_BUTTON, GAME_REPLAY_BUTTON_X, GAME_REPLAY_BUTTON_Y
from constants.screen import GAME_REPLAY_BUTTON, GAME_REPLAY_BUTTON_X, GAME_REPLAY_BUTTON_Y
from constants.screen import GAME_EXIT_BUTTON, GAME_EXIT_BUTTON_X, GAME_EXIT_BUTTON_Y
from constants.screen import START_IMAGE, START_IMAGE_X, START_IMAGE_Y
from constants.screen import STOP_IMAGE, STOP_IMAGE_X, STOP_IMAGE_Y
from constants.bullet_player import PLAYER_BULLET_LIST
from constants.bullet_enemy import ENEMY_LEVEL_1_BULLET_LIST, ENEMY_LEVEL_2_BULLET_LIST, ENEMY_LEVEL_3_BULLET_LIST, ENEMY_LEVEL_4_BULLET_LIST, ENEMY_LEVEL_5_BULLET_LIST
from constants.enemy import ENEMY_LIST, ENEMY_GENETATE_DELAY
from constants.player import PLAYER_LIST
from constants.item import ITEM_LIST
from src.player import Player
from src.enemy import Enemy

# ================================ Game Start Loop ================================
def game_start_loop():
    while True:
        GAME_START_SCREEN.blit(GAME_START_SCREEN_BACKGROUND, (0,0))
        GAME_START_SCREEN.blit(START_IMAGE, (START_IMAGE_X, START_IMAGE_Y))
        GAME_START_SCREEN.blit(GAME_PLAY_BUTTON, (GAME_PLAY_BUTTON_X,  GAME_PLAY_BUTTON_Y))
        GAME_START_SCREEN.blit(GAME_EXIT_BUTTON, (GAME_EXIT_BUTTON_X, GAME_EXIT_BUTTON_Y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pygame.Rect(GAME_PLAY_BUTTON_X, GAME_PLAY_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT).collidepoint(pos):
                    game_loop()
                elif pygame.Rect(GAME_EXIT_BUTTON_X, GAME_EXIT_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT).collidepoint(pos):
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loop()
        pygame.display.update()

       
# ================================ Game Stop Loop ================================
def game_stop_loop():
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
        GAME_STOP_SCREEN.blit(GAME_STOP_SCREEN_BACKGROUND, (0,0))
        GAME_STOP_SCREEN.blit(STOP_IMAGE, (STOP_IMAGE_X, STOP_IMAGE_Y))
        GAME_STOP_SCREEN.blit(GAME_REPLAY_BUTTON, (GAME_REPLAY_BUTTON_X,  GAME_REPLAY_BUTTON_Y))
        GAME_STOP_SCREEN.blit(GAME_EXIT_BUTTON, (GAME_EXIT_BUTTON_X, GAME_EXIT_BUTTON_Y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pygame.Rect(GAME_REPLAY_BUTTON_X, GAME_REPLAY_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT).collidepoint(pos):
                    game_loop()
                elif pygame.Rect(GAME_EXIT_BUTTON_X, GAME_EXIT_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT).collidepoint(pos):
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loop()
                    
        pygame.display.update()
        

# ================================ Game Loop ================================
def game_loop():
    player = Player()
    PLAYER_LIST.add(player)
    game_over = False
    SKIN_ANGLE = 0
    enemy_spawn_time = 0.0 
    GAME_LOOP_SCREEN_BACKGROUND_MUSIC.play(-1)
    GAME_LOOP_SCREEN_BACKGROUND_Y = 0
    enemy_bullet_list = [ENEMY_LEVEL_1_BULLET_LIST, ENEMY_LEVEL_2_BULLET_LIST, ENEMY_LEVEL_3_BULLET_LIST, ENEMY_LEVEL_4_BULLET_LIST, ENEMY_LEVEL_5_BULLET_LIST]
    while not game_over:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                sys.exit()
        
        # ====================================== SCREEN ====================================== 
        GAME_LOOP_SCREEN_BACKGROUND_Y += GAME_LOOP_SCREEN_BACKGROUND_SPEED
        if GAME_LOOP_SCREEN_BACKGROUND_Y >= 0:
            GAME_LOOP_SCREEN_BACKGROUND_Y = -SCREEN_HEIGHT
        GAME_LOOP_SCREEN.blit(GAME_LOOP_SCREEN_BACKGROUND, (0, GAME_LOOP_SCREEN_BACKGROUND_Y))
        GAME_LOOP_SCREEN.blit(GAME_LOOP_SCREEN_BACKGROUND, (0, GAME_LOOP_SCREEN_BACKGROUND_Y + SCREEN_HEIGHT))   
                    
        # ====================================== ENEMY ====================================== #
        enemy_spawn_time += 1/FPS
        
        if enemy_spawn_time >= ENEMY_GENETATE_DELAY:
            Enemy.generate_enemies() 
            enemy_spawn_time = 0.0  
            
        for enemy in ENEMY_LIST:
            enemy.update()
            
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
        game_stop_loop()
        
if __name__ == "__main__":
    game_start_loop()