import unittest
from core.trait_card import TraitCard


class TestTraitCard(unittest.TestCase):
    def setUp(self):
        self.trait_card = TraitCard(name='Burrowing')

    def test_str_representation(self):
        self.assertEqual(
            'Burrowing',
            str(self.trait_card),
        )

    def test_eq_returns_true_when_trait_cards_are_equal(self):
        trait_card_1 = TraitCard(name='Burrowing')
        trait_card_2 = TraitCard(name='Burrowing')
        self.assertEqual(
            trait_card_1,
            trait_card_2
        )

    def test_eq_returns_false_when_trait_cards_are_not_equal(self):
        trait_card_1 = TraitCard(name='Burrowing')
        trait_card_2 = TraitCard(name='Long neck')
        self.assertNotEqual(
            trait_card_1,
            trait_card_2
        )

    def test_hash_is_the_same_for_two_trait_cards(self):
        trait_card_1 = TraitCard(name='Burrowing')
        trait_card_2 = TraitCard(name='Burrowing')
        self.assertEqual(
            hash(trait_card_1),
            hash(trait_card_2)
        )


