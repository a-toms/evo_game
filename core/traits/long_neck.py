from core.constants import Signal, TraitCategory
from core.trait_card import TraitCard
from pydispatch import dispatcher


class LongNeck(TraitCard):
    def __init__(self):
        name = type(self).__name__
        categories = tuple([TraitCategory.EATING])
        super().__init__(name, categories)
        dispatcher.connect(
            self.handler_start_feeding_phase,
            Signal.BEFORE_FEEDING_PHASE
        )

    def handler_start_feeding_phase(self):
        if self.__owner_species_exists():
            self._owner_species().eat_food()

    def __owner_species_exists(self) -> bool:
        """
        Checks if the Long Neck trait has been assigned to a species.
        """
        return (self._owner_species is not None
                and self._owner_species() is not None)





