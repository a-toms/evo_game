import unittest

from core.game import Game
from core.phases import FeedingPhase
from core.species import Species
from core.traits.long_neck import LongNeck


class TestLongNeckFeedingPhase(unittest.TestCase):
    def setUp(self):
        self.game = Game(["Firestein"])
        self.species = Species()
        self.species.add_trait(LongNeck())

    def test_feed_at_start_of_feeding_phase(self):
        """
        Constructor of the FeedingPhase sends the Signal.BEFORE_FEEDING_PHASE event.
        """
        feeding_phase = FeedingPhase(self.game)
        feeding_phase.start()
        expected_food_eaten = 1

        self.assertEqual(expected_food_eaten, self.species.food_eaten)

    def test_no_feed_without_feeding_phase(self):
        expected_food_eaten = 0

        self.assertEqual(expected_food_eaten, self.species.food_eaten)

    def test_no_feed_if_no_long_neck_trait(self):
        game_2 = Game(["Dunbar"])
        blank_species = Species()
        feeding_phase = FeedingPhase(game_2)
        feeding_phase.start()

        expected_food_eaten = 0

        self.assertEqual(expected_food_eaten, blank_species.food_eaten)
