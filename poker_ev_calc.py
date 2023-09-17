from typing import List
import random

class TexasHoldemGame:

    # Constructor
    def __init__(self) -> None:
        self.deck = []
        self.num_of_opponents = 6
        self.player_hand = []
        self.community_cards = []
        self.your_contribution_to_bot = None
        self.pot_size = None
        self.num_of_sims = 100
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
        
        



        return []
    
    # Returns a number from 0.0 - 1.0, representing the winrate of the player's hand
    def get_player_hand_winrate(self):
        win_count = 0

        # Simulate possible outcomes
        for i in range(self.num_of_sims):
            # Simulate the opponents' hands.
                # Example for 3 players:
                #  [0, ["As", "Ad", 0]]
                #  [1, ["Ks", "3s", 0]]
                #  [2, ["4h", "2d", 0]]
            opponent_hands = []
            for _ in range(self.num_of_sims): 
                for _ in range(self.num_of_opponents):
                    opponent_hands.append(self.generate_opponent_hand(self.player_hand))


            # Simulate flop, turn, and river cards
            flop_turn_river = self.generate_flop_turn_river(opponent_hands)


            # Determine if player hand is a winning hand. 
            # Will return a int 1-10 if it is a winning hand, 0 if it isnt.
            # The higher the int, the stronger the winning hand
            player_hand_is_win = self.hand_is_win(self.player_hand, opponent_hands, flop_turn_river)


            # Determine if opponents hand are winning hands
            player_and_opponent_cards = player_hand + opponent_hands
            opponent_hand_is_win = 0

            for opponent_hand in opponent_hands:
                # Figure out what's left between the player's and opponents' cards if we remove the opponent's hand we're trying to evaluate
                leftover_cards = []
                for card in player_and_opponent_cards:
                    if card not in opponent_hand:
                        leftover_cards.append(card)
                
                # Determine if the opponent's hand is a winning hand. 
                # Will return a int 1-10 if it is a winning hand, 0 if it isnt.
                # The higher the int, the stronger the winning hand
                this_opponent_hand_is_win = self.hand_is_win(opponent_hand, leftover_cards, flop_turn_river)
                if this_opponent_hand_is_win > opponent_hand_is_win:
                    opponent_hand_is_win = this_opponent_hand_is_win
            

            # Increment the win counter if the player won
            if player_hand_is_win > opponent_hand_is_win:
                win_count += 1
            
        return win_count / self.num_of_sims


    # Method to draw a random hand for an opponent in the format: [first card, second card, 0], where 0 is the win/loss status of the hand.
    #  cards_to_exclude: A list of cards, to exclude from the opponent's simulated hand (for example, you should exclude the cards in your hand).
    def generate_opponent_hand(self, cards_to_exclude: List[str]):
        # Draw the first card
        first_card = self.draw_random_card(cards_to_exclude)
        # Remove the first card from the deck
        leftover_deck_set = set(self.deck) - {first_card}

        # Draw the second card
        second_card = random.choice(list(leftover_deck_set))
        
        # Return the opponent's hand
        return [first_card, second_card, 0]
    
    
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
    
    
    # Method to draw a random card
    def draw_random_card(self, cards_to_exclude: List[str]):
        # Determine which cards are valid for the draw
        if len(cards_to_exclude > 0):
            deck_set = set(self.deck)
            cards_to_exclude_set = set(cards_to_exclude)
            leftover_deck_set = deck_set - cards_to_exclude_set
            return random.choice(list(leftover_deck_set))
        else:
            return random.choice(self.deck)

    
    # Determine if a hand is a win. Will return 1-10 if it is a win (10 is the best winning hand, 1 is the worst winning hand), and 0 if it is a losing hand.
    def hand_is_win(self, player_hand: List(str), opponent_hands: List(str), flop_turn_river: List(str)):
        if self.is_royal_flush(player_hand, flop_turn_river):
            return 10
        elif self.is_straight_flush(player_hand, flop_turn_river):
            return 9
        elif self.is_four_of_a_kind(player_hand, flop_turn_river):
            return 8
        elif self.is_full_house(player_hand, flop_turn_river):
            return 7
        elif self.is_flush(player_hand, flop_turn_river):
            return 6
        elif self.is_straight(player_hand, flop_turn_river):
            return 5
        elif self.is_three_of_a_kind(player_hand, flop_turn_river):
            return 4
        elif self.is_two_pair(player_hand, flop_turn_river):
            return 3
        elif self.is_pair(player_hand, flop_turn_river):
            return 2
        elif self.is_high_card(player_hand, opponent_hands):
            return 1
        else:
            return 0
    

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
        # Return true if there is a straight and a flush occuring simultaneously, false otherwise
        return self.is_straight(player_hand, flop_turn_river) and self.is_flush(player_hand, flop_turn_river)
    

    # Determine if a player's hand is a 4-of-a-kind win, which is 4 cards of the same rank.
    # Example of a valid 4-of-a-kind win:
    #  player_hand: ["Jd", "Ts"]
    #  flop_turn_river: ["Th", "Td", "4s", "3s", "Tc"]
    #   player wins with Ts, Th, Td, Tc
    def is_four_of_a_kind(self, player_hand: List[str], flop_turn_river: List[str]) -> bool:
        # Get a list of all the cards in play (table and player's hand)
        hand_and_table_cards = player_hand + flop_turn_river

        # Create a dictionary to count the occurences of each rank
        rank_count = self.count_ranks(hand_and_table_cards)
        
        # Check if there is any rank with a count of 4 (indicating a four-of-a-kind)
        for count in rank_count.values():
            if count == 4:
                return True
        
        # Return false if no pair was found
        return False
    

    # Determine if a player's hand is a full house win, which is a three of a kind combined with a pair (eg. A,A,A,5,5). 
    # Ties on a full house are broken by the three of a kind, as you cannot have two equal sets of three of a kind in any single deck.
    # Example of a valid flush win:
    #  player_hand: ["5c", "Js"]
    #  flop_turn_river: ["5s", "Jh", "Jc", "Jd", "6d"]
    #   player wins with Js, Jh, Jc, 5c, 5s
    def is_full_house(self, player_hand: List[str], flop_turn_river: List[str]):
        # Get a list of all the cards in play (table and player's hand)
        hand_and_table_cards = player_hand + flop_turn_river

        # Count the occurences of each rank
        rank_count = self.count_ranks(hand_and_table_cards)

        # Initialize variables to track the three-of-a-kind and pair ranks
        three_of_a_kind_rank = None
        pair_rank = None

        # Iterate through the ranks and determine if there's a three-of-a-kind and a pair
        for rank, count in rank_count.items():
            if count == 3:
                three_of_a_kind_rank = rank
            elif count == 2:
                pair_rank = rank
        
        # Check if both a three-of-a-kind and a pair were found. Return True if so, False if not.
        if (three_of_a_kind_rank is not None) and (pair_rank is not None):
            return True
        return False


    # Determine if a player's hand is a flush win, which is any five card with the same suit. The high card determines the winner if two or more people have a flush.
    # Example of a valid flush win:
    #  player_hand: ["5c", "Js"]
    #  flop_turn_river: ["2s", "Ts", "7s", "4s", "6d"]
    #   player wins with 2s, 7s, 4s, Js, Ts
    def is_flush(self, player_hand: List[str], flop_turn_river: List[str]):
        # Get a list of all the cards in play (table and player's hand)
        hand_and_table_cards = player_hand + flop_turn_river

        # Extract all the suits from all cards
        hand_and_table_suits = self.get_suits(hand_and_table_cards)

        # Count the occurence of each suit and store it in the suit_count dictionary
        suit_count = self.count_suits(hand_and_table_suits)

        # Check if there are at least 5 cards with the same suit, return True if so
        for suit, count in suit_count.items():
            if count >= 5:
                return True
        
        # Return False if there aren't at least 5 cards with the same suit
        return False


    # Determine if a player's hand is a straight win, which is any five card with consecutive ranks.
    # Example of a valid straight win:
    #  player_hand: ["5c", "Js"]
    #  flop_turn_river: ["2s", "Qs", "3c", "4h", "6d"]
    #   player wins with 2s, 3c, 4h, 5c, 6d
    def is_straight(self, player_hand: List[str], flop_turn_river: List[str]):
        # Get a list of all the cards in play (table and player's hand)
        hand_and_table_cards = player_hand + flop_turn_river

        # Extract ranks from all cards
        hand_and_table_ranks = self.get_ranks(hand_and_table_cards)

        # Convert ranks to integers
        ranks_int = [self.rank_to_int(rank) for rank in hand_and_table_ranks]

        # Sort the ranks in ascending order
        sorted_ranks_int = sorted(ranks_int)

        # Check if there are five consecutive ranks
        consecutive_rank_count = 1 # Initialize the count to 1 to include the current card
        for i in range (1, len(sorted_ranks_int)):
            # If the previous rank + 1 is equal to the current rank, increment the consecutive rank counter.
            if sorted_ranks_int[i - 1] + 1 == sorted_ranks_int[i]:
                consecutive_rank_count += 1
                # If you have at least 5 consecutive ranks, return True
                if consecutive_rank_count >= 5:
                    return True
        
        # If you do not have at least 5 consecutive ranks, return False
        return False 
        

        # Check if the player's hand contains the required cards to win with a Royal Flush
        for suit in royal_flush_suits:
            # For this suit, generate a Royal Flush hand
            royal_flush_hand = set([rank + suit for rank in royal_flush_ranks])

            # If the royal flush hand exists within the player's hand set + the flop, turn, river set, return True
            if royal_flush_hand.issubset(player_hand_set.union(flop_turn_river_set)):
                return True
        
        # If no Royal Flush hand was found, return false
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
    # Example of a valid 2-pair win:
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


    # Determine if a player's hand has a higher ranking card than the opponents' hands
    def is_high_card(self, player_hand: List[str], opponent_hands: List[str]):
        highest_player_rank = 0
        for card_rank in self.get_ranks(player_hand):
            int_card_rank = self.rank_to_int(card_rank)

            if int_card_rank > highest_player_rank:
                highest_player_rank = int_card_rank
        
        highest_opponent_rank = 0
        for hand in opponent_hands:
            for card_rank in self.get_ranks(hand):
                int_card_rank = self.rank_to_int(card_rank)

            if int_card_rank > highest_opponent_rank:
                highest_player_rank = int_card_rank

        return True if highest_player_rank > highest_opponent_rank else False


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
    

    # Counts the occurence of each suit in a set of cards.
    # Example:
    #  Cards: ["Ts", "Td", "Ah", "3s", "4c", "Jd", "Td"]
    #  count_suits will return {("s", 2), ("d", 3), ("h", 1), ("c", 1)}
    def count_suits(self, cards: List[str]):

        # Create a dictionary to count the occurences of each suit
        suit_count = {}

        # Count the ranks in the player's hand and table
        for card in cards:
            suit = card[-1] # Gets the last element from the string, turning "9c" into "c"
            
            if suit in suit_count:
                suit_count[suit] += 1
            else:
                suit_count[suit] = 1
        
        # Return the rank_count dictionary
        return suit_count
            

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


    # Convert's a card's rank into an integer to assist in comparing the ranks of different cards.
    # Params:
    #   rank (str): Rank of a card. Examples: "K", "3", "A", "7", ...
    def rank_to_int(self, rank: str) -> int:
        # Define a mapping of ranks to their respective integer
        rank_mapping = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

        # Convert the rank string to an integer using the mapping
        return rank_mapping.get(rank, 0)  # 0 is returned if the rank is not recognized



      
myHoldemGame = TexasHoldemGame()
myHoldemGame.set_num_of_opponents(1)
myHoldemGame.set_player_hand(["As", "Th"])
myHoldemGame.set_num_of_sims(100000)

player_hand = ["3c", "9d"]
ftr = ["4c", "5c", "Kc", "9h", "6c"]
opponent_hands = ["Ah", "7s"]
print("Is Royal Flush: " + str(myHoldemGame.is_royal_flush(player_hand, ftr)))
print("Is Straight Flush: " + str(myHoldemGame.is_straight_flush(player_hand, ftr)))
print("Is Four of a Kind: " + str(myHoldemGame.is_four_of_a_kind(player_hand, ftr)))
print("Is Full House: " + str(myHoldemGame.is_full_house(player_hand, ftr)))
print("Is Flush: " + str(myHoldemGame.is_flush(player_hand, ftr)))
print("Is Straight: " + str(myHoldemGame.is_straight(player_hand, ftr)))
print("Is Three of a Kind: " + str(myHoldemGame.is_three_of_a_kind(player_hand, ftr)))
print("Is Two Pair: " + str(myHoldemGame.is_two_pair(player_hand, ftr)))
print("Is Pair: " + str(myHoldemGame.is_pair(player_hand, ftr)))

print("Is Winning Hand: " + str(myHoldemGame.hand_is_win(player_hand, opponent_hands, ftr)))