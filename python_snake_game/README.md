# Python Snake Game

A classic Snake game implementation using Python and Pygame.

## Features
- Classic snake gameplay
- Score tracking
- Collision detection (walls and self)
- Responsive controls

## Requirements
- Python 3.7 or higher
- Pygame 2.6.1

## Installation

1. Clone or download this repository
2. Navigate to the `python_snake_game` directory
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## How to Play

### Method 1: Using the provided scripts (Recommended)
- On Windows: Double-click `run_game.bat`
- On Linux/Mac: Run `./run_game.sh` in the terminal

### Method 2: Manual installation
1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the game:
   ```
   python main.py
   ```

3. Controls:
   - Arrow keys to move the snake
   - Close the window to exit the game

## Game Rules

- Control the snake to eat the red food
- Each food item increases your score by 1
- The snake grows longer each time it eats food
- The game ends if the snake hits the wall or itself
- Try to get the highest score possible!

## Implementation Details

The game consists of three main classes:
1. `Snake` - Handles the snake's movement, drawing, and collision detection
2. `Food` - Manages the food's position and drawing
3. `Game` - Controls the overall game logic, scoring, and game over conditions

The game runs at 60 FPS with the snake moving at a speed of 10 cells per second.