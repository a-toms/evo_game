
class Species:
    def __init__(self):
        self.traits = set()
        self.population = 0
        self.body_size = 0
        self.food_eaten = 0

    @property
    def is_hungry(self) -> bool:
        return self.food_eaten < self.population

    def add_population(self, increase=1):
        self.population += increase
        return self.population

    def add_body_size(self, increase=1):
        self.body_size += increase

    def __remove_unfed_population(self):
        self.population = self.food_eaten

    def __reset_food_eaten(self):
        self.food_eaten = 0

    def update_species_population_and_food_eaten_after_feeding(self):
        self.__remove_unfed_population()
        self.__reset_food_eaten()

    def eat_food(self, food=1):
        self.food_eaten += food

    def __str__(self) -> str:
        # Todo: Separate the below into multiple lines that conform to PEP8.
        return f'Species: Pop {self.population} - Body size {self.body_size} - Food eaten {self.food_eaten} - Traits {self.traits}'

