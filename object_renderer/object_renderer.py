import pygame as pg
from pygame import Surface
from settings import *
from typing import TypeVar


Game = TypeVar("Game")


class ObjectRenderer:
    def __init__(self, game: Game) -> None:
        self.__game = game
        self.screen = self.__game.screen
        self.wall_texture = self.__load_wall_textures()

    @staticmethod
    def __get_texture(path: str, res=(TEXTURE_SIZE, TEXTURE_SIZE)) -> Surface:
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def __load_wall_textures(self):
        return {
            1: self.__get_texture("../resources/textures/1.png"),
            2: self.__get_texture("../resources/textures/2.png"),
            3: self.__get_texture("../resources/textures/3.png"),
            4: self.__get_texture("../resources/textures/4.png"),
            5: self.__get_texture("../resources/textures/5.png")
        }