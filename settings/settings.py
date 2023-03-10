from typing import Tuple
import math
# game settings


# screen settings

RES = WIDTH, HEIGHT = 1600, 900
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS: int = 0

# player settings:
PLAYER_POS: Tuple[float, float] = 1.5, 5
PLAYER_ANGLE: int = 0
PLAYER_SPEED: float = 0.004
PLAYER_ROT_SPEED: float = 0.002
PLAYER_SIZE_SCALE = 60

# ray casting settings:
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

# 3d projection:
SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

# texture:
TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2
FLOOR_COLOR = (30, 30, 30)

# mouse settings:
MOUSE_SENSITIVITY = 0.0003
MOUSE_MAX_REL = 40
MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT


# npc settings:
NPC_SPEED = 0.03
NPC_SIZE = 10
NPC_HEALTH = 100
NPC_ATTACK_DAMAGE = 10
NPC_ACCURACY = 0.15