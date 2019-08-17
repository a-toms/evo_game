import unittest
from core.species import Species


class TestSpecies(unittest.TestCase):
    def setUp(self):
        self.species = Species()

    def test_is_hungry__returns_true_when_hungry(self):
        self.species.population = 2
        self.species.food_eaten = 1

        self.assertEqual(
            True,
            self.species.is_hungry
        )

    def test_is_hungry__returns_false_when_not_hungry(self):
        self.species.population = 2
        self.species.food_eaten = 2

        self.assertEqual(
            False,
            self.species.is_hungry
        )

    def test_eat_food(self):
        self.assertEqual(
            0,
            self.species.food_eaten
        )
        self.species.eat_food(4)

        self.assertEqual(
            4,
            self.species.food_eaten
        )

    def test_update_species_population_and_food_eaten_after_feeding(self):
        self.species.population = 4
        self.species.food_eaten = 2
        self.species.update_species_population_and_food_eaten_after_feeding()

        self.assertEqual(
            [2, 0],
            [self.species.population, self.species.food_eaten]
        )

    def test_str(self):
        self.species.population = 2
        self.species.body_size = 3
        self.species.food_eaten = 2
        self.species.traits.add('Trait 1')

        self.assertEqual(
            'Species: Pop 2 - Body size 3 - Food eaten 2 - Traits {\'Trait 1\'}',
            str(self.species)
        )
