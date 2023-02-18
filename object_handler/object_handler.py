from random import choices, randrange
from sprites import *
from typing import TypeVar
import pygame as pg
from npc import NPC


Game = TypeVar("Game")
Npc = TypeVar("Npc")


class ObjectHandler:
    def __init__(self, game: Game):
        self.enemies = None
        self.npc_positions = dict()
        self.game = game
        self.npc_list = list()
        add_npc = self.add_npc
        self.npc_sprite_path = "resources/sprites/npc/"

        add_npc(NPC(game))

    def update(self) -> None:
        #self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [npc.update() for npc in self.npc_list]
        #self.check_win()

    def add_npc(self, npc: Npc) -> None:
        self.npc_list.append(npc)

    def spawn_npc(self) -> None:
        for i in range(self.enemies):
            npc = choices(self.npc_types, self.weights)[0]
            pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
            while (pos in self.game.map.world_map) or (pos in self.restricted_area):
                pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
            self.add_npc(npc(self.game, pos=(x + 0.5, y + 0.5)))

    def check_win(self) -> None:
        if not len(self.npc_positions):
            self.game.object_render.win()
            pg.time.delay(1500)
            self.game.new_game()
    