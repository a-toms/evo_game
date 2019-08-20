import abc

from pydispatch import dispatcher

from core.game import Game
from core.player import Player
from core.trait_card import TraitCard
from core.constants import PhaseState, Signal


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


class DealPhase(Phase):
    def __init__(self, game):
        super().__init__(game)

    def deal_cards(self) -> bool:
        if self.__can_deal():
            self.__distribute_cards()
            self._state = PhaseState.READY_TO_END
            return True
        else:
            self._state = PhaseState.GAME_OVER
            return False

    def __distribute_cards(self):
        for player in self._game.players:
            number_of_cards = player.receives_how_many_cards_at_round_start
            cards_to_give = self._game.draw_pile[-number_of_cards:]
            player.add_to_hand_cards(cards_to_give)
            self._game.draw_pile = self._game.draw_pile[:-number_of_cards]

    def __can_deal(self) -> bool:
        if self.__has_enough_cards_to_deal_to_each_player():
            return True
        else:
            return False

    @property
    def __number_of_cards_in_draw_pile(self) -> int:
        return self._game.number_of_cards_in_draw_pile

    def __number_of_cards_to_deal_to_all_players(self) -> int:
        total_number = 0
        for player in self._game.players:
            total_number += player.receives_how_many_cards_at_round_start
        return total_number

    def __has_enough_cards_to_deal_to_each_player(self) -> bool:
        required_number = self.__number_of_cards_to_deal_to_all_players()
        return self.__number_of_cards_in_draw_pile >= required_number


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
        if total_food > 0:
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


class FeedingPhase(Phase):
    def __init__(self, game):
        super().__init__(game)
        dispatcher.send(signal=Signal.START_FEEDING_PHASE, sender=self)

