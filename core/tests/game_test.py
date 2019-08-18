import unittest
from core.game import Game
from core.species import Species


class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        self.game = Game(["Huxley", "Charlesworth", "Haldane"])


    def test_initialise_players(self):
        player_names = ["Darwin", "Mendel", "Dawkins"]
        game = Game(player_names)

        self.assertEqual(
            set(player_names),
            set(player.name for player in game.players)
        )

    def test_duplicate_players(self):
        player_names = ["Crick", "Crick"]

        self.assertRaises(ValueError, lambda: Game(player_names))

    def test_too_many_players(self):
        player_names = [
            "Watson", "Walace", "Profet", "Grant", "Buss", "Lenski",
            "Dobzhansky"
        ]

        self.assertRaises(ValueError, lambda: Game(player_names))

    def test_deal_cards(self):
        self.assertEqual(
            0,
            len(self.game.players[1].hand_cards)
        )
        self.game.deal_cards()

        self.assertEqual(
            5,
            len(self.game.players[1].hand_cards)
        )

    def test_deal_cards__gives_more_cards_if_player_has_more_species(self):
        self.game.players[1].species = [
            Species(), Species(), Species(), Species()
        ]

        self.assertEqual(
            0,
            len(self.game.players[1].hand_cards)
        )

        self.game.deal_cards()

        self.assertEqual(
            8,
            len(self.game.players[1].hand_cards)
        )

    def test_deal_cards_removes_trait_cards_from_the_cards_remaining(self):
        self.assertEqual(177, len(self.game.cards_remaining))
        self.game.deal_cards()
        self.assertEqual(162, len(self.game.cards_remaining))


