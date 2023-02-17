import pygame as pg
from pygame import Surface
from settings import *
from typing import TypeVar, Any, Dict

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

    def draw(self) -> None:
        self.__render_game_objects()

    def __render_game_objects(self) -> None:
        list_objects = self.__game.ray_casting.objects_to_render
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    def __load_wall_textures(self) -> Dict[int, Any]:
        return {
            1: self.__get_texture("resources/textures/1.png"),
            2: self.__get_texture("resources/textures/2.png"),
            3: self.__get_texture("resources/textures/3.png"),
            4: self.__get_texture("resources/textures/4.png"),
            5: self.__get_texture("resources/textures/5.png")
        }