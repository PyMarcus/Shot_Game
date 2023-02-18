from sprites import *
from random import randint, random, choice
from settings import NPC_SIZE, NPC_SPEED, NPC_HEALTH, NPC_ACCURACY, NPC_ATTACK_DAMAGE


class NPC(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/npc/soldier/0.png',
                 pos=(10.0, 5.5), scale=0.6, shift=0.38, animation_time=180) -> None:
        super().__init__(game, path, pos, scale, shift, animation_time)

        self.attack_images = self.get_images(self.path + '/attack')
        self.death_images = self.get_images(self.path + '/death')
        self.idle_images = self.get_images(self.path + '/idle')
        self.pain_images = self.get_images(self.path + '/pain')
        self.walk = self.get_images(self.path + '/walk')

        self.attack_dist = randint(3, 6)
        self.speed = NPC_SPEED
        self.size = NPC_SIZE
        self.health = NPC_HEALTH
        self.attack_damage = NPC_ATTACK_DAMAGE
        self.accuracy = NPC_ACCURACY
        self.alive = True
        self.pain = False

    def update(self) -> None:
        self.check_animation_time()
        self.get_sprite()
