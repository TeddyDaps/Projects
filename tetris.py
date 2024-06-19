<<<<<<< HEAD
import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
import pygame
import random
import ttkbootstrap as tb

# Database setup
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tetris_db"
)
cursor = db.cursor()

# Tetris Game Configuration
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [(0, 255, 255), (0, 0, 255), (255, 165, 0), (255, 255, 0), (0, 255, 0), (160, 32, 240), (255, 0, 0)]
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]]
]

# Level configurations
LEVELS = {
    "Easy": 3,
    "Medium": 5,
    "Hard": 8,
    "Expert": 10
}

class Tetris:
    def __init__(self, user_id, level):
        self.user_id = user_id
        self.level = level
        self.screen = pygame.display.set_mode((300, 600))
        pygame.display.set_caption('Tetris')
        self.grid = [[0 for _ in range(10)] for _ in range(20)]
        self.current_shape = self.get_random_shape()
        self.current_shape_color = random.choice(COLORS)
        self.current_pos = [0, 10 // 2 - len(self.current_shape[0]) // 2]
        self.score = 0
        self.game_over = False

    def get_random_shape(self):
        return random.choice(SHAPES)

    def draw_grid(self):
        for row in range(20):
            for col in range(10):
                pygame.draw.rect(self.screen, WHITE if self.grid[row][col] == 0 else COLORS[self.grid[row][col] - 1],
                                 (col * 30, row * 30, 30, 30))
                pygame.draw.rect(self.screen, BLACK, (col * 30, row * 30, 30, 30), 1)

    def draw_shape(self):
        for row_idx, row in enumerate(self.current_shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, self.current_shape_color,
                                     ((self.current_pos[1] + col_idx) * 30, (self.current_pos[0] + row_idx) * 30, 30, 30))
                    pygame.draw.rect(self.screen, BLACK,
                                     ((self.current_pos[1] + col_idx) * 30, (self.current_pos[0] + row_idx) * 30, 30, 30), 1)

    def can_move(self, delta_row, delta_col):
        for row_idx, row in enumerate(self.current_shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    new_row, new_col = self.current_pos[0] + row_idx + delta_row, self.current_pos[1] + col_idx + delta_col
                    if new_row >= 20 or new_col < 0 or new_col >= 10 or (new_row >= 0 and self.grid[new_row][new_col] != 0):
                        return False
        return True

    def place_shape(self):
        for row_idx, row in enumerate(self.current_shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    self.grid[self.current_pos[0] + row_idx][self.current_pos[1] + col_idx] = COLORS.index(self.current_shape_color) + 1
        self.clear_lines()
        self.current_shape = self.get_random_shape()
        self.current_shape_color = random.choice(COLORS)
        self.current_pos = [0, 10 // 2 - len(self.current_shape[0]) // 2]
        if not self.can_move(0, 0):
            self.save_score()
            self.game_over = True

    def clear_lines(self):
        new_grid = [row for row in self.grid if any(cell == 0 for cell in row)]
        cleared_lines = 20 - len(new_grid)
        self.score += cleared_lines
        self.grid = [[0 for _ in range(10)] for _ in range(cleared_lines)] + new_grid

    def move_shape(self, delta_row, delta_col):
        if self.can_move(delta_row, delta_col):
            self.current_pos[0] += delta_row
            self.current_pos[1] += delta_col
        elif delta_row:
            self.place_shape()

    def rotate_shape(self):
        new_shape = list(zip(*self.current_shape[::-1]))
        if all(self.can_move(row_idx, col_idx) for row_idx, row in enumerate(new_shape) for col_idx, cell in enumerate(row) if cell):
            self.current_shape = new_shape

    def save_score(self):
        cursor.execute("INSERT INTO leaderboard (user_id, score) VALUES (%s, %s)", (self.user_id, self.score))
        db.commit()

    def run(self):
        clock = pygame.time.Clock()
        while not self.game_over:
            self.screen.fill(BLACK)
            self.draw_grid()
            self.draw_shape()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.move_shape(0, -1)
                    elif event.key == pygame.K_RIGHT:
                        self.move_shape(0, 1)
                    elif event.key == pygame.K_DOWN:
                        self.move_shape(1, 0)
                    elif event.key == pygame.K_SPACE:  # Changed from K_UP to K_SPACE for rotation
                        self.rotate_shape()
            self.move_shape(1, 0)
            clock.tick(self.level)  # Adjust tick rate based on selected level

# GUI for Login, Registration, Leaderboard, Account Deletion, and Level Selection
def register_user():
    username = entry_username.get()
    password = entry_password.get()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        messagebox.showinfo("Registration", "User registered successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", str(err))

def login_user():
    username = entry_username.get()
    password = entry_password.get()
    cursor.execute("SELECT id FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    if user:
        messagebox.showinfo("Login", "Login successful!")
        root.destroy()  # Close the login window
        level = level_var.get()  # Get selected level from dropdown
        Tetris(user_id=user[0], level=LEVELS[level]).run()  # Start the Tetris game with selected level
    else:
        messagebox.showerror("Error", "Invalid credentials")

def delete_account():
    username = entry_username.get()
    password = entry_password.get()
    cursor.execute("DELETE FROM users WHERE username = %s AND password = %s", (username, password))
    db.commit()
    messagebox.showinfo("Account Deletion", "Account deleted successfully")

def show_leaderboard():
    cursor.execute("SELECT users.username, leaderboard.score FROM leaderboard JOIN users ON leaderboard.user_id = users.id ORDER BY leaderboard.score DESC")
    scores = cursor.fetchall()
    leaderboard_window = tk.Toplevel(root)
    leaderboard_window.title("Leaderboard")
    for idx, (username, score) in enumerate(scores, start=1):
        tk.Label(leaderboard_window, text=f"{idx}. {username}: {score}").pack()

# Main application window
root = tb.Window(themename="darkly")
root.title("Tetris Login")

# Configure styles
style = tb.Style()
style.configure("TButton", font=("Helvetica", 12))
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))

# Username label and entry
tk.Label(root, text="Username").pack(pady=10)
entry_username = ttk.Entry(root, width=30)
entry_username.pack(pady=5)

# Password label and entry
tk.Label(root, text="Password").pack(pady=10)
entry_password = ttk.Entry(root, show="*", width=30)
entry_password.pack(pady=5)

# Level Selection
tk.Label(root, text="Select Level:").pack(pady=10)
level_var = tk.StringVar(root)
level_dropdown = ttk.Combobox(root, textvariable=level_var, values=list(LEVELS.keys()))
level_dropdown.pack()

# Buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=20)

ttk.Button(button_frame, text="Login", command=login_user).grid(row=0, column=0, padx=5)
ttk.Button(button_frame, text="Register", command=register_user).grid(row=0, column=1, padx=5)
ttk.Button(button_frame, text="Delete Account", command=delete_account).grid(row=0, column=2, padx=5)
ttk.Button(button_frame, text="Leaderboard", command=show_leaderboard).grid(row=0, column=3, padx=5)

# Help Section
help_frame = ttk.Frame(root)
help_frame.pack(pady=20)

tk.Label(help_frame, text="Controls:", font=("Helvetica", 14)).pack(pady=5)
tk.Label(help_frame, text="Left Arrow: Move left", font=("Helvetica", 12)).pack(pady=2)
tk.Label(help_frame, text="Right Arrow: Move right", font=("Helvetica", 12)).pack(pady=2)
tk.Label(help_frame, text="Down Arrow: Move down", font=("Helvetica", 12)).pack(pady=2)
tk.Label(help_frame, text="Space Bar: Rotate", font=("Helvetica", 12)).pack(pady=2)

# Run the application
root.mainloop()

