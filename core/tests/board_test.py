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

    def test_empty_watering_hole_error(self):
        self.assertRaises(
            ValueError,
            self.board.remove_food_from_watering_hole
        )

    def test_add_food_to_watering_hole(self):
        amount = 10
        self.board.add_to_watering_hole(amount)

        self.assertEqual(amount, self.board.watering_hole_food)