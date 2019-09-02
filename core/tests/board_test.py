import unittest
from core.board import Board, ClimateScale


class TestClimateScale(unittest.TestCase):
    def setUp(self):
        self.climate_scale = ClimateScale()

    def test_climate_scale_defaulting(self):
        current_climate = self.climate_scale.current_climate()

        self.assertEqual('Temperate', current_climate.name)

    def test_temperature_increase(self):
        self.climate_scale.increase_temperature()
        current_climate = self.climate_scale.current_climate()

        self.assertEqual('Warm', current_climate.name)

    def test_temperature_decrease(self):
        self.climate_scale.decrease_temperature()
        self.climate_scale.decrease_temperature()
        current_climate = self.climate_scale.current_climate()

        self.assertEqual('Cold', current_climate.name)


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_watering_hole_does_not_become_negative(self):
        """
        Test that the lowest food of food that the watering hole
        can have is 0 food.
        """
        amount = -10
        self.board.update_watering_hole_food(amount)

        self.assertEqual(
            0,
            self.board.watering_hole_food
        )

    def test_update_watering_hole_food(self):
        amount = 10
        self.board.update_watering_hole_food(amount)

        self.assertEqual(
            amount,
            self.board.watering_hole_food
        )