class Board:
    def __init__(self):
        self.watering_hole_food = 0
        self.climate_scale = ClimateScale()

    # Todo: write test
    @property
    def watering_hole_has_food(self) -> bool:
        return self.watering_hole_food > 0

    def update_watering_hole_food(self, food: int):
        if self.watering_hole_food + food >= 0:
            self.watering_hole_food += food
        else:
            self.watering_hole_food = 0


class ClimateZone:
    def __init__(self, name: str, food_adjust: int, affected_body_size_range: range, population_impact: int):
        self.name = name
        self.food_adjust = food_adjust
        self.affected_body_size_range = affected_body_size_range
        self.population_impact = population_impact

    def __str__(self) -> str:
        return f'ClimateZone: {self.name}'


class ClimateScale:
    def __init__(self):
        self.__marker_position = 0
        self.__scale = {  # Note that the below ClimateZones are for a 4-6 player game.
            -4: ClimateZone('Ice Age', -30, range(1, 6), 4),
            -3: ClimateZone('Freezing', -16, range(1, 4), 2),
            -2: ClimateZone('Cold', -8, range(1, 2), 1),
            -1: ClimateZone('Cool', -4, range(0), 0),
            0: ClimateZone('Temperate', 0, range(0), 0),
            1: ClimateZone('Warm', 4, range(0), 0),
            2: ClimateZone('Tropical', 12, range(5, 6), 1),
            3: ClimateZone('Hot', 6, range(3, 6), 2),
            4: ClimateZone('Scorching', -20, range(1, 6), 4),
        }

    def __str__(self) -> str:
        return f'Current {self.current_climate()}'

    def current_climate(self) -> ClimateZone:
        return self.__scale[self.__marker_position]

    def increase_temperature(self):
        self.__change_marker_position(1)

    def decrease_temperature(self):
        self.__change_marker_position(-1)

    def __change_marker_position(self, change: int):
        current_position = self.__marker_position
        new_position = current_position + change

        if new_position in self.__scale.keys():
            self.__marker_position += change
        else:
            raise ValueError(
                f'Invalid temperature level: {new_position}. '
                f'Allowed: {list(self.__scale)}'
            )
