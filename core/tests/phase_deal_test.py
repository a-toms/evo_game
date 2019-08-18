import unittest

from core.game import Game
from core.phases import PhaseState, DealPhase
from core.species import Species


class TestDealPhase(unittest.TestCase):
    def setUp(self):
        self._game = Game(["Dawkins", "Mendel", "Doncaster"])
        self.deal_phase = DealPhase(self._game)

    def test_deal_cards(self):
        self.assertEqual(
            0,
            len(self._game.players[1].hand_cards)
        )
        self.deal_phase.deal_cards()

        self.assertEqual(
            5,
            len(self._game.players[1].hand_cards)
        )

    def test_deal_cards__gives_more_cards_if_player_has_more_species(self):
        self._game.players[1].species = [
            Species(), Species(), Species(), Species()
        ]

        self.assertEqual(
            0,
            len(self._game.players[1].hand_cards)
        )

        self.deal_phase.deal_cards()

        self.assertEqual(
            8,
            len(self._game.players[1].hand_cards)
        )

    def test_deal_cards_removes_trait_cards_from_the_draw_pile(self):
        self.assertEqual(177, len(self._game.draw_pile))
        self.deal_phase.deal_cards()
        self.assertEqual(162, len(self._game.draw_pile))


    def test_number_of_cards_in_draw_pile__updates_after_deal(self):
        self.deal_phase.deal_cards()
        self.assertEqual(162, self._game.number_of_cards_in_draw_pile)

    def test_deal_cards__return_true_if_dealt_cards(self):
        """
        There are 3 players. Each player receives 5 cards in the deal deal_phase.
        """
        self._game.draw_pile = self._game.draw_pile[:15]

        self.assertEqual(
            True,
            self.deal_phase.deal_cards()
        )

    def test_deal_cards__return_false_if_insufficient_cards_to_deal(self):
        """
        There are 3 players. Each player receives 5 cards in the deal deal_phase.
        """
        self._game.draw_pile = self._game.draw_pile[:14]

        self.assertEqual(
            False,
            self.deal_phase.deal_cards()
        )
