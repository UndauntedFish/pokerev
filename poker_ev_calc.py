from typing import List
import random

class TexasHoldemGame:

    # Constructor
    def __init__(self) -> None:
        self.deck = []
        self.num_of_opponents = None
        self.player_hand = []
        self.community_cards = []
        self.your_contribution_to_bot = None
        self.pot_size = None
        self.num_of_sims = None
        self.generate_deck()


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

        self.deck = deck


    # Setter methods to update game variables
    def set_num_of_opponents(self, num_of_opponents: float):
        self.num_of_opponents = num_of_opponents

    def set_player_hand(self, player_hand: List[str]):
        self.player_hand = player_hand

    def set_community_cards(self, community_cards: List[str]):
        self.community_cards = community_cards

    def set_your_contribution_to_bot(self, your_contribution_to_bot: float):
        self.your_contribution_to_bot = your_contribution_to_bot

    def set_pot_size(self, pot_size: float):
        self.pot_size = pot_size

    def set_num_of_sims(self, num_of_sims: int):
        self.num_of_sims = num_of_sims

    def add_to_pot(self, pot_contribution: float):
        self.pot_size = self.pot_size + pot_contribution


    # Method to calculate the expected value of your hand
    def poker_expected_value(self):
        # Simulate possible outcomes
        win_count = 0
        
        # Simulate the opponents' hands.
            # Example for 3 players:
            #  [0, ["As", "Ad"]]
            #  [1, ["Ks", "3s"]]
            #  [2, ["4h", "2d"]]
        opponent_hands = []
        for _ in range(self.num_of_sims): 
            for _ in range(self.num_of_opponents):
                opponent_hands.append(self.generate_opponent_hand(self.player_hand))

        # Simulate flop, turn, and river cards
        flop_turn_river = self.generate_flop_turn_river(opponent_hands)

        # Determine if player hand is a winning hand
        player_hand_is_win = hand_is_win(hand, flop_turn_river)

        # Determine if opponents hand are winning hands

        return []
    
    
    # Method to draw a random hand for an opponent
    #  cards_to_exclude: A list of cards, to exclude from the opponent's simulated hand (for example, you should exclude the cards in your hand).
    def generate_opponent_hand(self, cards_to_exclude: List[str]):
        # Draw the first card
        first_card = self.draw_random_card()
        # Remove the first card from the deck
        leftover_deck_set = set(self.deck) - {first_card}

        # Draw the second card
        second_card = random.choice(list(leftover_deck_set))
        
        # Return the opponent's hand
        return [first_card, second_card]
    
    
    # Method to generate the flop, turn, and river cards, given the player's hand and opponents' hands
    def generate_flop_turn_river(self, opponent_hands):
        played_cards = {}

        # Add the cards in the player's hand in the played cards set
        played_cards.append(set(self.player_hand))

        # Go through each opponent and store all the cards in their hands in the played_cards set
        for opponent_hand in opponent_hands:
            first_card = opponent_hand[0]
            second_card = opponent_hand[1]
            played_cards.append({first_card, second_card})

        # Get a set of the cards left over, excluding the player's and opponents' hands
        leftover_deck_set = self.deck - played_cards

        # Draw the flop, turn, and river
        flop_card_1 = self.draw_random_cards(played_cards)
        played_cards = played_cards + {flop_card_1}

        flop_card_2 = self.draw_random_cards(played_cards)
        played_cards = played_cards + {flop_card_2}

        flop_card_3 = self.draw_random_cards(played_cards)
        played_cards = played_cards + {flop_card_3}

        turn_card = self.draw_random_cards(played_cards)
        played_cards = played_cards + {turn_card}

        river_card = self.draw_random_cards(played_cards)
        played_cards = played_cards + {river_card}

        # Return a list of all the dealt cards
        return [flop_card_1, flop_card_2, flop_card_3, turn_card, river_card]
    
    
    def draw_random_card(self, cards_to_exclude: List[str]):
        # Determine which cards are valid for the draw
        if len(cards_to_exclude > 0):
            deck_set = set(self.deck)
            cards_to_exclude_set = set(cards_to_exclude)
            leftover_deck_set = deck_set - cards_to_exclude_set
            return random.choice(list(leftover_deck_set))
        else:
            return random.choice(self.deck)


    # Determine if a hand is a win
    def hand_is_win(self, player_hand: List(str), opponent_hands: List(str), flop_turn_river: List(str)):
        if self.is_royal_flush(player_hand, flop_turn_river):
            return True
        elif self.is_straight_flush(player_hand, flop_turn_river):
            return True
        elif self.is_4_of_a_kind(player_hand, flop_turn_river):
            return True
        elif self.is_full_house(player_hand, flop_turn_river):
            return True
        elif self.is_flush(player_hand, flop_turn_river):
            return True
        elif self.is_straight(player_hand, flop_turn_river):
            return True
        elif self.is_3_of_a_kind(player_hand, flop_turn_river):
            return True
        elif self.is_2_pair(player_hand, flop_turn_river):
            return True
        elif self.is_pair(player_hand, flop_turn_river):
            return True
        elif self.is_high_card(player_hand, opponent_hands):
            return True
        else:
            return False






      
myHoldemGame = TexasHoldemGame()
myHoldemGame.set_num_of_opponents(1)
myHoldemGame.set_player_hand(["As", "Th"])
myHoldemGame.set_num_of_sims(100000)

opponent_hand = myHoldemGame.poker_expected_value()
print(opponent_hand[0])
print(opponent_hand[1])
print(opponent_hand[2])
print(opponent_hand[3])
print(opponent_hand[4])



