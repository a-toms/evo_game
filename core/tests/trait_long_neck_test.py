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
        # Constructor of the FeedingPhase sends the Signal.START_FEEDING_PHASE event
        FeedingPhase(self.game)
        expected_food_eaten = 1

        self.assertEqual(expected_food_eaten, self.species.food_eaten)

