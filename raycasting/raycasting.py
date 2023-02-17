import pygame as pg
import math
from settings import *
from typing import TypeVar


Game = TypeVar("Game")


class RayCasting:
    def __init__(self, game: Game) -> None:
        self.__game = game
        self.ray_casting_result = list()
        self.objects_to_render = list()
        self.textures = self.__game.object_renderer.wall_texture

    def get_objects_to_render(self) -> None:
        self.objects_to_render = list()
        for ray, values in enumerate(self.ray_casting_result):


    def __ray_cast(self) -> None:
        self.ray_casting_result.clear()
        texture_vert, texture_hor = None, None
        ox, oy = self.__game.player.pos
        x_map, y_map = self.__game.player.map_pos
        ray_angle = self.__game.player.angle - HALF_FOV + 0.0001
        for ray in range(NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # horizontals lines
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a

            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.__game.map.world_map:
                    texture_hor = self.__game.map.world_map[tile_hor]
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            # verticals lines
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a

            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.__game.map.world_map:
                    texture_vert = self.__game.map.world_map[tile_vert]
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            # colision with the wall (depth)
            if depth_vert < depth_hor:
                depth, texture = depth_vert, texture_vert
                y_vert %= 1
                offset = y_vert if cos_a > 0 else (1 - y_vert)
            else:
                depth, texture = depth_hor, texture_hor
                x_hor %= 1
                offset = (1 - x_hor) if sin_a > 0 else x_hor
            # debug
            """pg.draw.line(self.__game.screen, 'red', (100 * ox, 100 * oy),
                         (100 * ox + 100 * depth * cos_a, 100 * oy + 100
                          * depth * sin_a), 2)"""
            # remove the lag effect
            depth *= math.cos(self.__game.player.angle - ray_angle)


            # projection
            proj_height = SCREEN_DIST / (depth + 0.0001)

            # draw the walls
            """color = [255 / (1 + depth ** 5 * 0.00002)] * 3
            pg.draw.rect(self.__game.screen, color,
                         (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE,
                          proj_height))"""
            self.ray_casting_result.append((depth, proj_height, texture, offset))

            ray_angle += DELTA_ANGLE

    def update(self) -> None:
        self.__ray_cast()
