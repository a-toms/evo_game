from core.constants import Signal, TraitCategory
from core.trait_card import TraitCard
from pydispatch import dispatcher


class LongNeck(TraitCard):
    def __init__(self):
        name = type(self).__name__
        categories = tuple([TraitCategory.EATING])
        super().__init__(name, categories)
        dispatcher.connect(self.handler_start_feeding_phase, Signal.START_FEEDING_PHASE)

    def handler_start_feeding_phase(self):
        # self._owner can be None, otherwise expect it to be a reference.
        # The reference may resolve to None, so we check for that too.
        # Otherwise, resolve the reference and call appropriate method.
        if self._parent_species is not None and self._parent_species() is not None:
            self._parent_species().eat_food()


