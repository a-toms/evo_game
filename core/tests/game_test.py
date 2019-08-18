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

    def test_number_of_cards_in_draw_pile(self):
        self.assertEqual(177, self.game.number_of_cards_in_draw_pile)
