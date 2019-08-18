from typing import List
from core.species import Species
from core.trait_card import TraitCard
from core.constants import SpeciesPosition


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand_cards = []
        self.species = [Species()]  # Player starts with one species.
        self.food_bag = 0

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'Player {self.name}'

    @property
    def receives_how_many_cards_at_round_start(self) -> int:
        base_number_of_cards_to_receive = 4
        if len(self.species) == 0:
            raise ValueError(
                f'Every player must have at least one species when it ' +
                f'receives cards.'
            )
        else:
            return base_number_of_cards_to_receive + len(self.species)

    def add_to_food_bag(self, food: int) -> int:
        self.food_bag += food
        return self.food_bag

    def add_to_hand_cards(self, cards: List) -> List:
        self.hand_cards.extend(cards)
        return self.hand_cards

    def add_species(self, discard_card: TraitCard, position: SpeciesPosition):
        self.hand_cards.remove(discard_card)
        if position == SpeciesPosition.RIGHT:
            self.species.append(Species())
        elif position == SpeciesPosition.LEFT:
            self.species.insert(0, Species())








