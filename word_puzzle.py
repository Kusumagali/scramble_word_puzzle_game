import tkinter as tk
import json
import random

# Load words from JSON
with open("words.json", "r") as f:
    words_data = json.load(f)

# Game variables
score = 0
time_left = 30
level = "easy"
word_list = words_data[level]
original_word = ""

# Functions
def select_level(lvl):
    global level, word_list, score
    level = lvl
    word_list = words_data[level]
    score = 0
    score_label.config(text=f"Score: {score}")
    new_game()

def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        timer_label.config(text=f"Time Left: {time_left}s")
        root.after(1000, countdown)
    else:
        result.config(text=f"⏱ Time's up! The word was '{original_word}'", fg="orange")
        entry.config(state='disabled')

def new_game():
    global original_word, scrambled_word, time_left
    time_left = 30
    timer_label.config(text=f"Time Left: {time_left}s")
    entry.config(state='normal')
    entry.delete(0, tk.END)
    original_word = random.choice(word_list)
    scrambled_word = ''.join(random.sample(original_word, len(original_word)))
    word_label.config(text=scrambled_word)
    result.config(text="")
    countdown()

def check_word():
    global score
    user_input = entry.get()
    if user_input.lower() == original_word:
        score += 1
        score_label.config(text=f"Score: {score}")
        new_game()
    else:
        result.config(text="❌ Wrong, try again!", fg="red")

# GUI Setup
root = tk.Tk()
root.title("Word Puzzle Game")
root.geometry("350x350")
root.config(bg="#f0f8ff")

tk.Label(root, text="Word Puzzle Game", font=("Arial", 16, "bold"), bg="#f0f8ff").pack(pady=5)

# Level Buttons
btn_frame = tk.Frame(root, bg="#f0f8ff")
tk.Label(btn_frame, text="Select Level:", bg="#f0f8ff").pack(side=tk.LEFT)
tk.Button(btn_frame, text="Easy", command=lambda: select_level("easy")).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Medium", command=lambda: select_level("medium")).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Hard", command=lambda: select_level("hard")).pack(side=tk.LEFT, padx=5)
btn_frame.pack(pady=5)

# Game Widgets
word_label = tk.Label(root, text="", font=("Arial", 24, "bold"), bg="#f0f8ff")
word_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack()

tk.Button(root, text="Submit", command=check_word, bg="#4CAF50", fg="white").pack(pady=5)
result = tk.Label(root, text="", font=("Arial", 12), bg="#f0f8ff")
result.pack()

score_label = tk.Label(root, text="Score: 0", font=("Arial", 12), bg="#f0f8ff")
score_label.pack()

timer_label = tk.Label(root, text="Time Left: 30s", font=("Arial", 12), bg="#f0f8ff")
timer_label.pack()

# Start game
select_level("easy")  # default
root.mainloop()
