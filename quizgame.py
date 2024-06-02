import tkinter as tk
from tkinter import messagebox
import requests
import mysql.connector
import random
import hashlib

# Database connection configuration
db_config = {
    'user': 'root',  # replace with your MySQL username
    'password': '',  # replace with your MySQL password
    'host': 'localhost',
    'database': 'quiz_game',
}

def connect_db():
    return mysql.connector.connect(**db_config)

def create_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
    conn.commit()
    conn.close()

def verify_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT id FROM users WHERE username = %s AND password = %s", (username, hashed_password))
    result = cursor.fetchone()
    conn.close()
    return result

def fetch_questions(amount=20, category=None, difficulty=None):
    url = 'https://opentdb.com/api.php'
    params = {
        'amount': amount,
        'type': 'multiple'
    }
    if category:
        params['category'] = category
    if difficulty:
        params['difficulty'] = difficulty

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()['results']
    else:
        messagebox.showerror("Error", "Failed to fetch questions")
        return []

def save_score(user_id, score):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO leaderboard (user_id, score) VALUES (%s, %s)", (user_id, score))
    conn.commit()
    conn.close()

def show_leaderboard():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT u.username, l.score, l.date 
        FROM leaderboard l 
        JOIN users u ON l.user_id = u.id 
        ORDER BY l.score DESC, l.date ASC
    """)
    results = cursor.fetchall()
    conn.close()
    
    leaderboard_text = "\nLeaderboard:\n"
    for rank, (username, score, date) in enumerate(results, start=1):
        leaderboard_text += f"{rank}. {username} - {score} points on {date}\n"
    
    leaderboard_label.config(text=leaderboard_text)

def login():
    username = username_entry.get()
    password = password_entry.get()
    user = verify_user(username, password)
    if user:
        messagebox.showinfo("Success", "Login successful!")
        global user_id
        user_id = user[0]
        main_menu_frame.pack_forget()
        start_quiz()
    else:
        messagebox.showerror("Error", "Invalid username or password")

def register():
    username = username_entry.get()
    password = password_entry.get()
    create_user(username, password)
    messagebox.showinfo("Success", "Registration successful! Please log in.")
    main_menu_frame.pack()

def start_quiz():
    global questions, current_question, score
    questions = fetch_questions(amount=20)
    if not questions:
        return
    current_question = 0
    score = 0
    quiz_frame.pack()
    show_question()

def show_question():
    global current_question, questions
    question_data = questions[current_question]
    question_label.config(text=f"Question {current_question + 1}: {question_data['question']}")
    answers = question_data['incorrect_answers'] + [question_data['correct_answer']]
    random.shuffle(answers)
    
    for i, answer in enumerate(answers):
        answer_buttons[i].config(text=answer, command=lambda ans=answer: check_answer(ans))

def check_answer(answer):
    global current_question, score
    correct_answer = questions[current_question]['correct_answer']
    if answer == correct_answer:
        score += 1
        messagebox.showinfo("Correct!", "That's the right answer!")
    else:
        messagebox.showinfo("Incorrect", f"Wrong answer! The correct answer was: {correct_answer}")

    current_question += 1
    if current_question < len(questions):
        show_question()
    else:
        end_quiz()

def end_quiz():
    global user_id, score
    save_score(user_id, score)
    messagebox.showinfo("Quiz Finished", f"Your final score is: {score}/{len(questions)}")
    quiz_frame.pack_forget()
    main_menu_frame.pack()
    show_leaderboard()

def quit_game():
    root.quit()

# GUI Setup
root = tk.Tk()
root.title("Trivia Quiz Game")

# Custom font
title_font = ('Helvetica', 24, 'bold')
label_font = ('Helvetica', 14)
button_font = ('Helvetica', 12)

# Main Menu Frame
main_menu_frame = tk.Frame(root, bg='lightblue', bd=5)
main_menu_frame.place(relx=0.5, rely=0.5, anchor="center")

username_label = tk.Label(main_menu_frame, text="Username:", font=label_font, bg='lightblue')
username_label.pack(pady=5)
username_entry = tk.Entry(main_menu_frame, font=label_font)
username_entry.pack(pady=5)

password_label = tk.Label(main_menu_frame, text="Password:", font=label_font, bg='lightblue')
password_label.pack(pady=5)
password_entry = tk.Entry(main_menu_frame, show="*", font=label_font)
password_entry.pack(pady=5)

login_button = tk.Button(main_menu_frame, text="Login", font=button_font, bg='#0066cc', fg='white', command=login)
login_button.pack(pady=5)

register_button = tk.Button(main_menu_frame, text="Register", font=button_font, bg='#0066cc', fg='white', command=register)
register_button.pack(pady=5)

leaderboard_button = tk.Button(main_menu_frame, text="Leaderboard", font=button_font, bg='#0066cc', fg='white', command=show_leaderboard)
leaderboard_button.pack(pady=5)

quit_button = tk.Button(main_menu_frame, text="Quit", font=button_font, bg='#cc0000', fg='white', command=quit_game)
quit_button.pack(pady=5)

leaderboard_label = tk.Label(root, text="", font=label_font, bg='lightblue')
leaderboard_label.pack(pady=5)

# Quiz Frame
quiz_frame = tk.Frame(root, bg='lightblue', bd=5)

question_label = tk.Label(quiz_frame, text="", font=label_font, wraplength=500, bg='lightblue')
question_label.pack(pady=20)

answer_buttons = []
for i in range(4):
    btn = tk.Button(quiz_frame, font=button_font, bg='#0066cc', fg='white')
    btn.pack(fill="x", pady=5)
    answer_buttons.append(btn)

user_id = None
questions = []
current_question = 0
score = 0

if __name__ == "__main__":
    root.mainloop()
