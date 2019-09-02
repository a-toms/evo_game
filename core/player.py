from typing import List
from core.species import Species
from core.trait_card import TraitCard
from core.constants import SpeciesPosition


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand_cards = []
        self.species = [Species()]  # Player starts with one species_to_feed.
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

    def _add_to_hand_cards(self, cards: List) -> List:
        self.hand_cards.extend(cards)
        return self.hand_cards


    def select_food_card(self, hand_card_index: int) -> TraitCard:  # Todo: write test
        try:
            return self.hand_cards.pop(hand_card_index)
        except IndexError:
            raise IndexError (
                f'The player has no hand card in his hand cards'
                f' at the index {hand_card_index}'
            )

    def add_species(self, discard_card: TraitCard, position: SpeciesPosition):
        self.hand_cards.remove(discard_card)
        if position == SpeciesPosition.RIGHT:
            self.species.append(Species())
        elif position == SpeciesPosition.LEFT:
            self.species.insert(0, Species())

    # Todo: Write test
    def get_any_hungry_species(self) -> List:
        return [
            individual_species for individual_species in self.species
            if individual_species.is_hungry
        ]

    # Todo: Write test
    def has_at_least_one_hungry_species(self) -> bool:
        return len(self.get_any_hungry_species()) > 0

    # Todo: Write test
    def feed_species(self, species_to_feed: Species, place_to_eat: int):
        """
        This function adds food to the eating species and subtracts either:
        a) food from the watering hole; or b) population from the prey species.
        """
        if species_to_feed.is_carnivore is False:
            index = self.species.index(species_to_feed)
            eaten_food = self.species[index].eat_food_and_return_eaten_amount(place_to_eat)
            # Todo: Check here if other species recieve any food. E.g., cooperation.














