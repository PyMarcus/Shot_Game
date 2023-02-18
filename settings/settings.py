from typing import Tuple
import math
# game settings


# screen settings

RES = WIDTH, HEIGHT = 700, 500
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS: int = 100

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

# mouse settings:

