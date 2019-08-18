import unittest
from core.game import Game
from core.phases import SelectFoodAndClimatePhase, PhaseState
from core.trait_card import TraitCard


class TestSelectFoodAndClimatePhase(unittest.TestCase):
    def setUp(self):
        self.game = Game(["Smith", "Gould"])
        self.phase = SelectFoodAndClimatePhase(self.game)

    def test_player_already_played(self):
        cards = [TraitCard("Test1"), TraitCard("Test2")]
        player = self.game.players[0]
        player.add_to_hand_cards(cards)
        self.phase.play_card(player, cards[0])

        self.assertRaises(ValueError, lambda: self.phase.play_card(player, cards[1]))

    def __test_climate_effects(self, net_climate):
        if net_climate > 0:
            expected_climate_name = "Warm"
        elif net_climate < 0:
            expected_climate_name = "Cool"
        else:
            expected_climate_name = "Temperate"

        actual_climate = self.game.board.climate_scale.current_climate()

        self.assertEqual(expected_climate_name, actual_climate.name)

    def __test_food_effects(self, net_food):
        expected_watering_hole = max(net_food, 0)

        self.assertEqual(expected_watering_hole, self.game.board.watering_hole)

    def test_food_and_climate_effects(self):
        for food in [-5, -1, 0, 1, 10]:
            for climate in [-4, -1, 0, 1, 4]:
                net_food = 0
                net_climate = 0
                for player in self.game.players:
                    net_food += food
                    net_climate += climate

                    card = TraitCard("Test")
                    card.climate_effect = climate
                    card.food_effect = food

                    player.add_to_hand_cards([card])

                    self.phase.play_card(player, card)

                self.phase.end()

                self.__test_climate_effects(net_climate)
                self.__test_food_effects(net_food)
                # Call 'setUp' to ensure we have a 'clean' game. Ideally would run parametrised test
                # multiple times with different arguments and then the 'native' setUp calls
                # would take care of that.
                self.setUp()

    def test_ready_to_end(self):
        for player in self.game.players:
            card = TraitCard("Trait1")
            player.add_to_hand_cards([card])
            self.phase.play_card(player, card)

        state = self.phase.end()

        self.assertEqual(PhaseState.ENDED, state)

