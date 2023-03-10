import pygame as pg
import sys
from pygame import Surface

from object_handler import ObjectHandler
from settings import *
from map import Map
from typing import Any
from player import Player
from raycasting import RayCasting
from object_renderer import ObjectRenderer
from sprites import Sprite, AnimatedSprite
from weapons import Weapon
from sound_management import Sound


class Game:
    def __init__(self) -> None:
        """
        Start the window
        and time object
        """
        pg.init()
        pg.mouse.set_visible(False)
        self.__screen = pg.display.set_mode(RES)
        self.__clock = pg.time.Clock()
        self.__map = None
        self.__player = None
        self.__ray_casting = None
        self.__object_render = None
        self.__delta_time: Any = 1
        self.__new_game()

    @property
    def ray_casting(self) -> Any:
        return self.__ray_casting

    @property
    def object_render(self) -> Any:
        return self.__object_render

    @property
    def delta_time(self) -> Any:
        return self.__delta_time

    @property
    def screen(self) -> Surface:
        return self.__screen

    @property
    def map(self) -> Map:
        return self.__map

    @map.setter
    def map(self, value: Map):
        self.__map = value

    @property
    def player(self) -> Player:
        return self.__player

    @player.setter
    def player(self, value: Player):
        self.__player = value

    def __new_game(self) -> None:
        self.__map = Map(self)
        self.__player = Player(self)
        self.__object_render = ObjectRenderer(self)
        self.__ray_casting = RayCasting(self)
        self.__sprite_objects = Sprite(self)
        self.__animate_sprite_objects = AnimatedSprite(self)
        self.__weapon = Weapon(self)
        self.__sound = Sound(self)
        self.__handle_objects = ObjectHandler(self)

    def new_game(self) -> Any:
        return self.__new_game()

    def __update(self) -> None:
        """
        Update screen and update fps how title of window
        and set the legend to screen
        :return:
        """
        self.player.update()
        self.__ray_casting.update()
        #self.__sprite_objects.update()
        self.__animate_sprite_objects.update()
        self.__weapon.update()
        self.__handle_objects.update()
        pg.display.flip()
        self.__delta_time = self.__clock.tick(FPS)
        pg.display.set_caption(f"{self.__clock.get_fps():.1f}")

    def __draw(self) -> None:
        # self.__screen.fill('black')
        self.object_render.draw()
        self.__weapon.draw()
        # self.__map.draw()
        # self.__player.draw()

    def __check_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit(0)
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.__sound.gun_sound()
            self.__player.single_fire_event(event)

    def run(self) -> None:
        while True:
            self.__check_events()
            self.__update()
            self.__draw()


if __name__ == '__main__':
    game = Game()
    game.run()
