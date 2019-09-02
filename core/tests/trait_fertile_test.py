import unittest

from core.game import Game
from core.phases import FeedingPhase
from core.species import Species
from core.traits.fertile import Fertile


class TestFertile(unittest.TestCase):
    def setUp(self):
        self.game = Game(["Gadagkar"])
        self.species = Species()  # Each species_to_feed starts with 1 population
        self.species.add_trait(Fertile())
        self.feeding_phase = FeedingPhase(self.game)

    def test_species_initial_population(self):
        self.assertEqual(
            1,
            self.species.population
        )

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

