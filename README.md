# Blackjack-Game

A command-line implementation of the classic Blackjack card game in Python. Play against the computer dealer following standard Blackjack rules.

## Python Concepts Implemented

- **Lists and List Operations**: Card deck management and hand tracking
- **Random Module**: Using `random.choice()` for card selection
- **Functions**: Modular code organization with clear function definitions
- **Control Flow**: If-else statements and while loops for game logic
- **Type Conversion**: Converting strings to integers for score calculation
- **Input/Output**: User interaction through command-line interface
- **Boolean Logic**: Game state management and win conditions
- **Error Handling**: Input validation and game state verification

## Features

- Player vs Computer (Dealer) gameplay
- Standard deck of cards (Ace = 11 or 1)
- ASCII art interface
- Score tracking
- Option to play multiple rounds

## Game Rules

- Get as close to 21 as possible without going over
- Aces count as 11 (unless that would cause a bust, then they count as 1)
- Face cards (J, Q, K) count as 10
- Computer must draw cards until it has at least 17 points
- Natural blackjack (21 with first two cards) beats all other hands

## Project Structure

```
blackjack-game/
│
├── main.py      # Core game logic and main game loop
├── art.py       # ASCII art assets
└── README.md    # Documentation
```

## How to Run

```bash
python main.py
```

## Implementation Details

### Key Functions
- `deal_card()`: Returns a random card from the deck
- `calculate_score()`: Handles scoring logic including Ace values
- `compare()`: Determines the winner based on final scores
- `play_game()`: Controls the main game flow

### Dependencies
- Python 3.x
- No external libraries required

## Future Enhancements
- Add multiplayer support
- Implement card counting
- Add betting system
- Save game statistics
