import unittest
from core.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player(name='Dorothy')

    def test_str_representation(self):
        self.assertEqual(
            'Dorothy',
            str(self.player),
        )

    def test_receives_how_many_at_the_round_start(self):
        self.player.species = ['species 1', 'species 2', 'species 3']
        base_number = 4
        self.assertEqual(
            base_number + len(self.player.species),
            self.player.receives_how_many_cards_at_the_round_start
        )

    def test_add_to_food_bag(self):
        self.assertEqual(
            5,
            self.player.add_to_food_bag(5)
        )

