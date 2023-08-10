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
        self.root.title("MineSweeper")
        
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

    def place_mines(self):
        """
        Randomly place the specified number of mines on the game grid.
        """
        self.mines = set()
        available_cells = [(row, col) for row in range(self.rows) for col in range(self.cols)]
        random.shuffle(available_cells)
        mine_cells = available_cells[:self.num_mines]
        self.mines.update(mine_cells)

    def calculate_counts(self):
        """
        Calculate the number of adjacent mines for each cell in the game grid.
        """
        for row in range(self.rows):
            for col in range(self.cols):
                if (row, col) not in self.mines:
                    count = 0
                    for r in range(row - 1, row + 2):
                        for c in range(col - 1, col + 2):
                            if (r, c) in self.mines:
                                count += 1
                    self.board[row][col] = str(count) if count > 0 else ' '

    def on_cell_left_click(self, row, col):
        """
        Handle left-click event on a cell.

        Parameters:
            row (int): Row index of the clicked cell.
            col (int): Column index of the clicked cell.
        """
        if self.game_over:
            return

        if (row, col) in self.mines:
            self.buttons[row][col].config(text='X', bg='red')
            self.show_all_mines()
            messagebox.showinfo("Game Over", "You hit a mine! Game over.")
            self.game_over = True
        elif self.uncovered[row][col] == ' ':
            self.uncover_cell(row, col)
            self.buttons[row][col].config(text=self.board[row][col], relief=tk.SUNKEN)
            self.remaining_cells -= 1

            if self.remaining_cells == 0:
                self.show_all_mines()
                messagebox.showinfo("Congratulations!", "You won the game!")
                self.game_over = True

    def on_cell_right_click(self, event, row, col):
        """
        Handle right-click event on a cell.

        Parameters:
            event: The right-click event object.
            row (int): Row index of the clicked cell.
            col (int): Column index of the clicked cell.
        """
        if self.game_over:
            return

        if self.uncovered[row][col] == ' ':
            self.uncovered[row][col] = 'F'
            self.buttons[row][col].config(text='F', fg='red')
        elif self.uncovered[row][col] == 'F':
            self.uncovered[row][col] = ' '
            self.buttons[row][col].config(text='', fg='black')

    def uncover_cell(self, row, col):
        """
        Recursively uncover the cell and adjacent cells if they are empty.

        Parameters:
            row (int): Row index of the cell to uncover.
            col (int): Column index of the cell to uncover.
        """
        if self.uncovered[row][col] != ' ':
            return

        self.uncovered[row][col] = self.board[row][col]
        if self.board[row][col] == ' ':
            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    if 0 <= r < self.rows and 0 <= c < self.cols:
                        self.uncover_cell(r, c)

    def show_all_mines(self):
        """
        Show all the mines on the game grid.
        """
        for row, col in self.mines:
            self.buttons[row][col].config(text='X', bg='red')

    def display_grid(self):
        """
        Display the current state of the game grid in the command-line interface.
        """
        for row in range(self.rows):
            for col in range(self.cols):
                if self.uncovered[row][col] != ' ':
                    print(f' {self.uncovered[row][col]} ', end='')
                else:
                    print(' - ', end='')
            print()

    def run(self):
        """
        Run the game GUI main loop.
        """
        self.root.mainloop()


def play_game():
    """
    Play the Minesweeper game.
    """
    print("Welcome to Minesweeper!")
    print("Uncover cells to find all non-mine cells.")
    print("Be careful not to uncover a mine!")
    print("Flag suspected mine cells to mark them.")

    difficulty = get_input_difficulty()
    rows, cols, num_mines = get_difficulty_settings(difficulty)

    game = MinesweeperGUI(rows, cols, num_mines)
    game.display_grid()
    game.run()


def get_input_int(message, limit=None):
    """
    Get an integer input from the user.

    Parameters:
        message (str): The input prompt message.
        limit (int): The upper limit for the input value (default: None).

    Returns:
        int: The input integer value.
    """
    while True:
        try:
            value = int(input(message))
            if limit is not None and (value < 0 or value >= limit):
                raise ValueError
            return value
        except ValueError:
            print('Invalid input. Please enter a valid integer.')


def get_input_difficulty():
    """
    Prompt the user to select the difficulty level.

    Returns:
        int: The selected difficulty level.
    """
    while True:
        print("\n[Difficulty Levels]")
        print("1: Easy")
        print("2: Medium")
        print("3: Hard")
        difficulty = get_input_int("Enter the difficulty level: ")
        if difficulty in [1, 2, 3]:
            return difficulty
        print('Invalid difficulty level. Please choose a valid level.')


def get_difficulty_settings(difficulty):
    """
    Get the game grid size and number of mines based on the selected difficulty level.

    Parameters:
        difficulty (int): The selected difficulty level.

    Returns:
        tuple: The game grid size (rows, cols) and number of mines.
    """
    if difficulty == 1:
        return 8, 8, 10
    elif difficulty == 2:
        return 12, 12, 25
    elif difficulty == 3:
        return 16, 16, 40


def main():
    """
    Main entry point of the program.
    """
    play_game()


if __name__ == '__main__':
    main()
