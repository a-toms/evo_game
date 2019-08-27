from core.trait_card import TraitCard


class Species:
    def __init__(self, name='nameless species'):
        self.traits = {}
        self.population = 1
        self.body_size = 1
        self.food_eaten = 0
        self.name = name

    @property
    def is_hungry(self) -> bool:
        return self.food_eaten < self.population

    @property
    def hunger_amount(self) -> int:
        return self.population - self.food_eaten

    def add_population(self, increase=1):
        if self.population < 6:
            self.population += increase

    def add_body_size(self, increase=1):
        self.body_size += increase

    def add_trait(self, trait: TraitCard):
        self.traits[f'{trait.name}'] = trait
        trait.set_owner(self)

    def __remove_unfed_population(self):
        self.population = self.food_eaten

    def __reset_food_eaten(self):
        self.food_eaten = 0

    def update_species_population_and_food_eaten_after_feeding(self):
        self.__remove_unfed_population()
        self.__reset_food_eaten()

    def eat_food_from_food_bank(self, food=1):
        if self.is_hungry:
            self.food_eaten += food

    def eat_food_from_watering_hole(self, food=1):
        # Todo: Continue here.
        # Add food to species
        # Remove food from the watering hole in the game instance.
        pass

    def __str__(self) -> str:
        return (
            f'Species: Pop {self.population} - Body size {self.body_size}'
            f' - Food eaten {self.food_eaten} - Traits {list(self.traits.keys())}'
        )


