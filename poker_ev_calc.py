from typing import List

class TexasHoldemGame:

    # Constructor
    def __init__(self) -> None:
        self.deck = self.generate_deck()
        self.num_of_players = None
        self.your_hand = []
        self.community_cards = []
        self.your_contribution_to_bot = None
        self.pot_size = None
        self.num_of_sims = None

    # Method to generate a 52-card deck
    def generate_deck(self):
        # Define what ranks and suits to include
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        suits = ["s", "h", "c", "d"]

        # Combine ranks and suits to form a deck
        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append(rank + suit)


        return deck

    # Setter methods to update game variables
    def set_num_of_players(self, num_of_players: float):
        self.num_of_players = num_of_players

    def set_your_hand(self, your_hand: List[str]):
        self.your_hand = your_hand

    def set_community_cards(self, community_cards: List[str]):
        self.community_cards = community_cards

    def set_your_contribution_to_bot(self, your_contribution_to_bot: float):
        self.your_contribution_to_bot = your_contribution_to_bot

    def set_pot_size(self, pot_size: float):
        self.pot_size = pot_size

    def set_num_of_sims(self, num_of_sims: int):
        self.num_of_sims = num_of_sims

    # Method to calculate the expected value of your hand
    def poker_expected_value(self):
        # Simulate possible outcomes
        win_count = 0
        
        #for _ in range(self.num_of_sims):
            # Simulate the opponent's hand
            #opponent_hand = generate_opponent_hand(cards_to_exclude)

        return 11


            
myHoldemGame = TexasHoldemGame()
myHoldemGame.set_num_of_players(5)
myHoldemGame.set_your_hand(["As", "Th"])

deck = myHoldemGame.generate_deck()
for card in deck:
    print(card)
print(len(deck))