from typing import TypeVar, Any
import pygame as pg
from settings import *


Game = TypeVar("Game")


class Player:
    def __init__(self, game: Game) -> None:
        self.rel = None
        self.__game = game
        self.__x, self.__y = PLAYER_POS
        self.__angle = PLAYER_ANGLE
        self.shot = False

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float:
        return self.__y

    @property
    def angle(self) -> float:
        return self.__angle

    @angle.setter
    def angle(self, new_value: Any) -> None:
        self.__angle = new_value

    @property
    def pos(self) -> Tuple[float, float]:
        return self.__x, self.__y

    @property
    def map_pos(self) -> Tuple[int, int]:
        return int(self.__x), int(self.__y)

    def __movement(self) -> None:
        sin_a = math.sin(self.__angle)
        cos_a = math.cos(self.__angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.__game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.__check_wall_collision(dx, dy)

        if keys[pg.K_LEFT]:
            self.__angle -= PLAYER_ROT_SPEED * self.__game.delta_time
        if keys[pg.K_RIGHT]:
            self.__angle += PLAYER_ROT_SPEED * self.__game.delta_time

        self.__angle %= math.tau  # tau = 2π

    def draw(self) -> None:
        pg.draw.line(self.__game.screen,
                     'yellow',
                     (self.__x * 100, self.__y * 100),
                     (self.__x * 100 + WIDTH * math.cos(self.__angle),
                      self.__y * 100 + WIDTH * math.sin(self.__angle)), 2)
        pg.draw.circle(self.__game.screen,
                       'green',
                       (self.__x * 100, self.__y * 100), 15)

    def __check_wall(self, x: float, y: float) -> bool:
        return (x, y) not in self.__game.map.world_map

    def __check_wall_collision(self, dx, dy) -> None:
        # best graphical when is near of the wall
        scale = PLAYER_SIZE_SCALE / self.__game.delta_time if PLAYER_SIZE_SCALE / self.__game.delta_time > 0 else 5
        if self.__check_wall(int(self.__x + dx * scale), int(self.__y)):
            self.__x += dx
        if self.__check_wall(int(self.__x), int(self.__y + dy * scale)):
            self.__y += dy

    def __mouse_control(self) -> None:
        mx, my = pg.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSITIVITY * self.__game.delta_time

    def update(self) -> None:
        self.__movement()
        self.__mouse_control()

    def single_fire_event(self, event) -> None:
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.shot:
                self.shot = True
