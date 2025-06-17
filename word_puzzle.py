import tkinter as tk
import json
import random

# Load words from JSON file
with open("words.json", "r") as f:
    data = json.load(f)
    words = data["words"]

# Game variables
score = 0

# Functions
def new_game():
    global original_word, scrambled_word
    original_word = random.choice(words)
    scrambled_word = ''.join(random.sample(original_word, len(original_word)))
    word_label.config(text=scrambled_word)
    entry.delete(0, tk.END)
    result.config(text="")

def check_word():
    global score
    user_input = entry.get()
    if user_input.lower() == original_word:
        score += 1
        result.config(text="✅ Correct!", fg="green")
        score_label.config(text=f"Score: {score}")
        new_game()
    else:
        result.config(text="❌ Try Again!", fg="red")

# GUI Setup
root = tk.Tk()
root.title("Word Puzzle Game")
root.geometry("300x250")
root.config(bg="#f0f8ff")

tk.Label(root, text="Unscramble the Word", font=("Arial", 14), bg="#f0f8ff").pack(pady=5)
word_label = tk.Label(root, text="", font=("Arial", 24, "bold"), bg="#f0f8ff")
word_label.pack()

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)

tk.Button(root, text="Submit", command=check_word, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(root, text="New Word", command=new_game, bg="#2196F3", fg="white").pack(pady=5)

result = tk.Label(root, text="", font=("Arial", 12), bg="#f0f8ff")
result.pack()

score_label = tk.Label(root, text="Score: 0", font=("Arial", 12), bg="#f0f8ff")
score_label.pack()

# Start game
new_game()
root.mainloop()
