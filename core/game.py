from core.board import Board
from core.player import Player
from core.trait_card import TraitCard
from enum import auto, Enum


class Phase(Enum):
    DEAL = auto()
    SELECT_FOOD_AND_CLIMATE = auto()
    PLAY_CARDS = auto()
    MODIFY_ENVIRONMENT = auto()
    FEEDING = auto()


class Game:
    __max_players = 6
    __total_trait_cards = 177

    def __init__(self, player_names: list):
        """
        Note that the first phase is the deal phase.
        """
        self.board = Board()
        self.players = self.__generate_players(player_names)
        self.round = 1
        self.draw_pile = [
            TraitCard(name=f'Trait{i}')
            for i in range(self.__total_trait_cards)
        ]  # Todo: Replace self.draw_pile with real traits.
        self.phase = Phase.DEAL

    def __generate_players(self, player_names: list) -> list:
        if len(set(player_names)) != len(player_names):
            raise ValueError(f'Duplicate player names found: {player_names}')
        elif len(player_names) > self.__max_players:
            raise ValueError(
                f'Too many players: {len(player_names)}. '
                f'The maximum is: {self.__max_players}')
        else:
            return [Player(player_name) for player_name in player_names]

    @property
    def number_of_cards_in_draw_pile(self) -> int:
        return len(self.draw_pile)
