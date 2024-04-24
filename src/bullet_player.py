import math
from constants.screen import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_LOOP_SCREEN
from constants.setup import LASER_TYPE
from constants.player import PLAYER_LASER_WIDTH
from constants.bullet_player import *


class BulletPlayer(pygame.sprite.Sprite):
    def __init__(self, x, y, image, vx, vy, type):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.type = type

    def draw(self):
        GAME_LOOP_SCREEN.blit(self.image, (self.x, self.y))

    def move(self, player):
        if self.type == LASER_TYPE:
            self.x = (
                player.rect.x + PLAYER_LASER_WIDTH // 2 - PLAYER_BULLET_LASER_WIDTH // 2
            )
            self.y += self.vy
        else:
            self.x += self.vx
            self.y += self.vy

    def remove(self):
        if self.x < 0 or self.x > SCREEN_WIDTH or self.y < 0 or self.y > SCREEN_HEIGHT:
            self.kill()

    def update(self, player):
        self.move(player)
        self.draw()
        self.remove()

    @staticmethod
    def generate_bullets_player(
        bullet_image,
        bullet_x,
        bullet_y,
        bullet_speed,
        bullet_numbers,
        start_angle,
        end_angle,
        bullet_type,
    ):
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
            bullet_vy = -bullet_speed * math.cos(angle)
            bullet = BulletPlayer(
                bullet_x, bullet_y, bullet_image, bullet_vx, bullet_vy, bullet_type
            )
            PLAYER_BULLET_LIST.add(bullet)
