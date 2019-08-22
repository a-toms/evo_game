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
            Signal.START_FEEDING_PHASE
        )

    def handler_start_feeding_phase(self):
        if self.__owner_species_has_trait():
            self._owner_species().eat_food()

    def __owner_species_has_trait(self) -> bool:
        """
        Checks if a species has the Long Neck trait.

        self._owner may be None. Otherwise expect self.owner to be a reference.
        The reference may resolve to None; so we check for that too.
        """
        return (self._owner_species is not None
                and self._owner_species() is not None)





