import pygame as pg
import os
from typing import TypeVar, Any, Dict, Tuple
from settings import *
from collections import deque


Game = TypeVar("Game")
Player = TypeVar("Player")


class Sprite:

    def __init__(self, game: Game, path='resources/sprites/animated_sprites/green_light/0.png',
                 pos=(10.5, 3.5), scale=0.8, shift=0.16) -> None:
        self.__game = game
        self.scale = scale
        self.shift = shift
        self.__path = path
        self.__pos = pos
        self.__player = game.player
        self.x, self.y = self.__pos
        self.__image = pg.image.load(self.__path).convert_alpha()
        self.IMAGE_WIDTH = self.__image.get_width()
        self.IMAGE_HALF_WIDTH = self.__image.get_width() // 2
        self.IMAGE_WIDTH = self.__image.get_width()
        self.IMAGE_HALF_WIDTH = self.__image.get_width() // 2
        self.IMAGE_RATIO = self.IMAGE_WIDTH / self.__image.get_height()
        self.dx = 0
        self.dy = 0
        self.theta = 0
        self.screen_x = 0
        self.dist = 1
        self.norm_dist = 1
        self.sprite_half_width = 0
        self.SPRITE_HEIGHT_SHIFT = self.shift
        self.SPRITE_SCALE = self.scale

    @property
    def player(self) -> Player:
        return self.__player

    @property
    def image(self) -> Any:
        return self.__image

    @image.setter
    def image(self, new_image: Any) -> None:
        self.__image = new_image

    def get_sprite(self) -> None:
        dx = self.x - self.__player.x
        dy = self.y - self.__player.y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)

        delta = self.theta - self.__player.angle
        if (dx > 0 and self.__player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau

        delta_rays = delta / DELTA_ANGLE
        self.screen_x = (HALF_NUM_RAYS + delta_rays) * SCALE

        self.dist = math.hypot(dx, dy)
        self.norm_dist = self.dist * math.cos(delta)
        if -self.IMAGE_HALF_WIDTH < self.screen_x < (WIDTH + self.IMAGE_HALF_WIDTH) and self.norm_dist > 0.5:
            self.__get_sprite_projection()

    def __get_sprite_projection(self) -> None:
        proj = SCREEN_DIST / self.norm_dist * self.SPRITE_SCALE
        proj_width, proj_height = proj * self.IMAGE_RATIO, proj
        image = pg.transform.scale(self.__image, (proj_width, proj_height))
        self.sprite_half_width = proj_width // 2
        height_shift = proj_height * self.SPRITE_HEIGHT_SHIFT
        pos = self.screen_x - self.sprite_half_width, HALF_HEIGHT - proj_height // 2 + height_shift
        self.__game.ray_casting.objects_to_render.append((self.norm_dist, image, pos))

    def update(self) -> None:
        self.get_sprite()


class AnimatedSprite(Sprite):
    def __init__(self, game: Game, path='resources/sprites/animated_sprites/green_light/0.png',
                 pos=(11.5, 3.5), scale=0.8, shift=0.16, animation_time=120):
        super().__init__(game, path, pos, scale, shift)
        self.animation_time = animation_time
        self.path = path.rsplit('/', 1)[0]
        self.images = self.get_images(self.path)
        self.animation_time_prev = pg.time.get_ticks()
        self.animation_trigger = False

    def update(self):
        super().update()
        self.check_animation_time()
        self.animate(self.images)

    def animate(self, images):
        if self.animation_trigger:
            images.rotate(-1)
            self.image = images[0]

    def check_animation_time(self):
        self.animation_trigger = False
        time_now = pg.time.get_ticks()
        if time_now - self.animation_time_prev > self.animation_time:
            self.animation_time_prev = time_now
            self.animation_trigger = True

    @staticmethod
    def get_images(path):
        images = deque()
        for file_name in os.listdir(path):
            if os.path.isfile(os.path.join(path, file_name)):
                img = pg.image.load(path + '/' + file_name).convert_alpha()
                images.append(img)
        return images

