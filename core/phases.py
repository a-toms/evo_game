import abc
from core.game import Game
from core.player import Player
from core.trait_card import TraitCard
from enum import auto, Enum


class PhaseState(Enum):
    WAITING_FOR_PLAYER_ACTIONS = auto()
    READY_TO_END = auto()
    ENDED = auto()


class Phase(abc.ABC):
    def __init__(self, game: Game):
        self._state = PhaseState.WAITING_FOR_PLAYER_ACTIONS
        self._game = game

    def _accepting_actions(self) -> bool:
        return PhaseState.WAITING_FOR_PLAYER_ACTIONS == self._state

    def _ready_to_end(self) -> bool:
        return PhaseState.READY_TO_END == self._state

    def end(self) -> PhaseState:
        if self._ready_to_end():
            self._state = PhaseState.ENDED

        return self._state


class SelectFoodAndClimatePhase(Phase):
    def __init__(self, game):
        super().__init__(game)
        self.watering_hole_cards = []
        self.played_this_round = []

    def __update_state(self) -> PhaseState:
        if set(self._game.players) == set(self.played_this_round):
            self._state = PhaseState.READY_TO_END

        return self._state

    def __update_climate(self):
        net_effect = sum([card.climate_effect for card in self.watering_hole_cards])

        if net_effect > 0:
            self._game.board.climate_scale.increase_temperature()
        elif net_effect < 0:
            self._game.board.climate_scale.decrease_temperature()
        elif net_effect != 0:
            raise ValueError(f'Unexpected net effect: {net_effect}')

    def __update_food(self):
        total_food = sum([card.food_effect for card in self.watering_hole_cards])
        self._game.board.add_food_to_watering_hole(total_food)

    def __update_climate_and_food(self):
        self.__update_food()
        self.__update_climate()

    def play_card(self, player: Player, card: TraitCard) -> PhaseState:
        if self._accepting_actions():
            if card in player.hand_cards and player not in self.played_this_round:
                player.hand_cards.remove(card)
                self.watering_hole_cards.append(card)
                self.played_this_round.append(player)
            else:
                raise ValueError(f'{Player} cannot play {card}')
        else:
            raise ValueError('Invalid action')

        return self.__update_state()

    def end(self) -> PhaseState:
        if self._ready_to_end():
            self.__update_climate_and_food()
            self._state = PhaseState.ENDED

        return self._state

