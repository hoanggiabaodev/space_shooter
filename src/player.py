import pygame
from constants.player import *
from constants.bullet_player import *
from constants.screen import GAME_LOOP_SCREEN
from constants.setup import (
    NORMAL_TYPE,
    SPECIAL_TYPE,
    SPREAD_TYPE,
    AROUND_TYPE,
    LASER_TYPE,
)
from constants.setup import (
    NUMBER_0,
    NUMBER_1,
    NUMBER_2,
    NUMBER_3,
    NUMBER_4,
    NUMBER_5,
    NUMBER_6,
    NUMBER_7,
    NUMBER_8,
    NUMBER_9,
)
from constants.item import (
    ITEM_SPECIAL_DURATION,
    ITEM_SPREAD_DURATION,
    ITEM_AROUND_DURATION,
    ITEM_LASER_DURATION,
    ITEM_HEALTH_REGENERATION,
)
from constants.item import (
    ITEM_HEALTH,
    ITEM_SPECIAL,
    ITEM_SPREAD,
    ITEM_AROUND,
    ITEM_LASER,
)
from src.bullet_player import BulletPlayer
from constants.enemy import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = PLAYER_NORMAL_IMAGE
        self.rect = self.image.get_rect()
        self.rect.x = PLAYER_START_X
        self.rect.y = PLAYER_START_Y
        self.speed_x = PLAYER_SPEED_X
        self.speed_y = PLAYER_SPEED_Y
        self.health = PLAYER_HEALTH
        self.damage = PLAYER_NORMAL_DAMAGE
        self.defense = PLAYER_NORMAL_DEFENSE
        self.hit_box_image = PLAYER_NORMAL_HIT_BOX_IMAGE
        self.type = NORMAL_TYPE
        self.skin_1 = None
        self.skin_2 = None
        self.last_shot = pygame.time.get_ticks()
        self.score = 0
        self.explosion_effect = PLAYER_EXPLOSION_EFFECT
        self.explosion_time = None
        self.death_effect = PLAYER_DEATH_EFFECT
        self.death_time = None
        self.transform_start_time = None
        self.transform_duration = None
        self.game_over = False

    def move(self):
        if not self.game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed_x
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed_x
            if keys[pygame.K_UP]:
                self.rect.y -= self.speed_y
            if keys[pygame.K_DOWN]:
                self.rect.y += self.speed_y
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT

    def draw(self, angle):
        if self.type == NORMAL_TYPE:
            self.hit_box_image = PLAYER_NORMAL_HIT_BOX_IMAGE
            self.image = PLAYER_NORMAL_IMAGE
            self.skin_1 = None
            self.skin_2 = None
        elif self.type == SPECIAL_TYPE:
            self.hit_box_image = PLAYER_SPECIAL_HIT_BOX_IMAGE
            self.image = PLAYER_SPECIAL_IMAGE
            self.skin_1 = pygame.transform.rotate(PLAYER_SPECIAL_SKIN_1_IMAGE, angle)
            self.skin_2 = pygame.transform.rotate(PLAYER_SPECIAL_SKIN_2_IMAGE, 0)
        elif self.type == SPREAD_TYPE:
            self.hit_box_image = PLAYER_SPREAD_HIT_BOX_IMAGE
            self.image = PLAYER_SPREAD_IMAGE
            self.skin_1 = pygame.transform.rotate(PLAYER_SPREAD_SKIN_1_IMAGE, angle)
            self.skin_2 = pygame.transform.rotate(PLAYER_SPREAD_SKIN_2_IMAGE, -angle)
        elif self.type == AROUND_TYPE:
            self.hit_box_image = PLAYER_AROUND_HIT_BOX_IMAGE
            self.image = PLAYER_AROUND_IMAGE
            self.skin_1 = pygame.transform.rotate(PLAYER_AROUND_SKIN_1_IMAGE, 0)
            self.skin_2 = pygame.transform.rotate(PLAYER_AROUND_SKIN_2_IMAGE, angle)
        elif self.type == LASER_TYPE:
            self.hit_box_image = PLAYER_LASER_HIT_BOX_IMAGE
            self.image = PLAYER_LASER_IMAGE
            self.skin_1 = pygame.transform.rotate(PLAYER_LASER_SKIN_1_IMAGE, angle)
            self.skin_2 = pygame.transform.rotate(PLAYER_LASER_SKIN_2_IMAGE, 0)

        hit_box_x = self.rect.centerx - PLAYER_HIT_BOX_WIDTH // 2
        hit_box_y = self.rect.centery - PLAYER_HIT_BOX_HEIGHT // 2
        if self.skin_1 is not None and self.skin_2 is not None:
            skin_1_x = self.rect.centerx - self.skin_1.get_rect().centerx
            skin_1_y = self.rect.centery - self.skin_1.get_rect().centery
            skin_2_x = self.rect.centerx - self.skin_2.get_rect().centerx
            skin_2_y = self.rect.centery - self.skin_2.get_rect().centery
            GAME_LOOP_SCREEN.blit(self.skin_1, (skin_1_x, skin_1_y))
            GAME_LOOP_SCREEN.blit(self.skin_2, (skin_2_x, skin_2_y))

        GAME_LOOP_SCREEN.blit(self.image, (self.rect.x, self.rect.y))
        GAME_LOOP_SCREEN.blit(self.hit_box_image, (hit_box_x, hit_box_y))

    def draw_health_bar(self):
        GAME_LOOP_SCREEN.blit(PLAYER_HEALTH_BAR_EMPTY, PLAYER_HEALTH_BAR_EMPTY_POSITION)
        health_bar_full_width = (
            self.health / PLAYER_HEALTH * PLAYER_HEALTH_BAR_FULL_WIDTH
        )
        health_bar_full_rect = pygame.Rect(
            0, 0, health_bar_full_width, PLAYER_HEALTH_BAR_FULL_HEIGHT
        )
        GAME_LOOP_SCREEN.blit(
            PLAYER_HEALTH_BAR_FULL,
            PLAYER_HEALTH_BAR_FULL_POSITION,
            health_bar_full_rect,
        )

    def draw_number(self, number, x, y, space):
        number_images = [
            NUMBER_0,
            NUMBER_1,
            NUMBER_2,
            NUMBER_3,
            NUMBER_4,
            NUMBER_5,
            NUMBER_6,
            NUMBER_7,
            NUMBER_8,
            NUMBER_9,
        ]
        number_str = str(number)
        for i, digit in enumerate(number_str):
            if digit.isdigit():
                digit_image = number_images[int(digit)]
                digit_x = x + i * (digit_image.get_width() + space)
                GAME_LOOP_SCREEN.blit(digit_image, (digit_x, y))

    def draw_info(self):
        GAME_LOOP_SCREEN.blit(PLAYER_HEALTH_ICON, PLAYER_HEALTH_ICON_POSITION)
        GAME_LOOP_SCREEN.blit(PLAYER_DEFENSE_ICON, PLAYER_DEFENSE_ICON_POSITION)
        GAME_LOOP_SCREEN.blit(PLAYER_DAMAGE_ICON, PLAYER_DAMAGE_ICON_POSITION)
        GAME_LOOP_SCREEN.blit(PLAYER_KILL_ICON, PLAYER_KILL_ICON_POSITION)
        GAME_LOOP_SCREEN.blit(GAME_PAUSE_BUTTON, GAME_PAUSE_BUTTON_POSITION)
        self.draw_number(self.health, 45, 30, 0)
        self.draw_number(self.defense, SCREEN_WIDTH - 90, 15, 0)
        self.draw_number(self.damage, SCREEN_WIDTH - 90, 50, 0)
        self.draw_number(self.score, SCREEN_WIDTH - 90, 85, 0)

    def shoot(self):
        now = pygame.time.get_ticks()
        if self.type == NORMAL_TYPE:
            self.damage = PLAYER_NORMAL_DAMAGE
            self.defense = PLAYER_NORMAL_DEFENSE
            if now - self.last_shot >= PLAYER_BULLET_NORMAL_DELAY:
                self.last_shot = now
                BulletPlayer.generate_bullets_player(
                    PLAYER_BULLET_NORMAL_IMAGE,
                    self.rect.x
                    + PLAYER_NORMAL_WIDTH // 2
                    - PLAYER_BULLET_NORMAL_WIDTH // 2,
                    self.rect.y - PLAYER_BULLET_NORMAL_HEIGHT // 2,
                    PLAYER_BULLET_NORMAL_SPEED,
                    PLAYER_BULLET_NORMAL_COUNT,
                    PLAYER_BULLET_NORMAL_START_ANGLE,
                    PLAYER_BULLET_NORMAL_END_ANGLE,
                    NORMAL_TYPE,
                )
                PLAYER_BULLET_NORMAL_SOUND.play()
        elif self.type == SPECIAL_TYPE:
            self.damage = PLAYER_SPECIAL_DAMAGE
            self.defense = PLAYER_SPECIAL_DEFENSE
            if now - self.last_shot >= PLAYER_BULLET_SPECIAL_DELAY:
                self.last_shot = now
                BulletPlayer.generate_bullets_player(
                    PLAYER_BULLET_SPECIAL_IMAGE,
                    self.rect.x
                    + PLAYER_SPECIAL_WIDTH // 2
                    - PLAYER_BULLET_SPECIAL_WIDTH // 2,
                    self.rect.y - PLAYER_BULLET_SPECIAL_HEIGHT // 2,
                    PLAYER_BULLET_SPECIAL_SPEED,
                    PLAYER_BULLET_SPECIAL_COUNT,
                    PLAYER_BULLET_SPECIAL_START_ANGLE,
                    PLAYER_BULLET_SPECIAL_END_ANGLE,
                    SPECIAL_TYPE,
                )
                PLAYER_BULLET_SPECIAL_SOUND.play()
        elif self.type == SPREAD_TYPE:
            self.damage = PLAYER_SPREAD_DAMAGE
            self.defense = PLAYER_SPREAD_DEFENSE
            if now - self.last_shot >= PLAYER_BULLET_SPREAD_DELAY:
                self.last_shot = now
                BulletPlayer.generate_bullets_player(
                    PLAYER_BULLET_SPREAD_IMAGE,
                    self.rect.x
                    + PLAYER_SPREAD_WIDTH // 2
                    - PLAYER_BULLET_SPREAD_WIDTH // 2,
                    self.rect.y - PLAYER_BULLET_SPREAD_HEIGHT // 2 - 30,
                    PLAYER_BULLET_SPREAD_SPEED,
                    PLAYER_BULLET_SPREAD_COUNT,
                    PLAYER_BULLET_SPREAD_START_ANGLE,
                    PLAYER_BULLET_SPREAD_END_ANGLE,
                    SPREAD_TYPE,
                )
                PLAYER_BULLET_SPREAD_SOUND.play()
        elif self.type == AROUND_TYPE:
            self.damage = PLAYER_AROUND_DAMAGE
            self.defense = PLAYER_AROUND_DEFENSE
            if now - self.last_shot >= PLAYER_BULLET_AROUND_DELAY:
                self.last_shot = now
                BulletPlayer.generate_bullets_player(
                    PLAYER_BULLET_AROUND_IMAGE,
                    self.rect.x
                    + PLAYER_AROUND_WIDTH // 2
                    - PLAYER_BULLET_AROUND_WIDTH // 2,
                    self.rect.y
                    + PLAYER_AROUND_HEIGHT // 2
                    - PLAYER_BULLET_AROUND_HEIGHT // 2,
                    PLAYER_BULLET_AROUND_SPEED,
                    PLAYER_BULLET_AROUND_COUNT,
                    PLAYER_BULLET_AROUND_START_ANGLE,
                    PLAYER_BULLET_AROUND_END_ANGLE,
                    AROUND_TYPE,
                )
                PLAYER_BULLET_AROUND_SOUND.play()
        elif self.type == LASER_TYPE:
            self.damage = PLAYER_LASER_DAMAGE
            self.defense = PLAYER_LASER_DEFENSE
            if now - self.last_shot >= PLAYER_BULLET_LASER_DELAY:
                self.last_shot = now
                BulletPlayer.generate_bullets_player(
                    PLAYER_BULLET_LASER_IMAGE,
                    self.rect.x
                    + PLAYER_LASER_WIDTH // 2
                    - PLAYER_BULLET_LASER_WIDTH // 2,
                    self.rect.y - 20,
                    PLAYER_BULLET_LASER_SPEED,
                    PLAYER_BULLET_LASER_COUNT,
                    PLAYER_BULLET_LASER_START_ANGLE,
                    PLAYER_BULLET_LASER_END_ANGLE,
                    LASER_TYPE,
                )
                PLAYER_BULLET_LASER_SOUND.play()

    def player_hit(self, bullet):
        hit_box_x = self.rect.centerx - PLAYER_HIT_BOX_WIDTH // 2
        hit_box_y = self.rect.centery - PLAYER_HIT_BOX_HEIGHT // 2
        if (
            bullet.x + bullet.rect.width >= hit_box_x
            and bullet.x <= hit_box_x + PLAYER_HIT_BOX_WIDTH
        ) and (
            bullet.y + bullet.rect.height >= hit_box_y
            and bullet.y <= hit_box_y + PLAYER_HIT_BOX_HEIGHT
        ):
            bullet.kill()
            self.explosion_time = pygame.time.get_ticks()
            actual_damage = bullet.damage - self.defense
            if actual_damage > 0:
                if self.health > 0:
                    self.health -= actual_damage
                    if self.health <= 0:
                        self.health = 0
                        self.death_time = pygame.time.get_ticks()
                        self.game_over = True

        if self.explosion_time is not None:
            current_time = pygame.time.get_ticks()
            if current_time - self.explosion_time < PLAYER_EXPLOSION_EFFECT_TIME:
                self.explosion_effect.render(
                    GAME_LOOP_SCREEN,
                    (
                        self.rect.centerx - self.rect.width // 2,
                        self.rect.centery - self.rect.height,
                    ),
                )
            else:
                self.explosion_time = None

        if self.death_time is not None:
            current_time = pygame.time.get_ticks()
            if current_time - self.death_time < PLAYER_DEATH_EFFECT_TIME:
                PLAYER_DEATH_SOUND.play()
                self.death_effect.render(
                    GAME_LOOP_SCREEN, (self.rect.centerx - 100, self.rect.centery - 100)
                )
            else:
                self.death_time = None
                PLAYER_LIST.empty()

    def player_collide(self, enemy):
        hit_box_x = self.rect.centerx - PLAYER_HIT_BOX_WIDTH // 2
        hit_box_y = self.rect.centery - PLAYER_HIT_BOX_HEIGHT // 2
        if (
            # enemy.x + enemy.rect.width >= hit_box_x
            # and enemy.x <= hit_box_x + PLAYER_HIT_BOX_WIDTH
            enemy.rect.right >= hit_box_x
            and enemy.rect.left <= hit_box_x + PLAYER_HIT_BOX_WIDTH
        ) and (
            # enemy.y + enemy.rect.height >= hit_box_y
            # and enemy.y <= hit_box_y + PLAYER_HIT_BOX_HEIGHT
            enemy.rect.bottom >= hit_box_y
            and enemy.rect.top <= hit_box_y + PLAYER_HIT_BOX_HEIGHT
        ):
            enemy.kill()
            self.explosion_time = pygame.time.get_ticks()
            actual_damage = enemy.damage - self.defense
            if actual_damage > 0:
                if self.health > 0:
                    self.health -= actual_damage
                    if self.health <= 0:
                        self.death_time = pygame.time.get_ticks()
                        self.game_over = True

        if self.explosion_time is not None:
            current_time = pygame.time.get_ticks()
            if current_time - self.explosion_time < PLAYER_EXPLOSION_EFFECT_TIME:
                self.explosion_effect.render(
                    GAME_LOOP_SCREEN,
                    (
                        self.rect.centerx - self.rect.width // 2,
                        self.rect.centery - self.rect.height,
                    ),
                )
            else:
                self.explosion_time = None

        if self.death_time is not None:
            current_time = pygame.time.get_ticks()
            if current_time - self.death_time < PLAYER_DEATH_EFFECT_TIME:
                PLAYER_DEATH_SOUND.play()
                self.death_effect.render(
                    GAME_LOOP_SCREEN, (self.rect.centerx - 100, self.rect.centery - 100)
                )
            else:
                self.death_time = None
                PLAYER_LIST.empty()

    def get_item(self, item):
        if (
            self.rect.x + self.rect.width >= item.rect.x
            and self.rect.x <= item.rect.x + item.rect.width
        ) and (
            self.rect.y + self.rect.height >= item.rect.y
            and self.rect.y <= item.rect.y + item.rect.height
        ):
            item.kill()
            if item.type == ITEM_HEALTH:
                if self.health < PLAYER_HEALTH:
                    self.health += ITEM_HEALTH_REGENERATION
                if self.health >= PLAYER_HEALTH:
                    self.health = PLAYER_HEALTH
            elif item.type == ITEM_SPECIAL:
                self.type = SPECIAL_TYPE
                self.transform_duration = ITEM_SPECIAL_DURATION
            elif item.type == ITEM_SPREAD:
                self.type = SPREAD_TYPE
                self.transform_duration = ITEM_SPREAD_DURATION
            elif item.type == ITEM_AROUND:
                self.type = AROUND_TYPE
                self.transform_duration = ITEM_AROUND_DURATION
            elif item.type == ITEM_LASER:
                self.type = LASER_TYPE
                self.transform_duration = ITEM_LASER_DURATION
            self.transform_start_time = pygame.time.get_ticks()

    def update(self, angle):
        if len(PLAYER_LIST) > 0:
            self.shoot()
            self.draw(angle)
            self.draw_health_bar()
            self.draw_info()
            self.move()
            if (
                self.transform_start_time is not None
                and self.transform_duration is not None
            ):
                current_time = pygame.time.get_ticks()
                elapsed_time = current_time - self.transform_start_time
                if elapsed_time >= self.transform_duration:
                    self.type = NORMAL_TYPE
                    self.transform_start_time = None
