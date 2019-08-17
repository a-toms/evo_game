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
