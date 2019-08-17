from typing import List

class Player:
    def __init__(self, name):
        self.name = name
        self.hand_cards = []
        self.species = []
        self.food_bag = 0

    def __str__(self) -> str:
        return str(self.name)

    @property
    def receives_how_many_cards_at_the_round_start(self) -> int:
        base_number_of_cards_to_receive = 4
        return base_number_of_cards_to_receive + len(self.species)

    def add_to_food_bag(self, food: int) -> int:
        self.food_bag += food
        return self.food_bag

    def add_to_hand_cards(self, cards: List) -> List:
        self.hand_cards.extend(cards)
        return self.hand_cards





