from core.constants import Signal, TraitCategory
from core.trait_card import TraitCard
from pydispatch import dispatcher


class LongNeck(TraitCard):
    def __init__(self):
        super().__init__(type(self).__name__, tuple([TraitCategory.EATING]))
        dispatcher.connect(self.handler_start_feeding_phase, Signal.START_FEEDING_PHASE)

    def handler_start_feeding_phase(self):
        # self._owner can be None, otherwise expect it to be a reference.
        # The reference may resolve to None, so we check for that too.
        # Otherwise, resolve the reference and call appropriate method.
        if self._owner is not None and self._owner() is not None:
            self._owner().eat_food()


