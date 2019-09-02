import weakref
from core import species


class TraitCard:
    def __init__(self, name, trait_categories: tuple = (), owner: species = None):
        self.name = name
        self.climate_effect = 0
        self.food_effect = 0
        self.trait_categories = trait_categories
        self._owner_species = owner

    def __str__(self) -> str:
        return str(self.name)

    def __eq__(self, other: 'TraitCard') -> bool:
        if type(self) == type(other):
            return vars(self) == vars(other)
        else:
            return False

    def __hash__(self) -> int:
        return hash(tuple(vars(self).values()))

    def set_owner(self, owner_species: 'species_to_feed.Species'):
        self._owner_species = owner_species

    def _owner_species_exists(self) -> bool:
        """
        Checks if the trait card has been assigned to a species_to_feed.
        """
        return self._owner_species is not None




