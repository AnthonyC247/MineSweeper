#Board-Creation

import random
import tkinter as tk
from tkinter import messagebox

class MinesweeperGUI:
    def __init__(self, rows, cols, num_mines):
        """
        Start the Minesweeper game GUI.

        Parameters:
            rows (int): Number of rows in the game grid.
            cols (int): Number of columns in the game grid.
            num_mines (int): Number of mines to be placed in the game grid.
        """
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.total_cells = rows * cols
        self.remaining_cells = self.total_cells - num_mines
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.uncovered = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.mines = set()

        self.root = tk.Tk()
        self.root.title("Minesweeper")
        
        self.create_board()
        self.place_mines()
        self.calculate_counts()

        self.game_over = False

    def create_board(self):
        """
        Create the game board with buttons for each cell in the grid.
        """
        self.buttons = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                button = tk.Button(
                    self.root,
                    width=2,
                    height=1,
                    font=('Arial', 12),
                    command=lambda r=row, c=col: self.on_cell_left_click(r, c)
                )
                button.grid(row=row, column=col)
                button.bind('<Button-3>', lambda event, r=row, c=col: self.on_cell_right_click(event, r, c))
                self.buttons[row][col] = button