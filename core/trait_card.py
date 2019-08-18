
class TraitCard:
    def __init__(self, name):
        self.name = name
        self.climate_effect = 0
        self.food_effect = 0
        self.trait_categories = ()

    def __str__(self) -> str:
        return str(self.name)

    def __eq__(self, other: object) -> bool:
        if type(self) == type(other):
            return vars(self) == vars(other)
        else:
            return False

    def __hash__(self) -> int:
        return hash(tuple(vars(self).values()))

