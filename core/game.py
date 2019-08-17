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
        self.players = self.__generate_players(player_names)
        self.round = 1
        self.cards_remaining = [TraitCard(name=f'Trait{i}') for i in range(177)]  # Todo: Replace with real traits.
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

    def deal_cards(self):
        for player in self.players:
            number_of_cards = player.receives_how_many_cards_at_the_round_start
            cards_to_give = self.cards_remaining[-number_of_cards:]
            player.add_to_hand_cards(cards_to_give)
            self.cards_remaining = self.cards_remaining[:-number_of_cards]



