class Board:
    def __init__(self):
        self.watering_hole = 0
        self.climate_scale = ClimateScale()

    def add_food_to_watering_hole(self, amount: int):
        self.__change_food(amount)

    def remove_food_from_watering_hole(self, amount=1):
        self.__change_food(-amount)

    def __change_food(self, amount: int):
        if self.watering_hole + amount >= 0:
            self.watering_hole += amount
        else:
            raise ValueError(f'Cannot change watering hole by {amount}, have {self.watering_hole}.')


class Climate:
    def __init__(self, name: str, food_adjust: int, affected_body_size_range: range, population_impact: int):
        self.name = name
        self.food_adjust = food_adjust
        self.affected_body_size_range = affected_body_size_range
        self.population_impact = population_impact

    def __str__(self) -> str:
        return f'Climate: {self.name}'


class ClimateScale:
    def __init__(self):
        self.__marker_position = 0
        self.__scale = {
            -4: Climate('Ice Age', -30, range(1, 6), 4),
            -3: Climate('Freezing', -16, range(1, 4), 2),
            -2: Climate('Cold', -8, range(1, 2), 1),
            -1: Climate('Cool', -4, range(0), 0),
            0: Climate('Temperate', 0, range(0), 0),
            1: Climate('Warm', 4, range(0), 0),
            2: Climate('Tropical', 12, range(5, 6), 1),
            3: Climate('Hot', 6, range(3, 6), 2),
            4: Climate('Scorching', -20, range(1, 6), 4),
        }

    def __str__(self) -> str:
        return f'Current {self.current_climate()}'

    def current_climate(self) -> Climate:
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
            raise ValueError(f'Invalid temperature level: {new_position}. Allowed: {list(self.__scale)}')
