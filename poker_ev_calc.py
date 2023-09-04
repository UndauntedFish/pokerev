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
        #player_hand_is_win = hand_is_win(hand, flop_turn_river)

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

    '''
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
            return False'''
    
    # Determine if a player's hand is a Royal Flush win, which is an Ace, King, Queen, Jack, and 10 of the same suit.
    # Example of a valid Royal Flush win:
    #  player_hand: ["As", "Ks"]
    #  flop_turn_river: ["Js", "Qs", "9d", "Ts", "7c"]
    #   player wins with As, Ks, Qs, Js, Ts
    def is_royal_flush(self, player_hand: List[str], flop_turn_river: List[str]):
        # Get a set of the ranks and suits of the player hand and table (flop, turn, river) cards
        player_hand_set = set(player_hand)
        flop_turn_river_set = set(flop_turn_river)

        # Define the all possible Royal Flush rank and suits
        royal_flush_ranks = {"A", "K", "Q", "J", "T"}
        royal_flush_suits = {"s", "c", "h", "d"}

        # Check if the player's hand contains the required cards to win with a Royal Flush
        for suit in royal_flush_suits:
            # For this suit, generate a Royal Flush hand
            royal_flush_hand = set([rank + suit for rank in royal_flush_ranks])

            # If the royal flush hand exists within the player's hand set + the flop, turn, river set, return True
            if royal_flush_hand.issubset(player_hand_set.union(flop_turn_river_set)):
                return True
        
        # If no Royal Flush hand was found, return false
        return False
    
    # Determine if a player's hand is a Straight Flush win, which is any 5 card sequence in the same suit and are consecutive.
    # Example of a valid Straight Flush win:
    #  player_hand: ["Jd", "Td"]
    #  flop_turn_river: ["3s", "8d", "9d", "Ts", "7d"]
    #   player wins with Jd, Td, 9d, 8d, 7d
    def is_straight_flush(self, player_hand: List[str], flop_turn_river: List[str]):
        # Implement after is_flush() and is_straight() has been implemented to use those methods to simplify things here
        return False
    

    # Determine if a player's hand is a 4-of-a-kind win, which is 4 cards of the same rank.
    # Example of a valid 3-of-a-kind win:
    #  player_hand: ["Jd", "Ts"]
    #  flop_turn_river: ["Th", "Td", "", "3s", "Tc"]
    #   player wins with Ts, Th, Td, Tc
    def is_four_of_a_kind(self, player_hand: List[str], flop_turn_river: List[str]) -> bool:
        # Combine the player_hand and flop_turn_river lists
        hand_and_table_cards = player_hand + flop_turn_river

        # Create a dictionary to count the occurences of each rank
        rank_count = self.count_ranks(hand_and_table_cards)
        
        # Check if there is any rank with a count of 4 (indicating a four-of-a-kind)
        for count in rank_count.values():
            if count == 4:
                return True
        
        # Return false if no pair was found
        return False
    
    
    # Determine if a player's hand is a 3-of-a-kind win, which is 3 cards of the same rank.
    # Example of a valid 3-of-a-kind win:
    #  player_hand: ["Jd", "3s"]
    #  flop_turn_river: ["Ts", "Td", "Jd", "3s", "Tc"]
    #   player wins with Ts, Td, Tc
    def is_three_of_a_kind(self, player_hand: List[str], flop_turn_river: List[str]) -> bool:
        # Combine the player_hand and flop_turn_river lists
        hand_and_table_cards = player_hand + flop_turn_river

        # Create a dictionary to count the occurences of each rank
        rank_count = self.count_ranks(hand_and_table_cards)
        
        # Check if there is any rank with a count of 3 (indicating a three-of-a-kind)
        for count in rank_count.values():
            if count == 3:
                return True
        
        # Return false if no pair was found
        return False

    
    # Determine if a player's hand is a 2-pair win, which is 2 cards of the same rank occuring twice.
    # Example of a valid 1-pair win:
    #  player_hand: ["Jd", "Ts"]
    #  flop_turn_river: ["Ts", "Td", "Jd", "3s", "4c"]
    #   player wins with Jd, Ts
    def is_two_pair(self, player_hand: List[str], flop_turn_river: List[str]) -> bool:
        # Combine the player_hand and flop_turn_river lists
        hand_and_table_cards = player_hand + flop_turn_river

        # Create a dictionary to count the occurrences of each rank
        rank_count = self.count_ranks(hand_and_table_cards)

        # Check if there are two different pairs of ranks occurring twice
        pair_count = 0
        for count in rank_count.values():
            if count == 2:
                pair_count += 1
            if pair_count == 2:
                return True

        return False
    
    
    # Determine if a player's hand is a 1-pair win, which is 2 cards of the same rank.
    # Example of a valid 1-pair win:
    #  player_hand: ["Jd", "Td"]
    #  flop_turn_river: ["Ts", "Td", "Ah", "3s", "4c"]
    #   player wins with Td, Td
    def is_pair(self, player_hand: List[str], flop_turn_river: List[str]):
        # Combine the player_hand and flop_turn_river lists
        hand_and_table_cards = player_hand + flop_turn_river

        # Create a dictionary to count the occurences of each rank
        rank_count = self.count_ranks(hand_and_table_cards)
        
        # Check if there is any rank with a count of 2 (indicating a pair)
        for count in rank_count.values():
            if count == 2:
                return True
        
        # Return false if no pair was found
        return False


    # Counts the occurence of each rank in a set of cards.
    # Example:
    #  Cards: ["Ts", "Td", "Ah", "3s", "4c", "Jd", "Td"]
    #  count_ranks will return {("T", 3), ("A", 1), ("3", 1), ("4", 1), ("J", 1)}
    def count_ranks(self, cards: List[str]):

        # Create a dictionary to count the occurences of each rank
        rank_count = {}

        # Count the ranks in the player's hand and table
        for card in cards:
            rank = card[:-1] # Removes the last element from the string, turning "9c" into "9"
            
            if rank in rank_count:
                rank_count[rank] += 1
            else:
                rank_count[rank] = 1
        
        # Return the rank_count dictionary
        return rank_count
            

    # Return only the ranks from a list of cards
    # ["Ks", "3d"] --> ["K", "3"]]
    def get_ranks(self, cards: List[str]):
        ranks_only = []

        # Iterate through the cards and extract the ranks to store in the ranks_only list
        for card in cards:
            rank = card[:-1]  # Extract the rank (all characters except the last one)
            ranks_only.append(rank)

        return ranks_only
    
    # Return only the suits from a list of cards
    # ["Ks", "3d"] --> ["s", "d"]]
    def get_suits(self, cards: List[str]):
        suits_only = []

        # Iterate through the cards and extract the ranks to store in the suits_only list
        for card in cards:
            rank = card[-1]  # Extract the rank (all characters except the last one)
            suits_only.append(rank)

        return suits_only       





      
myHoldemGame = TexasHoldemGame()
myHoldemGame.set_num_of_opponents(1)
myHoldemGame.set_player_hand(["As", "Th"])
myHoldemGame.set_num_of_sims(100000)

player_hand = ["3c", "Jd"]
ftr = ["Kd", "Qd", "4s", "3h", "3d"]
print(myHoldemGame.is_royal_flush(player_hand, ftr))
print(myHoldemGame.is_four_of_a_kind(player_hand, ftr))
print(myHoldemGame.is_three_of_a_kind(player_hand, ftr))
print(myHoldemGame.is_two_pair(player_hand, ftr))
print(myHoldemGame.is_pair(player_hand, ftr))