# MineSweeper

Welcome to MineSweeper! This is a simple implementation of the classic MineSweeper game in Python, using the Tkinter GUI framework.

## Description

MineSweeper is a game where you uncover cells on a grid, trying to avoid hidden mines. The goal is to uncover all non-mine cells without hitting a mine. You can flag suspected mine cells to help with your strategy.

## Algorithms Used

The MineSweeper game utilizes the following algorithms:

1. **Randomized Mine Placement:** The mines are randomly placed on the game grid to provide a different game experience each time.

2. **Counting Adjacent Mines:** When a mine is not present in a cell, the algorithm counts the number of adjacent cells that contain mines and displays the count on the uncovered cells.

3. **Recursive Uncovering:** When an empty cell (with no adjacent mines) is uncovered, the algorithm recursively uncovers adjacent empty cells until reaching cells with adjacent mines.

## Required Libraries

This program requires Tkinter. If you need to install this library, run the following command in terminal:

```pip install tkinter```

## Getting Started

To play the MineSweeper game, follow these steps:

1. Clone the repository or download the code files.

2. Install Python if you haven't already (version 3 or above).

3. Install the required dependencies:


4. Run the game by executing the following command:
   ```python MineSweeper.py```


5. Choose the difficulty level (Easy, Medium, or Hard) when prompted.

6. Interact with the game grid using left-click to uncover cells and right-click to flag potential mines.

7. Continue playing until you either uncover all non-mine cells or hit a mine.

## Game Controls

- Left-click on a cell to uncover it.
- Right-click on a cell to flag or unflag it as a potential mine.

## Difficulty Levels

The game offers three difficulty levels:

1. Easy: 8x8 grid with 10 mines.
2. Medium: 12x12 grid with 25 mines.
3. Hard: 16x16 grid with 40 mines.
