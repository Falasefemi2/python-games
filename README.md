<!-- @format -->

Project: Dungeon Escape Card Game
Game Overview

In this game, two players (or a player vs. computer) will take turns drawing cards and moving through a dungeon grid, where each cell represents a different challenge or action. Players must play cards to advance through the dungeon, avoid traps, and reach the exit first to win.
Key Features to Implement

    Dungeon Setup
        The dungeon is represented as a 5x5 grid (or larger if you want more complexity).
        Each cell in the grid could have different features, like monsters, traps, or treasures.
        Players start at the top-left corner and must reach the bottom-right corner.

    Cards and Deck
        Create a deck of cards, each with different effects:
            Move Forward: Allows the player to move one step forward.
            Jump: Allows the player to jump over one cell.
            Attack: Lets the player fight off monsters encountered in a dungeon cell.
            Trap Avoidance: Allows the player to skip a trap cell.
            Treasure: Grants points or power-ups.
        Special cards could allow unique actions, like healing or extra moves.

    Card Play Rules
        Players take turns drawing and playing cards.
        Each turn, a player draws a card and decides if they can or should use it, depending on the dungeon layout and obstacles in their path.

    Dungeon Obstacles
        Place various obstacles on random cells in the dungeon:
            Monster cells: Require an Attack card to pass.
            Trap cells: Require a Trap Avoidance card to avoid losing a turn.
            Treasure cells: Grant a reward, like a bonus card draw or extra movement.
        Cells could also be empty, allowing free movement.

    Winning the Game
        The first player to reach the bottom-right corner of the grid (the dungeon exit) wins the game.

Technical Requirements

    Deck and Card Management
        Create functions to initialize a deck, shuffle it, draw cards, and manage players’ hands.
        Implement logic to handle each card's effect when played.

    Dungeon Grid and Navigation
        Set up the dungeon as a 5x5 list of lists, each with its specific cell type (monster, trap, treasure, or empty).
        Track players' current positions on the grid.
        Create logic for moving players based on card effects and grid obstacles.

    Turn-Based Gameplay Loop
        Implement a game loop that alternates between players, allowing each to draw, play cards, and make moves until one player reaches the dungeon exit.

    Game Display
        Display the dungeon grid and players' current positions.
        Show each player's current hand and cards they’ve drawn.
        Display any obstacles in the cells when players move.

    Victory Condition
        Check each turn if a player has reached the exit and declare a winner.

Practice Questions

    If and For Statements
        Write a function even_numbers that takes a list of numbers and returns a list of only the even numbers using a for loop and an if statement.

    range() and break / continue Statements
        Write a for loop using range(10) to print numbers from 0 to 9. Modify it to skip printing the number 5 using continue and stop the loop if it reaches 8 using break.

    Else Clauses on Loops
        Write a loop to search for a number 5 in a list. If found, print "Found 5!" and break the loop. If the loop completes without finding it, print "5 is not in the list."

    Defining Functions with Default Arguments
        Write a function greet that takes a name and an optional greeting. If no greeting is provided, it should default to "Hello".

    Keyword-Only Arguments
        Write a function display_info that requires name as a positional argument but accepts age only as a keyword argument.

    Lambda Expression
        Write a lambda function that takes two numbers and returns their product. Use it in a simple print statement to show it works.

    Documentation Strings
        Write a function add that adds two numbers. Add a docstring explaining what the function does.

    Function Annotations
        Write a function multiply with annotations that take two integers and return their product as an integer.
