from core.board import Board
from core.player import Player
from core.trait_card import TraitCard
from core.constants import Phase


class Game:
    """
    The game's control flow occurs in the Game instance.
    The Game instance will call the phase instances's public methods.

    Note that the first phase is the deal phase.
    """
    __max_players = 6
    __total_trait_cards = 177

    def __init__(self, player_names: list):
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
