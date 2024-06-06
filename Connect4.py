import tkinter as tk
from tkinter import messagebox
import numpy as np
import random

class ConnectFour:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four")
        
        # Initialize user data
        self.users = {}
        self.current_user = None
        
        # Main menu
        self.main_menu()

    def main_menu(self):
        self.clear_window()
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack(pady=20)

        tk.Label(self.menu_frame, text="Connect Four", font=('Arial', 24)).pack(pady=10)
        tk.Button(self.menu_frame, text="Register", command=self.register_screen).pack(pady=5)
        tk.Button(self.menu_frame, text="Login", command=self.login_screen).pack(pady=5)
        tk.Button(self.menu_frame, text="Leaderboard", command=self.leaderboard_screen).pack(pady=5)

    def register_screen(self):
        self.clear_window()
        self.register_frame = tk.Frame(self.root)
        self.register_frame.pack(pady=20)

        tk.Label(self.register_frame, text="Register", font=('Arial', 24)).pack(pady=10)
        tk.Label(self.register_frame, text="Username").pack(pady=5)
        self.reg_username_entry = tk.Entry(self.register_frame)
        self.reg_username_entry.pack(pady=5)
        tk.Label(self.register_frame, text="Password").pack(pady=5)
        self.reg_password_entry = tk.Entry(self.register_frame, show='*')
        self.reg_password_entry.pack(pady=5)
        tk.Button(self.register_frame, text="Register", command=self.register).pack(pady=10)
        tk.Button(self.register_frame, text="Back", command=self.main_menu).pack(pady=5)

    def register(self):
        username = self.reg_username_entry.get()
        password = self.reg_password_entry.get()
        if username in self.users:
            messagebox.showerror("Error", "Username already exists!")
        else:
            self.users[username] = {"password": password, "score": 0}
            messagebox.showinfo("Success", "Registration successful!")
            self.main_menu()

    def login_screen(self):
        self.clear_window()
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(pady=20)

        tk.Label(self.login_frame, text="Login", font=('Arial', 24)).pack(pady=10)
        tk.Label(self.login_frame, text="Username").pack(pady=5)
        self.log_username_entry = tk.Entry(self.login_frame)
        self.log_username_entry.pack(pady=5)
        tk.Label(self.login_frame, text="Password").pack(pady=5)
        self.log_password_entry = tk.Entry(self.login_frame, show='*')
        self.log_password_entry.pack(pady=5)
        tk.Button(self.login_frame, text="Login", command=self.login).pack(pady=10)
        tk.Button(self.login_frame, text="Back", command=self.main_menu).pack(pady=5)

    def login(self):
        username = self.log_username_entry.get()
        password = self.log_password_entry.get()
        if username in self.users and self.users[username]["password"] == password:
            self.current_user = username
            self.level_selection_screen()
        else:
            messagebox.showerror("Error", "Invalid credentials!")

    def leaderboard_screen(self):
        self.clear_window()
        self.leaderboard_frame = tk.Frame(self.root)
        self.leaderboard_frame.pack(pady=20)

        tk.Label(self.leaderboard_frame, text="Leaderboard", font=('Arial', 24)).pack(pady=10)
        sorted_users = sorted(self.users.items(), key=lambda x: x[1]["score"], reverse=True)
        for user, data in sorted_users:
            tk.Label(self.leaderboard_frame, text=f"{user}: {data['score']}").pack(pady=2)

        tk.Button(self.leaderboard_frame, text="Back", command=self.main_menu).pack(pady=10)

    def level_selection_screen(self):
        self.clear_window()
        self.level_frame = tk.Frame(self.root)
        self.level_frame.pack(pady=20)

        tk.Label(self.level_frame, text="Select Difficulty Level", font=('Arial', 24)).pack(pady=10)
        tk.Button(self.level_frame, text="Easy", command=lambda: self.start_game("easy")).pack(pady=5)
        tk.Button(self.level_frame, text="Medium", command=lambda: self.start_game("medium")).pack(pady=5)
        tk.Button(self.level_frame, text="Hard", command=lambda: self.start_game("hard")).pack(pady=5)
        tk.Button(self.level_frame, text="Expert", command=lambda: self.start_game("expert")).pack(pady=5)
        tk.Button(self.level_frame, text="Logout", command=self.logout).pack(pady=10)

    def start_game(self, difficulty):
        self.difficulty = difficulty
        self.clear_window()
        self.canvas = tk.Canvas(self.root, width=700, height=600, bg='blue')
        self.canvas.pack()
        
        self.rows = 6
        self.columns = 7
        self.player_turn = 1
        self.board = np.zeros((self.rows, self.columns))
        self.circles = [[self.canvas.create_oval(col*100+5, row*100+5, col*100+95, row*100+95, fill='white') for col in range(self.columns)] for row in range(self.rows)]
        
        self.canvas.bind("<Button-1>", self.handle_click)

    def handle_click(self, event):
        col = event.x // 100
        if self.drop_piece(col):
            self.update_board()
            if self.check_win():
                self.canvas.create_text(350, 300, text=f"Player {self.player_turn} wins!", font=('Arial', 24), fill='yellow')
                self.canvas.unbind("<Button-1>")
                self.users[self.current_user]["score"] += 1
            else:
                self.player_turn = 3 - self.player_turn  # Toggle between player 1 and 2
                if self.player_turn == 2:
                    self.computer_move()

    def drop_piece(self, col):
        if self.board[0, col] != 0:
            return False
        for row in range(self.rows-1, -1, -1):
            if self.board[row, col] == 0:
                self.board[row, col] = self.player_turn
                return True
        return False

    def update_board(self):
        for row in range(self.rows):
            for col in range(self.columns):
                color = 'white'
                if self.board[row, col] == 1:
                    color = 'red'
                elif self.board[row, col] == 2:
                    color = 'yellow'
                self.canvas.itemconfig(self.circles[row][col], fill=color)

    def check_win(self):
        for row in range(self.rows):
            for col in range(self.columns-3):
                if self.board[row, col] == self.player_turn and all(self.board[row, col+i] == self.player_turn for i in range(4)):
                    return True
        for row in range(self.rows-3):
            for col in range(self.columns):
                if self.board[row, col] == self.player_turn and all(self.board[row+i, col] == self.player_turn for i in range(4)):
                    return True
        for row in range(self.rows-3):
            for col in range(self.columns-3):
                if self.board[row, col] == self.player_turn and all(self.board[row+i, col+i] == self.player_turn for i in range(4)):
                    return True
        for row in range(3, self.rows):
            for col in range(self.columns-3):
                if self.board[row, col] == self.player_turn and all(self.board[row-i, col+i] == self.player_turn for i in range(4)):
                    return True
        return False

    def computer_move(self):
        available_cols = [col for col in range(self.columns) if self.board[0, col] == 0]
        if self.difficulty == "easy":
            col = random.choice(available_cols)
        elif self.difficulty == "medium":
            col = self.medium_computer_move(available_cols)
        elif self.difficulty == "hard":
            col = self.hard_computer_move(available_cols)
        elif self.difficulty == "expert":
            col = self.expert_computer_move(available_cols)
        
        self.drop_piece(col)
        self.update_board()
        if self.check_win():
            self.canvas.create_text(350, 300, text=f"Computer wins!", font=('Arial', 24), fill='yellow')
            self.canvas.unbind("<Button-1>")
        else:
            self.player_turn = 1

    def medium_computer_move(self, available_cols):
        # Implement a simple strategy for medium difficulty
        return random.choice(available_cols)

    def hard_computer_move(self, available_cols):
        # Implement a more advanced strategy for hard difficulty
        return random.choice(available_cols)

    def expert_computer_move(self, available_cols):
        # Implement the most advanced strategy for expert difficulty
        return random.choice(available_cols)

    def logout(self):
        self.current_user = None
        self.main_menu()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = ConnectFour(root)
    root.mainloop()
