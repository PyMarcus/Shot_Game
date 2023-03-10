from typing import List, TypeVar, Dict
import pygame as pg


Game = TypeVar("Game")


class Map:
    def __init__(self, game: Game) -> None:
        self.__game = game
        self.__mini_map = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 2, 2, 2, 2, 0, 0, 0, 1, 1, 3, 0, 0, 5],
            [3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 3, 0, 0, 2],
            [3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 3, 0, 0, 2],
            [3, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [5, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [5, 1, 1, 1, 5, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4],
        ]
        self.__world_map = dict()
        self.__get_map()

    @property
    def world_map(self) -> Dict[int, int]:
        return self.__world_map

    def __get_map(self) -> None:
        for index, row in enumerate(self.__mini_map):
            for _, column in enumerate(row):
                if column:
                    self.__world_map[(_, index)] = column

    def draw(self) -> None:
        [pg.draw.rect(self.__game.screen,
                      'darkgray',
                      (pos[0] * 100, pos[1] * 100, 100, 100), 2)
         for pos in self.__world_map]
