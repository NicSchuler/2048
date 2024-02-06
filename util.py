from enum import Enum

MIN_SCREEN_HEIGHT = 18
MIN_SCREEN_WIDTH = 28

class GameState(Enum):
    RUNNING = 0
    FINISHED = 1