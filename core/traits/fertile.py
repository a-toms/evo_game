from core.constants import Signal, TraitCategory
from core.trait_card import TraitCard
from pydispatch import dispatcher


class Fertile(TraitCard):
    def __init__(self):
        name = type(self).__name__
        categories = tuple([TraitCategory.OTHER])
        super().__init__(name, categories)
        dispatcher.connect(
            self.handler_start_feeding_phase,
            Signal.BEFORE_FEEDING_PHASE
        )

    def handler_start_feeding_phase(self, watering_hole_food=0):
        if self.__owner_species_exists():
            self.__add_population_if_food_in_the_watering_hole(
                watering_hole_food
            )

    def __add_population_if_food_in_the_watering_hole(self, watering_hole_food):
            if watering_hole_food > 0:
                self.owner_species.add_population()

    def __owner_species_exists(self) -> bool:
        """
        Checks if the Fertile trait has been assigned to a species.
        """
        return self.owner_species is not None
