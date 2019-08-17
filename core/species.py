
class Species:
    def __init__(self):
        self.traits = set()
        self.population = 0
        self.body_size = 0
        self.food_eaten = 0

    @property
    def is_hungry(self) -> bool:
        return self.food_eaten < self.population

    def add_population(self, increase=1) -> int:
        """
        Returns updated population
        """
        self.population += increase
        return self.population

    def add_body_size(self, increase=1) -> int:
        """
        Returns updated body_size
        """
        self.body_size += increase
        return self.body_size

    def remove_unfed_population(self) -> int:
        """
        Returns the updated population.
        """
        self.population = self.food_eaten
        return self.population

    def eat_food(self, food=1) -> int:
        """
        Returns the updated food eaten.
        """
        self.food_eaten += food
        return self.food_eaten

    def __str__(self) -> str:
         # Todo: Separate the below into multiple lines that conform to PEP8.
        return f'Species: Pop {self.population} - Body size {self.body_size} - Food eaten {self.food_eaten} - Traits {self.traits}'

