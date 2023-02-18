import os
import time

import pygame as pg
from typing import TypeVar

Game = TypeVar("Game")


class Sound:
    def __init__(self, game: Game) -> None:
        self.game = game

    @staticmethod
    def gun_sound() -> None:
        pg.mixer.init()
        path = "resources/sound/shotgun.wav"
        shotgun = pg.mixer.Sound(path)
        shotgun.play()
