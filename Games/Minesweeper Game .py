# 12/6/2023
# I had some spare time and I wanted to get better at tkinter. I made this Minesweeper game with dynamic difficulty (a player can choose how many rows, columns, and mines to have on their grid). 
# To run this, one needs to have a bomb and a flag png image for the icons.
# I learned how to balance logic and design and how to debug issues involving state management and interactions between game components. 

from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import random
import time

MINE = '*'
EMPTY = ' '
UNREVEALED = '-'

NUMBER_COLORS = {
    '1': 'blue',
    '2': 'green',
    '3': 'red',
    '4': 'purple',
    '5': 'orange',
    '6': 'pink',
    '7': 'yellow',
    '8': 'black',
}

class Minesweeper:
    def __init__(self, root, rows, cols, num_mines):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.grid = [[UNREVEALED for _ in range(cols)] for _ in range(rows)]
        self.mine_field = [[EMPTY for _ in range(cols)] for _ in range(rows)]
        self.flags = [[False for _ in range(cols)] for _ in range(rows)]
        self.game_over = False
        self.revealed_cells = 0
        self.best_time = None
        self.time_taken = 0
        self.start_time = 0
        self.time_update_id = None
        self.tile_size = None
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]
        self.setup_ui()

    def setup_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        available_width = self.root.winfo_screenwidth() - 100
        available_height = self.root.winfo_screenheight() - 100
        tile_width = available_width // self.cols
        tile_height = available_height // self.rows
        self.tile_size = min(tile_width, tile_height)
        self.mine_icon = self.resize_icon("bomb.png")
        self.flag_icon = self.resize_icon("flag.png")
        top_frame = tk.Frame(self.root)
        top_frame.pack(pady=10)
        self.time_label = tk.Label(top_frame, text="Time: 0  Best Time: No Best Time Yet", font=("Arial", 16), padx=10)
        self.time_label.pack(side=tk.RIGHT)
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)
        for r in range(self.rows):
            for c in range(self.cols):
                btn = tk.Button(self.frame, text="", width=self.tile_size // 10, height=self.tile_size // 25, relief="raised", bd=5, font=("Arial", 14), command=lambda r=r, c=c: self.reveal(r, c))
                btn.bind("<Button-3>", lambda event, r=r, c=c: self.toggle_flag(event, r, c))
                btn.grid(row=r, column=c, padx=1, pady=1)
                self.buttons[r][c] = btn
        self.root.geometry(f"{self.cols * self.tile_size + 30}x{self.rows * self.tile_size + 150}")
        self.initialize_game()

    def resize_icon(self, path):
        original_image = Image.open(path)
        resized_image = original_image.resize((self.tile_size - 5, self.tile_size - 5), Image.LANCZOS)
        return ImageTk.PhotoImage(resized_image)

    def initialize_game(self):
        self.grid = [[UNREVEALED for _ in range(self.cols)] for _ in range(self.rows)]
        self.mine_field = [[EMPTY for _ in range(self.cols)] for _ in range(self.rows)]
        self.flags = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        self.game_over = False
        self.revealed_cells = 0
        self.start_time = time.time()
        mine_positions = random.sample(range(self.rows * self.cols), self.num_mines)
        for pos in mine_positions:
            row = pos // self.cols
            col = pos % self.cols
            self.mine_field[row][col] = MINE
        for r in range(self.rows):
            for c in range(self.cols):
                if self.mine_field[r][c] != MINE:
                    self.mine_field[r][c] = str(self.count_adjacent_mines(r, c))
        self.update_time()

    def count_adjacent_mines(self, row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        mine_count = 0
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols and self.mine_field[nr][nc] == MINE:
                mine_count += 1
        return mine_count

    def update_time(self):
        if not self.game_over:
            elapsed_time = time.time() - self.start_time
            self.time_label.config(text=f"Time: {self.format_time(elapsed_time)}  Best Time: {self.format_time(self.best_time) if self.best_time else 'No Best Time Yet'}")
            self.time_update_id = self.root.after(1000, self.update_time)

    def format_time(self, time_in_seconds):
        minutes = int(time_in_seconds) // 60
        seconds = int(time_in_seconds) % 60
        return f"{minutes:02}:{seconds:02}"

    def reveal(self, row, col):
        if self.game_over or self.grid[row][col] != UNREVEALED or self.flags[row][col]:
            return
        self.grid[row][col] = self.mine_field[row][col]
        self.buttons[row][col].config(relief="sunken", state="disabled", text=self.grid[row][col], disabledforeground=NUMBER_COLORS.get(self.grid[row][col], "black"))
        self.revealed_cells += 1
        if self.mine_field[row][col] == MINE:
            self.buttons[row][col].config(image=self.mine_icon, compound="center")
            self.show_game_lost()
        elif self.mine_field[row][col] == '0':
            self.grid[row][col] = EMPTY
            self.buttons[row][col].config(text=EMPTY, state="disabled", relief="sunken")
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    self.reveal(nr, nc)
        if self.check_win():
            self.show_game_won()

    def check_win(self):
        correctly_flagged_mines = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if self.mine_field[r][c] == MINE and self.flags[r][c]:
                    correctly_flagged_mines += 1
                elif self.mine_field[r][c] != MINE and self.grid[r][c] == UNREVEALED:
                    return False 
        return correctly_flagged_mines == self.num_mines

    def show_game_won(self):
        self.game_over = True
        self.time_taken = time.time() - self.start_time
        if self.best_time is None or self.time_taken < self.best_time:
            self.best_time = self.time_taken
        best_time_message = f"Best Time: {self.format_time(self.best_time)}"
        messagebox.showinfo("Congratulations!", f"You've won the game!\n\n{best_time_message}")
        self.reset_game()

    def show_game_lost(self):
        self.game_over = True
        messagebox.showinfo("Game Over", "You hit a mine! Game over.")
        self.reset_game()

    def reset_game(self):
        if self.time_update_id:
            self.root.after_cancel(self.time_update_id)
        self.setup_ui()

    def toggle_flag(self, event, row, col):
        if self.game_over or self.grid[row][col] != UNREVEALED:
            return

        if self.flags[row][col]:
            self.flags[row][col] = False
            self.buttons[row][col].config(image="", text="", compound="none")
        else:
            self.flags[row][col] = True
            self.buttons[row][col].config(image=self.flag_icon, text="", compound="center")

        if self.check_win():
            self.show_game_won()

    def show_game_lost(self):
        self.game_over = True
        messagebox.showinfo("Game Over", "You hit a mine! Game over.")
        self.reset_game()

    def show_game_won(self):
        self.game_over = True
        self.time_taken = time.time() - self.start_time
        if self.best_time is None or self.time_taken < self.best_time:
            self.best_time = self.time_taken
        best_time_message = f"Best Time: {self.format_time(self.best_time)}"
        messagebox.showinfo("Congratulations!", f"You've won the game!\n\n{best_time_message}")
        self.reset_game()

    def reveal(self, row, col):
        if self.game_over or self.grid[row][col] != UNREVEALED or self.flags[row][col]:
            return
        self.grid[row][col] = self.mine_field[row][col]
        self.buttons[row][col].config(relief="sunken", state="disabled", text=self.grid[row][col], disabledforeground=NUMBER_COLORS.get(self.grid[row][col], "black"))
        self.revealed_cells += 1
        if self.mine_field[row][col] == MINE:
            self.buttons[row][col].config(image=self.mine_icon, compound="center")
            self.show_game_lost()
        elif self.mine_field[row][col] == '0':
            self.grid[row][col] = EMPTY
            self.buttons[row][col].config(text=EMPTY, state="disabled", relief="sunken")
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    self.reveal(nr, nc)
        if self.check_win():
            self.show_game_won()

    def check_win(self):
        correctly_flagged_mines = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if self.mine_field[r][c] == MINE and self.flags[r][c]:
                    correctly_flagged_mines += 1
                elif self.mine_field[r][c] != MINE and self.grid[r][c] == UNREVEALED:
                    return False
        return correctly_flagged_mines == self.num_mines

class StartWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Minesweeper Game")
        self.setup_ui()

    def setup_ui(self):
        self.rows_label = tk.Label(self.root, text="Enter number of rows:")
        self.rows_label.pack(pady=5)
        self.rows_entry = tk.Entry(self.root)
        self.rows_entry.pack(pady=5)

        self.cols_label = tk.Label(self.root, text="Enter number of columns:")
        self.cols_label.pack(pady=5)
        self.cols_entry = tk.Entry(self.root)
        self.cols_entry.pack(pady=5)

        self.mines_label = tk.Label(self.root, text="Enter number of mines:")
        self.mines_label.pack(pady=5)
        self.mines_entry = tk.Entry(self.root)
        self.mines_entry.pack(pady=5)

        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=20)

    def start_game(self):
        rows = int(self.rows_entry.get())
        cols = int(self.cols_entry.get())
        num_mines = int(self.mines_entry.get())

        game_window = tk.Toplevel(self.root)
        game = Minesweeper(game_window, rows, cols, num_mines)
        self.root.withdraw()

if __name__ == "__main__":
    root = tk.Tk()
    start_window = StartWindow(root)
    root.mainloop()
