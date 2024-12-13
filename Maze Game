# 9/20/2023
# Tried out Tkinter by making this maze game. There is a lot of potential here, maybe even making it into a real, commercial game. The only purpose here was to get better at game interfaces and at structure generation.

import tkinter as tk
import random
import time

TILE_SIZE = 20
GRID_WIDTH = 120
GRID_HEIGHT = 80
WIDTH = TILE_SIZE * GRID_WIDTH
HEIGHT = TILE_SIZE * GRID_HEIGHT
MAPS = ["Random", "Maze1", "Maze2"]
DIFFICULTY_SETTINGS = {
    "Easy": {"width": 40, "height": 30},
    "Medium": {"width": 60, "height": 50},
    "Hard": {"width": 80, "height": 60},
}

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

WHITE = "#FFFFFF"
BLACK = "#1a1a1a"
NEON_GREEN = "#39FF14"
NEON_BLUE = "#00FFFF"
NEON_PURPLE = "#8A2BE2"
DARK_GRAY = "#121212"

player_x, player_y = None, None
player_size = TILE_SIZE
speed = 1
start_time = None
best_time = None
maze = []
start_pos = None
end_pos = None
difficulty = "Medium"
current_map = "Random"
current_state = "TITLE_SCREEN"

root = tk.Tk()
root.title("Maze Game")
root.geometry(f"{WIDTH}x{HEIGHT}")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=DARK_GRAY)
canvas.pack()

def generate_maze():
    global maze, player_x, player_y, start_pos, end_pos
    width = DIFFICULTY_SETTINGS[difficulty]["width"]
    height = DIFFICULTY_SETTINGS[difficulty]["height"]
    maze = [[1 for _ in range(width)] for _ in range(height)]

    start_x, start_y = random.randint(1, width - 2), random.randint(1, height - 2)
    end_x, end_y = random.randint(1, width - 2), random.randint(1, height - 2)

    def dfs(x, y):
        maze[y][x] = 0
        random.shuffle(DIRECTIONS)
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 < nx < width and 0 < ny < height and maze[ny][nx] == 1:
                maze[ny][nx] = 0
                maze[y + dy][x + dx] = 0 
                dfs(nx, ny)

    dfs(start_x, start_y)
    player_x, player_y = start_x, start_y
    start_pos = (start_x, start_y)
    end_pos = (end_x, end_y)

def draw_maze():
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 1:
                canvas.create_rectangle(x * TILE_SIZE, y * TILE_SIZE, (x + 1) * TILE_SIZE, (y + 1) * TILE_SIZE, fill=BLACK)
            elif maze[y][x] == 0:
                canvas.create_rectangle(x * TILE_SIZE, y * TILE_SIZE, (x + 1) * TILE_SIZE, (y + 1) * TILE_SIZE, fill=WHITE)

    if start_pos:
        sx, sy = start_pos
        canvas.create_rectangle(sx * TILE_SIZE, sy * TILE_SIZE, (sx + 1) * TILE_SIZE, (sy + 1) * TILE_SIZE, fill=NEON_GREEN)
    if end_pos:
        ex, ey = end_pos
        canvas.create_rectangle(ex * TILE_SIZE, ey * TILE_SIZE, (ex + 1) * TILE_SIZE, (ey + 1) * TILE_SIZE, fill=NEON_BLUE)

def draw_player(x, y):
    canvas.create_rectangle(x * TILE_SIZE, y * TILE_SIZE, (x + 1) * TILE_SIZE, (y + 1) * TILE_SIZE, fill=NEON_PURPLE)

def display_time(time_seconds):
    canvas.create_text(20, 20, text=f"Time: {time_seconds:.2f}s", anchor="nw", fill=NEON_GREEN, font=("Courier", 18))

def display_best_time():
    best_time_text = f"Best Time: {best_time:.2f}s" if best_time is not None else "Best Time: N/A"
    canvas.create_text(WIDTH - 20, 20, text=best_time_text, anchor="ne", fill=NEON_BLUE, font=("Courier", 18))

def reset_game():
    global player_x, player_y, start_time, start_pos, end_pos
    generate_maze()
    start_time = time.time()

def move_player(event):
    global player_x, player_y
    if event.keysym == 'Left' and maze[player_y][player_x - 1] != 1:
        player_x -= speed
    if event.keysym == 'Right' and maze[player_y][player_x + 1] != 1:
        player_x += speed
    if event.keysym == 'Up' and maze[player_y - 1][player_x] != 1:
        player_y -= speed
    if event.keysym == 'Down' and maze[player_y + 1][player_x] != 1:
        player_y += speed

def draw_title_screen():
    canvas.delete("all")
    canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="black", outline="black")
    canvas.create_text(WIDTH // 2, HEIGHT // 4, text="MAZE GAME", font=("Arial", 60, "bold"), fill=NEON_GREEN, tags="title")
    canvas.create_text(WIDTH // 2, HEIGHT // 2, text=f"Difficulty: {difficulty}", font=("Arial", 24, "bold"), fill=NEON_PURPLE, tags="difficulty")
    canvas.create_text(WIDTH // 2, HEIGHT // 2 + 40, text="Press Enter to Start", font=("Arial", 30, "italic"), fill=NEON_BLUE, tags="instructions")
    canvas.after(500, animate_title_glow)

def animate_title_glow():
    canvas.itemconfig("title", fill=NEON_GREEN if random.random() > 0.5 else NEON_BLUE)
    canvas.after(500, animate_title_glow)  # Repeat animation

def start_game():
    global current_state
    reset_game()
    current_state = "GAME_SCREEN"
    root.bind("<KeyPress>", move_player)

def game_loop():
    global current_state, player_x, player_y, start_time, best_time
    canvas.delete("all")
    
    if current_state == "TITLE_SCREEN":
        draw_title_screen()
    elif current_state == "GAME_SCREEN":
        if player_x is None or player_y is None:
            return
        draw_maze()
        draw_player(player_x, player_y)

        if start_time is None:
            start_time = time.time()

        elapsed_time = time.time() - start_time
        display_time(elapsed_time)
        display_best_time()

        if player_x == end_pos[0] and player_y == end_pos[1]:
            if best_time is None or elapsed_time < best_time:
                best_time = elapsed_time
            start_time = None
            reset_game()

    root.after(50, game_loop)  # Update every 50ms

def handle_title_screen_key(event):
    global current_state
    if event.keysym == 'Return':
        start_game()

root.bind("<KeyPress>", handle_title_screen_key)

root.after(50, game_loop)
root.mainloop()
