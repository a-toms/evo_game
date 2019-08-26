from core.constants import Signal, TraitCategory
from core.trait_card import TraitCard
from pydispatch import dispatcher


class FatTissue(TraitCard):
    def __init__(self):
        name = type(self).__name__
        categories = tuple([TraitCategory.EATING])
        super().__init__(name, categories)
        self.fat_tissue_food_amount = 0
        dispatcher.connect(
            self.handler_start_feeding_phase,
            Signal.BEFORE_FEEDING_PHASE
        )

    def handler_start_feeding_phase(self):
        if self.__owner_species_exists():  # Fixme: This is currently not returning false when no partnet.
            print(f' owner species exist = {self.__owner_species_exists()}')
            self.eat_any_fat_tissue_food()

    def eat_any_fat_tissue_food(self):
        if self._owner_species.is_hungry and self.fat_tissue_food_amount > 0:
            amount_to_eat = self.__get_amount_of_fat_tissue_to_eat()
            self._owner_species.eat_food(food=amount_to_eat)
            self.fat_tissue_food_amount -= amount_to_eat

    def __get_amount_of_fat_tissue_to_eat(self) -> int:
        if self._owner_species.hunger_amount < self.fat_tissue_food_amount:
            return self._owner_species.hunger_amount
        else:
            return self.fat_tissue_food_amount

    def __owner_species_exists(self) -> bool:
        """
        Checks if the fat tissue trait has been assigned to a species.
        """
        print(self._owner_species)
        print(self._owner_species())
        return self._owner_species is not None and self._owner_species() is not None
