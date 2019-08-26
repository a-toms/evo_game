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
        Test that the species moves any existing fat tissue food that it has
        to the species food eaten at the feeding phase's start.

        This test considers the situation where a species' population is higher
        or equal to the species' fat tissue food.
        """
        self.species.food_eaten = 0
        self.species.population = 3
        self.species.body_size = 3
        self.species.fat_tissue_food = 1
        self.feeding_phase.start()

        self.assertEqual(
            1,
            self.species.food_eaten
        )
        self.assertEqual(
            0,
            self.species.fat_tissue_food  # The remaining fat tissue food.
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
        self.species.fat_tissue_food = 5
        self.feeding_phase.start()

        self.assertEqual(
            3,
            self.species.food_eaten
        )
        self.assertEqual(
            2,
            self.species.fat_tissue_food  # The remaining fat tissue food.
        )

    def test_species_cannot_add_more_fat_tissue_food_than_body_size(self):
        self.fail()

    def test_species_adds_to_fat_tissue_up_to_its_body_size(self):
        """
        Tests that a species can only add an amount of body tissue food up to
        the species' body size.
        """
        self.species.food_eaten = 3
        self.species.population = 3
        self.species.body_size = 3

        self.fail()



    def test_fertile_increases_population_by_one_if_food_in_watering_hole(self):
        self.game.board.watering_hole_food = 1
        population_after_growth = 2
        self.feeding_phase.start()

        self.assertEqual(
            population_after_growth,
            self.species.population
        )

    def test_fertile_does_not_increase_population_if_no_food_in_watering_hole(self):
        self.game.board.watering_hole_food = 0
        population_without_growth = 1
        self.feeding_phase.start()

        self.assertEqual(
            population_without_growth,
            self.species.population
        )


if __name__ == '__main__':
    unittest.main()
