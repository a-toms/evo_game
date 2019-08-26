import unittest

from core.game import Game
from core.phases import FeedingPhase
from core.species import Species
from core.traits.fat_tissue import FatTissue


class TestFatTissue(unittest.TestCase):
    def setUp(self):
        self.game = Game(["Fitch"])
        self.species = Species()
        self.species.add_trait(FatTissue())
        self.feeding_phase = FeedingPhase(self.game)

    def test_species_initial_population(self):
        self.assertEqual(
            1,
            self.species.population
        )

    def test_species_eats_existing_fat_tissue__higher_or_equal_pop(self):
        """
        Test that the species moves any of its existing fat tissue food
        to its food eaten at the feeding phase's start.

        This test covers the situation where a species' population is higher
        or equal to the species' fat tissue food.
        """
        self.species.food_eaten = 0
        self.species.population = 3
        self.species.body_size = 3
        self.species.fat_tissue_food_amount = 1
        self.feeding_phase.start()

        self.assertEqual(
            1,
            self.species.food_eaten
        )
        self.assertEqual(
            0,
            self.species.fat_tissue_food_amount  # The remaining fat tissue food.
        )

    def test_species_eats_existing_fat_tissue__lower_pop(self):
        """
        Test that the species moves any existing fat tissue food that it has
        to the species food eaten at the feeding phase's start.

        This test considers the situation where a species' population is lower
        than the species' fat tissue food.
        """
        self.species.food_eaten = 0
        self.species.population = 3
        self.species.body_size = 3
        self.species.traits
        self.feeding_phase.start()

        self.assertEqual(
            3,
            self.species.food_eaten
        )
        self.assertEqual(
            2,
            self.species.fat_tissue_food_amount  # The remaining fat tissue food.
        )

    def test_species_cannot_add_more_fat_tissue_food_than_body_size(self):
        # Todo: Complete test_
        pass

    def test_species_adds_to_fat_tissue_up_to_its_body_size(self):
        """
        Tests that a species can only add an amount of body tissue food up to
        the species' body size.
        """
        self.species.food_eaten = 3
        self.species.population = 3
        self.species.body_size = 3

        # Todo: Complete test

    def test_owner_species_exists__returns_false_if_no_owner_species(self):
        fat_tissue_card = FatTissue()

        self.assertFalse(
            fat_tissue_card.owner_species_exists()
        )

    def test_owner_species_exists__returns_true_if_owner_species(self):
        self.game = Game(["Fitch"])
        self.species = Species()
        fat_tissue_card = FatTissue()
        self.species.add_trait(fat_tissue_card)

        self.assertTrue(
            fat_tissue_card.owner_species_exists()
        )


if __name__ == '__main__':
    unittest.main()
