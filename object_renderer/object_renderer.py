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
        self.sky_image = self.__get_texture('resources/textures/sol.png', (WIDTH, HALF_HEIGHT))
        self.sky_offset = 0
        self.win_image = self.__get_texture('resources/textures/win.png', RES)

    @staticmethod
    def __get_texture(path: str, res=(TEXTURE_SIZE, TEXTURE_SIZE)) -> Surface:
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def draw(self) -> None:
        self.__draw_background()
        self.__render_game_objects()

    def win(self):
        self.screen.blit(self.win_image, (0, 0))

    def __draw_background(self) -> None:
        self.sky_offset = (self.sky_offset + 4.5 * self.__game.player.rel) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))
        # FLOOR
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    def __render_game_objects(self) -> None:
        list_objects = sorted(self.__game.ray_casting.objects_to_render, key=lambda i: i[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    def __load_wall_textures(self) -> Dict[int, Any]:
        return {
            1: self.__get_texture("resources/textures/1.png"),
            2: self.__get_texture("resources/textures/2.png"),
            3: self.__get_texture("resources/textures/3.png"),
            4: self.__get_texture("resources/textures/4.png"),
            5: self.__get_texture("resources/textures/5.png"),
            #6: self.__get_texture("resources/textures/lula.png")
        }