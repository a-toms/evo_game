from core.board import Board
from core.player import Player
from core.trait_card import TraitCard
from core.constants import Phase, SpeciesPosition
from core.phases import DealPhase, SelectFoodAndClimatePhase


class Game:
    """
    The game's control flow occurs in the Game instance.
    The Game instance will call the phase instances's public methods.

    Note that the first phase is the deal phase.
    """
    __max_players = 6
    __total_trait_cards = 177

    def __init__(self, player_names: list):
        self.board = Board()
        self.players = self.__generate_players(player_names)
        self.round = 1
        self.draw_pile = [
            TraitCard(name=f'Trait{i}')
            for i in range(self.__total_trait_cards)
        ]  # Todo: Replace self.draw_pile with real traits.
        self.phase = Phase.DEAL

    def __generate_players(self, player_names: list) -> list:
        if len(set(player_names)) != len(player_names):
            raise ValueError(f'Duplicate player names found: {player_names}')
        elif len(player_names) > self.__max_players:
            raise ValueError(
                f'Too many players: {len(player_names)}. '
                f'The maximum is: {self.__max_players}')
        else:
            return [Player(player_name) for player_name in player_names]

    @property
    def number_of_cards_in_draw_pile(self) -> int:
        return len(self.draw_pile)

    def play(self):
        # Deal cards
        deal_phase = DealPhase(self)
        deal_phase.deal_cards()

        # Select food cards. Wait for all players to submit food cards. Begin by checking for this by using a while loop.
        food_cards = []
        for player in self.players:  # Change this to async so that players can submit food card simultaneously.
            hand_card_index = int(input(f'{player}, select index of food card'))
            food_card = player.select_food_card(hand_card_index)
            print(f'Selected {food_card}')
            food_cards.append(food_card)
        self.board.add_to_watering_hole(food=5)

        # First player plays cards. Once, complete next player plays cards, and so on until completion.
        for player in self.players:
            print(f'{player} decides to create a new species')
            new_species_position = input(f'{player} select left or right')
            if new_species_position == 'left':
                player.add_species(discard_card=player.hand_cards[0], position=SpeciesPosition.LEFT)
            elif new_species_position == 'right':
                player.add_species(discard_card=player.hand_cards[0], position=SpeciesPosition.RIGHT)
            print(player.species)

        # Pre-feeding phase card actions, e.g., Long Neck ## Todo: Cont here! :)
        ## For each player, check if any pre-feeding phase traits. If yes, activate Fertile, Long Neck, and Fat Tissue (in that order)

        # Modify environment
        ## Update the Board and Climate based on the selected food cards. Apply any climate effects to species.

        # Feeding phase
        ## Players feed their species until none can eat. Add method for herbivores first -> If there any food on the watering hole.


        # Check if game over. If yes, exit loop and show winner.


if __name__ == '__main__':
    game = Game(['Frank', 'Futuyma', 'Gadagkar', 'Galton'])
    game.play()