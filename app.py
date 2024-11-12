import random

# Step 1: Define the features of each cell type
features = {
    "monster": "Monster",
    "trap": "Trap",
    "treasure": "Treasure",
    "empty": "Empty"
}

# Step 2: Define each card type and description
card_types = {
    "move_forward": "Move Forward - Allows the player to move one cell forward.",
    "jump": "Jump - Allows the player to jump over one cell.",
    "attack": "Attack - Defeats a monster in the player's path.",
    "trap_avoidance": "Trap Avoidance - Lets the player avoid a trap.",
    "treasure": "Treasure - Grants a bonus or points."
}

# Step 3: Create a deck with multiple copies of each card type
deck = (
    ["move_forward"] * 10 +
    ["jump"] * 5 +
    ["attack"] * 5 +
    ["trap_avoidance"] * 3 +
    ["treasure"] * 2
)
random.shuffle(deck)

# Step 4: Initialize the 5x5 dungeon grid with random features
grid_size = 5
dungeon_grid = []
for i in range(grid_size):
    row = []
    for j in range(grid_size):
        cell_feature = random.choice(list(features.values()))
        row.append(cell_feature)
    dungeon_grid.append(row)

# Set start and end points
dungeon_grid[0][0] = "Start"
dungeon_grid[grid_size-1][grid_size-1] = "Exit"

# Step 5: Initialize player position at the top-left corner
player_position = [0, 0]

# Function to draw a card from the deck
def draw_card(deck):
    if deck:
        return deck.pop()
    else:
        print("The deck is empty!")
        return None

# Function to show card description
def show_card(card):
    if card:
        print(f"You drew a card: {card_types[card]}")

# Function to check if the card can be used based on the current cell type
def play_card(card, current_cell):
    if card == "move_forward" and current_cell != "Exit":
        print("You move forward by one cell.")
        return True
    elif card == "jump" and current_cell != "Exit":
        print("You jump over a cell.")
        return True
    elif card == "attack" and current_cell == "Monster":
        print("You defeated the monster!")
        return True
    elif card == "trap_avoidance" and current_cell == "Trap":
        print("You avoided the trap!")
        return True
    elif card == "treasure" and current_cell == "Treasure":
        print("You collected a treasure!")
        return True
    else:
        print("The card cannot be used right now.")
        return False

# Function to move player based on the card effect
def move_player(card):
    if card == "move_forward":
        player_position[1] += 1  # Move right
    elif card == "jump":
        player_position[1] += 2  # Jump two cells forward

# Main game loop
while True:
    # Display current position and cell type
    row, col = player_position
    current_cell = dungeon_grid[row][col]
    print(f"\nYou are at position {player_position} (Cell: {current_cell})")

    # Check for victory condition
    if current_cell == "Exit":
        print("Congratulations! You reached the exit and won the game!")
        break

    # Draw a card and show it
    card = draw_card(deck)
    if not card:
        print("Game over! The deck is empty.")
        break
    show_card(card)

    # Try to play the card
    if play_card(card, current_cell):
        move_player(card)  # Update player position if card was used

    # Check if player went out of grid bounds, and correct it
    if player_position[1] >= grid_size:
        player_position[1] = grid_size - 1
        player_position[0] += 1  # Move down a row
