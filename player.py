class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.species = []

    def __str__(self) -> str:
        return self.name