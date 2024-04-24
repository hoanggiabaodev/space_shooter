import pygame, random
from constants.item import *
from constants.screen import GAME_LOOP_SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT


class Item(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = ITEM_HEALTH_IMAGE
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = ITEM_SPEED_X
        self.speed_y = ITEM_SPEED_Y
        self.type = ITEM_HEALTH

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

    def update(self):
        self.draw()
        self.move()

    @staticmethod
    def generate_items(x, y):
        type = random.choices(
            [
                ITEM_HEALTH,
                ITEM_SPECIAL,
                ITEM_SPREAD,
                ITEM_AROUND,
                ITEM_LASER,
                ITEM_UPDATE,
            ],
            weights=[
                ITEM_HEALTH_FREQUENCY_RATE,
                ITEM_SPECIAL_FREQUENCY_RATE,
                ITEM_SPREAD_FREQUENCY_RATE,
                ITEM_AROUND_FREQUENCY_RATE,
                ITEM_LASER_FREQUENCY_RATE,
                ITEM_UPDATE_FREQUENCY_RATE,
            ],
        )[0]
        item = Item(x, y)
        if type == ITEM_HEALTH:
            item.type = ITEM_HEALTH
            item.image = ITEM_HEALTH_IMAGE
        elif type == ITEM_SPECIAL:
            item.type = ITEM_SPECIAL
            item.image = ITEM_SPECIAL_IMAGE
        elif type == ITEM_SPREAD:
            item.type = ITEM_SPREAD
            item.image = ITEM_SPREAD_IMAGE
        elif type == ITEM_AROUND:
            item.type = ITEM_AROUND
            item.image = ITEM_AROUND_IMAGE
        elif type == ITEM_LASER:
            item.type = ITEM_LASER
            item.image = ITEM_LASER_IMAGE
        elif type == ITEM_UPDATE:
            item.type = ITEM_UPDATE
            item.image = ITEM_UPDATE_IMAGE
        ITEM_LIST.add(item)
