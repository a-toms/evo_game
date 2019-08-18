import unittest
from core.game import Game
from core.phases import SelectFoodAndClimatePhase, PhaseState
from core.trait_card import TraitCard


class TestSelectFoodAndClimatePhase(unittest.TestCase):
    def setUp(self):
        self.game = Game(["Smith", "Gould"])
        self.phase = SelectFoodAndClimatePhase(self.game)

    def test_ready_to_end(self):
        for player in self.game.players:
            card = TraitCard("Trait1")
            player.add_to_hand_cards([card])
            self.phase.play_card(player, card)

        state = self.phase.end()

        self.assertEqual(PhaseState.ENDED, state)