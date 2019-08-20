import unittest
from core.player import Player
from core.trait_card import TraitCard
from core.constants import SpeciesPosition
from core.species import Species


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player(name='Dorothy')

    def test_str(self):
        self.assertEqual(
            'Dorothy',
            str(self.player),
        )

    def test_receives_how_many_cards_at_the_round_start(self):
        self.player.species = ['species 1', 'species 2', 'species 3']
        base_number = 4

        self.assertEqual(
            base_number + len(self.player.species),
            self.player.receives_how_many_cards_at_round_start
        )

    def test_receives_how_many_cards_at_the_round_start_raises_error_if_no_species(self):
        self.player.species = []

        self.assertRaises(
            ValueError,
            lambda: self.player.receives_how_many_cards_at_round_start
        )

    def test_add_to_food_bag(self):
        self.assertEqual(
            5,
            self.player.add_to_food_bag(5)
        )

    def test_add_to_hand_cards(self):
        cards = ['new card 1']
        self.player.add_to_hand_cards(cards)

        self.assertEqual(
            ['new card 1'],
            self.player.hand_cards
        )

    def test_add_species__removes_discard_card_from_player_hand_cards(self):
        self.player.hand_cards.extend(
            [TraitCard(name='Trait 1'), TraitCard(name='Trait 2')]
        )
        self.player.add_species(
            discard_card=self.player.hand_cards[0],
            position=SpeciesPosition.RIGHT
        )

        self.assertEqual(
            [TraitCard(name='Trait 2')],
            self.player.hand_cards
        )

    def test_add_species_left(self):
        """
        Test function adds species to the left of existing species.
        """
        self.player.hand_cards = [TraitCard(name='Trait 1')]
        initial_species = [Species(name='first species')]
        self.player.species = initial_species
        self.player.add_species(
            discard_card=self.player.hand_cards[0],
            position=SpeciesPosition.LEFT
        )

        self.assertEqual(
            ['nameless species', 'first species'],
            [self.player.species[0].name, self.player.species[1].name]
        )

    def test_add_species_right(self):
        """
        Test function adds species to the right of existing species.
        """
        self.player.hand_cards = [TraitCard(name='Trait 1')]
        initial_species = [Species(name='first species')]
        self.player.species = initial_species
        self.player.add_species(
            discard_card=self.player.hand_cards[0],
            position=SpeciesPosition.RIGHT
        )

        self.assertEqual(
            ['first species', 'nameless species'],
            [str(self.player.species[0].name), str(self.player.species[1].name)]
        )
