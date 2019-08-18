from typing import List
from core.species import Species


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
    def receives_how_many_cards_at_the_round_start(self) -> int:
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

    # def add_species(self, hand_card, position: str):
    #     removed_card = self.hand_cards.pop(hand_card)
    #     if position == 'left':
    #         # append left
    #     if position == 'right':
    #         self.species.




    # todo wrote: add_species(hand_card, position)
    # remove the hand card, add a species to the left or right of existing species array.





