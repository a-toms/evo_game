import unittest
from core.game import Game


class TestGame(unittest.TestCase):
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



