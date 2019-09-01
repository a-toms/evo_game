from core.constants import Signal, TraitCategory
from core.trait_card import TraitCard
from pydispatch import dispatcher


class FatTissue(TraitCard):
    def __init__(self):
        name = type(self).__name__  # Todo: Refactor name to snake case.
        categories = tuple([TraitCategory.EATING])
        super().__init__(name, categories)
        self.fat_tissue_food_amount = 0
        dispatcher.connect(
            receiver=self.handler_start_feeding_phase,
            signal=Signal.BEFORE_FEEDING_PHASE
        )

    def handler_start_feeding_phase(self, watering_hole_food=0):
        if self._owner_species_exists():
            self.eat_any_fat_tissue_food()

    def eat_any_fat_tissue_food(self):
        if self._owner_species_exists():
            if self._owner_species.is_hungry and self.fat_tissue_food_amount > 0:
                amount_to_eat = self.__get_amount_of_fat_tissue_to_eat()
                self._owner_species.eat_food_from_food_bank(food=amount_to_eat)
                self.fat_tissue_food_amount -= amount_to_eat

    def __get_amount_of_fat_tissue_to_eat(self) -> int:
        """
        Gets the food of fat tissue food that a species can eat. This food
        is the food of food that the species moves from the fat tissue card
        to its food eaten before the food cards are revealed.
        """
        if self._owner_species_exists():
            if self._owner_species.hunger_amount < self.fat_tissue_food_amount:
                return self._owner_species.hunger_amount
            else:
                return self.fat_tissue_food_amount

    def has_unused_fat_tissue(self) -> bool:
        return self.fat_tissue_food_amount < self._owner_species.body_size

    def add_to_fat_tissue(self):
        if self.has_unused_fat_tissue():
            # Todo: Find if the species can eat. Begin by finding if there is food in the watering hole.
            pass




