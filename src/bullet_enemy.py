import pygame, math
from constants.screen import GAME_LOOP_SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT
from constants.bullet_enemy import ENEMY_LEVEL_1_BULLET_LIST, ENEMY_LEVEL_2_BULLET_LIST, ENEMY_LEVEL_3_BULLET_LIST, ENEMY_LEVEL_4_BULLET_LIST, ENEMY_LEVEL_5_BULLET_LIST
from constants.enemy import LEVEL_1, LEVEL_2, LEVEL_3, LEVEL_4, LEVEL_5

class BulletEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y, image, vx, vy, level, damage):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.level = level
        self.damage = damage
                    
    def move(self):
        self.x += self.vx
        self.y += self.vy
            
    def draw(self):
        GAME_LOOP_SCREEN.blit(self.image, (self.x, self.y))
        
    def remove(self):
        if self.x < 0 or self.x > SCREEN_WIDTH or self.y < 0 or self.y > SCREEN_HEIGHT:
            self.kill()
    
    def update(self):
        self.move()
        self.draw()
        self.remove()
        
    @staticmethod
    def generate_bullets_enemy(bullet_image, bullet_x, bullet_y, bullet_speed, bullet_numbers, start_angle, end_angle, bullet_level, bullet_damage):
        if bullet_numbers == 1:
            angle_step = 0
        else:
            angle_step = (end_angle - start_angle) / (bullet_numbers - 1)
        for i in range(bullet_numbers):
            if bullet_numbers == 1:
                angle = math.radians(0)
            else:
                angle = math.radians(start_angle + i * angle_step) 
            if angle > math.radians(end_angle):
                angle = math.radians(end_angle)
            elif angle < math.radians(start_angle):
                angle = math.radians(start_angle)
            bullet_vx = bullet_speed * math.sin(angle) 
            bullet_vy = bullet_speed * math.cos(angle) 
            bullet = BulletEnemy(bullet_x, bullet_y, bullet_image, bullet_vx, bullet_vy, bullet_level, bullet_damage)
            if bullet_level == LEVEL_1:
                ENEMY_LEVEL_1_BULLET_LIST.add(bullet)
            elif bullet_level == LEVEL_2:
                ENEMY_LEVEL_2_BULLET_LIST.add(bullet)
            elif bullet_level == LEVEL_3:
                ENEMY_LEVEL_3_BULLET_LIST.add(bullet)
            elif bullet_level == LEVEL_4:
                ENEMY_LEVEL_4_BULLET_LIST.add(bullet)
            elif bullet_level == LEVEL_5:
                ENEMY_LEVEL_5_BULLET_LIST.add(bullet)