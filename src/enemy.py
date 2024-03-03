import pygame, random
from constants.enemy import *
from constants.bullet_enemy import *
from constants.screen import GAME_LOOP_SCREEN
from constants.setup import LASER_TYPE
from constants.item import ITEM_FREQUENCY_RATE
from src.bullet_enemy import BulletEnemy
from src.item import Item

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ENEMY_LEVEL_1_IMAGE
        self.rect = self.image.get_rect()
        self.rect.x = ENEMY_START_X
        self.rect.y = ENEMY_START_Y
        self.speed_x = 0
        self.speed_y = 0
        self.health = 0
        self.damage = 0
        self.defense = 0
        self.level = LEVEL_1
        self.last_shot = pygame.time.get_ticks()
        self.explosion_effect = ENEMY_LEVEL_1_EXPLOSION_EFFECT
        self.explosion_time = 0
        
    def draw(self):
        GAME_LOOP_SCREEN.blit(self.image, (self.rect.x, self.rect.y))
    
    def move(self):
        self.rect.x += self.speed_x 
        self.rect.y += self.speed_y 
        if self.rect.right > SCREEN_WIDTH or self.rect.left < 0:
            self.speed_x = -self.speed_x
            self.rect.y += self.rect.height
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()  
            
    def shoot(self):
        now = pygame.time.get_ticks()
        if self.level == LEVEL_1:
            if now - self.last_shot >= ENEMY_LEVEL_1_BULLET_DELAY:
                self.last_shot = now
                BulletEnemy.generate_bullets_enemy(
                    ENEMY_LEVEL_1_BULLET_IMAGE, 
                    self.rect.x + ENEMY_LEVEL_1_WIDTH // 2 - ENEMY_LEVEL_1_BULLET_WIDTH // 2, 
                    self.rect.y + ENEMY_LEVEL_1_HEIGHT // 2 + ENEMY_LEVEL_1_BULLET_HEIGHT // 2, 
                    ENEMY_LEVEL_1_BULLET_SPEED, 
                    ENEMY_LEVEL_1_BULLET_COUNT, 
                    ENEMY_LEVEL_1_BULLET_START_ANGLE, 
                    ENEMY_LEVEL_1_BULLET_END_ANGLE, 
                    LEVEL_1,
                    ENEMY_LEVEL_1_DAMAGE
                )
        
        elif self.level == LEVEL_2:
            if now - self.last_shot >= ENEMY_LEVEL_2_BULLET_DELAY:
                self.last_shot = now
                BulletEnemy.generate_bullets_enemy(
                    ENEMY_LEVEL_2_BULLET_IMAGE, 
                    self.rect.x + ENEMY_LEVEL_2_WIDTH // 2 - ENEMY_LEVEL_2_BULLET_WIDTH // 2, 
                    self.rect.y + ENEMY_LEVEL_2_HEIGHT // 2 + ENEMY_LEVEL_2_BULLET_HEIGHT // 2, 
                    ENEMY_LEVEL_2_BULLET_SPEED, 
                    ENEMY_LEVEL_2_BULLET_COUNT, 
                    ENEMY_LEVEL_2_BULLET_START_ANGLE, 
                    ENEMY_LEVEL_2_BULLET_END_ANGLE, 
                    LEVEL_2,
                    ENEMY_LEVEL_2_DAMAGE
                )
        elif self.level == LEVEL_3:
            if now - self.last_shot >= ENEMY_LEVEL_3_BULLET_DELAY:
                self.last_shot = now
                BulletEnemy.generate_bullets_enemy(
                    ENEMY_LEVEL_3_BULLET_IMAGE, 
                    self.rect.x + ENEMY_LEVEL_3_WIDTH // 2 - ENEMY_LEVEL_3_BULLET_WIDTH // 2, 
                    self.rect.y + ENEMY_LEVEL_3_HEIGHT // 2 + ENEMY_LEVEL_3_BULLET_HEIGHT // 2, 
                    ENEMY_LEVEL_3_BULLET_SPEED, 
                    ENEMY_LEVEL_3_BULLET_COUNT, 
                    ENEMY_LEVEL_3_BULLET_START_ANGLE, 
                    ENEMY_LEVEL_3_BULLET_END_ANGLE, 
                    LEVEL_3,
                    ENEMY_LEVEL_3_DAMAGE
                )
        elif self.level == LEVEL_4:
            if now - self.last_shot >= ENEMY_LEVEL_4_BULLET_DELAY:
                self.last_shot = now
                BulletEnemy.generate_bullets_enemy(
                    ENEMY_LEVEL_4_BULLET_IMAGE, 
                    self.rect.x + ENEMY_LEVEL_4_WIDTH // 2 - ENEMY_LEVEL_4_BULLET_WIDTH // 2, 
                    self.rect.y + ENEMY_LEVEL_4_HEIGHT // 2 + ENEMY_LEVEL_4_BULLET_HEIGHT // 2, 
                    ENEMY_LEVEL_4_BULLET_SPEED, 
                    ENEMY_LEVEL_4_BULLET_COUNT, 
                    ENEMY_LEVEL_4_BULLET_START_ANGLE, 
                    ENEMY_LEVEL_4_BULLET_END_ANGLE, 
                    LEVEL_4,
                    ENEMY_LEVEL_4_DAMAGE
                )
        elif self.level == LEVEL_5:
            if now - self.last_shot >= ENEMY_LEVEL_5_BULLET_DELAY:
                self.last_shot = now
                BulletEnemy.generate_bullets_enemy(
                    ENEMY_LEVEL_5_BULLET_IMAGE, 
                    self.rect.x + ENEMY_LEVEL_5_WIDTH // 2 - ENEMY_LEVEL_5_BULLET_WIDTH // 2, 
                    self.rect.y + ENEMY_LEVEL_5_HEIGHT // 2 + ENEMY_LEVEL_5_BULLET_HEIGHT // 2, 
                    ENEMY_LEVEL_5_BULLET_SPEED, 
                    ENEMY_LEVEL_5_BULLET_COUNT, 
                    ENEMY_LEVEL_5_BULLET_START_ANGLE, 
                    ENEMY_LEVEL_5_BULLET_END_ANGLE, 
                    LEVEL_5,
                    ENEMY_LEVEL_5_DAMAGE
                )
        
    def update(self):
        self.shoot()
        self.draw()
        self.move()
    
    def enemy_hit(self, bullet, player):
        if (bullet.x + bullet.rect.width >= self.rect.x and bullet.x <= self.rect.x + self.rect.width) and (bullet.y + bullet.rect.height >= self.rect.y and bullet.y <= self.rect.y + self.rect.height):
            if (player.type != LASER_TYPE ):
                bullet.kill()
            self.explosion_time = pygame.time.get_ticks()
            actual_damage = player.damage - self.defense
            if actual_damage > 0:
                if self.health > 0:
                    self.health -= actual_damage
                    if self.health <= 0:
                        if random.random() < ITEM_FREQUENCY_RATE:
                            Item.generate_items(self.rect.x, self.rect.y)
                        self.kill()
                        player.score += 1

        if self.explosion_time > 0:
            current_time = pygame.time.get_ticks()
            if current_time - self.explosion_time < 100:
                self.explosion_effect.render(GAME_LOOP_SCREEN, (self.rect.centerx - 20, self.rect.centery))
            else:
                self.explosion_time = 0 
                    
        
    @staticmethod
    def generate_enemies():
        level = random.choices(
            [LEVEL_1, LEVEL_2, LEVEL_3, LEVEL_4, LEVEL_5],
            weights = [
                ENEMY_LEVEL_1_FREQUENCY_RATE, 
                ENEMY_LEVEL_2_FREQUENCY_RATE, 
                ENEMY_LEVEL_3_FREQUENCY_RATE, 
                ENEMY_LEVEL_4_FREQUENCY_RATE, 
                ENEMY_LEVEL_5_FREQUENCY_RATE
            ]
        )[0]
        
        enemy = Enemy()
        if level == LEVEL_1:
            enemy.level = LEVEL_1
            enemy.image = ENEMY_LEVEL_1_IMAGE
            enemy.speed_x = ENEMY_LEVEL_1_SPEED_X
            enemy.speed_y = ENEMY_LEVEL_1_SPEED_Y
            enemy.health = ENEMY_LEVEL_1_HEALTH
            enemy.damage = ENEMY_LEVEL_1_DAMAGE
            enemy.defense = ENEMY_LEVEL_1_DEFENSE
            enemy.explosion_effect = ENEMY_LEVEL_1_EXPLOSION_EFFECT
        elif level == LEVEL_2:
            enemy.level = LEVEL_2
            enemy.image = ENEMY_LEVEL_2_IMAGE
            enemy.speed_x = ENEMY_LEVEL_2_SPEED_X
            enemy.speed_y = ENEMY_LEVEL_2_SPEED_Y
            enemy.health = ENEMY_LEVEL_2_HEALTH
            enemy.damage = ENEMY_LEVEL_2_DAMAGE
            enemy.defense = ENEMY_LEVEL_2_DEFENSE
            enemy.explosion_effect = ENEMY_LEVEL_2_EXPLOSION_EFFECT
        elif level == LEVEL_3:
            enemy.level = LEVEL_3
            enemy.image = ENEMY_LEVEL_3_IMAGE
            enemy.speed_x = ENEMY_LEVEL_3_SPEED_X
            enemy.speed_y = ENEMY_LEVEL_3_SPEED_Y
            enemy.health = ENEMY_LEVEL_3_HEALTH
            enemy.damage = ENEMY_LEVEL_3_DAMAGE
            enemy.defense = ENEMY_LEVEL_3_DEFENSE
            enemy.explosion_effect = ENEMY_LEVEL_3_EXPLOSION_EFFECT
        elif level == LEVEL_4:
            enemy.level = LEVEL_4
            enemy.image = ENEMY_LEVEL_4_IMAGE
            enemy.speed_x = ENEMY_LEVEL_4_SPEED_X
            enemy.speed_y = ENEMY_LEVEL_4_SPEED_Y
            enemy.health = ENEMY_LEVEL_4_HEALTH
            enemy.damage = ENEMY_LEVEL_4_DAMAGE
            enemy.defense = ENEMY_LEVEL_4_DEFENSE  
            enemy.explosion_effect = ENEMY_LEVEL_4_EXPLOSION_EFFECT
        elif level == LEVEL_5:
            enemy.level = LEVEL_5
            enemy.image = ENEMY_LEVEL_5_IMAGE
            enemy.speed_x = ENEMY_LEVEL_5_SPEED_X
            enemy.speed_y = ENEMY_LEVEL_5_SPEED_Y
            enemy.health = ENEMY_LEVEL_5_HEALTH
            enemy.damage = ENEMY_LEVEL_5_DAMAGE
            enemy.defense = ENEMY_LEVEL_5_DEFENSE
            enemy.explosion_effect = ENEMY_LEVEL_5_EXPLOSION_EFFECT
        enemy.rect = enemy.image.get_rect()
        ENEMY_LIST.add(enemy)
