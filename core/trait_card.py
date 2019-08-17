
class TraitCard:
    def __init__(self, name):
        self.name = name
        self.climate_effect = 0
        self.food_effect = 0
        self.trait_effect = []

    def __str__(self) -> str:
        return str(self.name)

