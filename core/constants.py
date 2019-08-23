from enum import auto, Enum


class SpeciesPosition(Enum):
    LEFT = auto()
    RIGHT = auto()


class Phase(Enum):
    DEAL = auto()
    SELECT_FOOD_AND_CLIMATE = auto()
    PLAY_CARDS = auto()
    MODIFY_ENVIRONMENT = auto()
    FEEDING = auto()


class PhaseState(Enum):
    WAITING_FOR_PLAYER_ACTIONS = auto()  # Perhaps rename to WAITING_FOR_ACTIONS.
    READY_TO_END = auto()
    ENDED = auto()
    GAME_OVER = auto()


class Signal(Enum):
    BEFORE_FEEDING_PHASE = auto()  # Note to B: See Green box on p.7 of rules regarding the play order. I also note that there will need to be an order in which these BEFORE_FEEDING_PHASE cards are activated. I suggest, 1. Fertile, 2. Fat Tissue, 3. Long Neck.


class TraitCategory(Enum):
    DEFENSIVE = auto()
    EATING = auto()
    CARNIVORE = auto()
    CLIMATE = auto()
    OTHER = auto()

