from enum import auto, Enum


class Position(Enum):
    LEFT = auto()
    RIGHT = auto()


class Phase(Enum):
    DEAL = auto()
    SELECT_FOOD_AND_CLIMATE = auto()
    PLAY_CARDS = auto()
    MODIFY_ENVIRONMENT = auto()
    FEEDING = auto()
    GAME_OVER = auto()


class PhaseState(Enum):
    WAITING_FOR_PLAYER_ACTIONS = auto()  # Perhaps rename to WAITING_FOR_ACTIONS.
    READY_TO_END = auto()
    ENDED = auto()
    GAME_OVER = auto()