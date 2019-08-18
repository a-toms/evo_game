import unittest
from core.game import Game
from core.phases import PhaseState, SelectFoodAndClimatePhase
from core.trait_card import TraitCard


class TestSelectFoodAndClimatePhase(unittest.TestCase):
    def setUp(self):
        self._game = Game(["Smith", "Gould"])
        self.phase = SelectFoodAndClimatePhase(self._game)

    def test_ready_to_end(self):
        for player in self._game.players:
            card = TraitCard("Trait1")
            player.add_to_hand_cards([card])
            self.phase.play_card(player, card)

        state = self.phase.end()

        self.assertEqual(PhaseState.ENDED, state)
