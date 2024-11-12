import random

shapes = ["CIRCLE", "SQUARE", "TRIANGLE", "STAR", "CROSS"]
numbers = [1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14]
special_number = 20

# create_deck function creates a deck of cards. Each card is represented by a tuple with a shape and a number.
# Special 'number 20' cards without a shape are added at the end. The deck is then shuffled.
def create_deck():
    deck = []
    for shape in shapes:
        for number in numbers:
            # Skip 'STAR' cards with numbers 10, 11, 12, 13, and 14
            if shape == "STAR" and number in [10, 11, 12, 13, 14]:
                continue
            deck.append((shape, number))
    
    # Add the special 'number 20' cards without shape
    for _ in range(5):
        deck.append((None, special_number))
    
    # Shuffle the deck to randomize the order of cards
    random.shuffle(deck)
    return deck

# give_cards function distributes cards to the players. 
# It removes cards from the deck and gives 5 cards to each player.
def give_cards(deck, num_cards=5):
    # Player 1 and Player 2 each get 5 cards from the deck.
    # The function goes through the deck and gives each player one card at a time until they both have 5 cards.
    player1 = [deck.pop() for _ in range(num_cards)]
    player2 = [deck.pop() for _ in range(num_cards)]
    return player1, player2, deck

# show_hands function returns a readable list of cards in the player's hand.
# Each card is displayed as a string with the shape and number, or '20' for cards with no shape.
def show_hands(player):
    return [f"{shape or '20'} {number}" for shape, number in player]

# is_valid_play function checks if a card can be legally played on top of the current card on the table.
# A card is valid if it has the same shape or number, or if it is a special 'number 20' card.
def is_valid_play(card, current_card):
    shape, number = card
    current_shape, current_number = current_card
    return shape == current_shape or number == current_number or number == special_number

# play_game function simulates the game loop.
# Players take turns playing cards, and the game continues until a break condition is met.
def play_game():
    # Create a deck of cards and shuffle them
    deck = create_deck()
    
    # Deal initial cards to the players; 'market' holds the remaining cards in the deck
    player1, player2, market = give_cards(deck)
    
    # Remove the last card from the deck and place it on the table as the starting card
    table_card = deck.pop()
    
    # List of players in the game
    players = [player1, player2]
    
    # Set player 1 to start the game
    player_turn = 0
    
    # Create an infinite loop that will continue until a break condition is met
    while True:
        # Select the current player's hand based on whose turn it is
        player = players[player_turn]
        
        # Display the current turn and the card on the table
        print(f"\nPlayer {player_turn + 1}'s turn. Table Card: {table_card[0] or '20'} {table_card[1]}")
        
        # Show the current player’s hand in a readable format
        print("Your hand:", show_hands(player))
        
        # Check each card in the player's hand and see if it matches the current table card
        # (by either shape, number, or any special condition). If it matches, add it to playable_cards.
        playable_cards = [card for card in player if is_valid_play(card, table_card)]
        
        # Check if there are any valid cards in the player's hand that can be played
        if playable_cards:
            played_card = playable_cards[0]
            # Select the first valid card from playable_cards and assign it to played_card
            player.remove(played_card)
            # Remove the card the player just played from their hand
            
            table_card = played_card
            # Update the table with the card that the player just played
            
            print(f"Player {player_turn + 1} played: {played_card[0] or '20'} {played_card[1]}")
            # Print a message showing the card the player played (shape and number)
            
            # Check if the player's hand is empty (meaning they have played all their cards)
            if not player:
                # Print a message that the current player has won by playing all their cards
                print(f"\nPlayer {player_turn + 1} wins by playing all cards")
                # Exit the game loop to end the game, as we have a winner
                break
            
        else:
            # If the player has no playable cards:
            if market:
                # Take the top card from the market pile (last card in the market list)
                drawn_card = market.pop()
                
                # Add the drawn card to the player's hand
                player.append(drawn_card)
                
                # Display a message indicating the player has drawn a card from the market
                print(f"Player {player_turn + 1} draws from market: {drawn_card[0] or '20'} {drawn_card[1]}")
            else:
                # If the market deck is empty (no cards left to draw)
                print("Market is empty")

        # Check if the game should end due to no moves being possible
        if not market and all(not is_valid_play(card, table_card) for card in player):
            # If the market is empty and the player has no valid moves (no playable card in hand)
            print("Game over! No more moves possible.")
            # End the game by breaking out of the loop
            break

        # Switch turns to the other player
        player_turn = 1 - player_turn

        
play_game()
