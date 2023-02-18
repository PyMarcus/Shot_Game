from collections import deque
import pygame as pg
from sprites import AnimatedSprite
from settings import *


class Weapon(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/weapon/shotgun/0.png',
                 pos=(11.5, 3.5), scale=0.5, shift=0.16, animation_time=120) -> None:
        super().__init__(game, path='resources/sprites/weapon/shotgun/0.png',
                 pos=(11.5, 3.5), scale=0.1, shift=0.16, animation_time=120)

        self.game = game
        print(scale)
        self.images = deque(
            [pg.transform.smoothscale(
                img, (self.image.get_width() * scale, self.image.get_height() * scale)
            ) for img in self.images]
        )

        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        self.reloading = False
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = 50

    def draw(self) -> None:
        self.game.screen.blit(self.images[0], self.weapon_pos)

    def update(self) -> None:
        self.check_animation_time()
        self.animate_shot()

    def animate_shot(self) -> None:
        if self.reloading:
            self.game.player.shot = False
            if self.animation_trigger:
                self.images.rotate(-1)
                self.image = self.images[0]
                self.frame_counter += 1
                if self.frame_counter == self.num_images:
                    self.reloading = False
                    self.frame_counter = 0
        else:
            if self.game.player.shot:
                #sound = Sound(self.game)
                self.reloading = True
