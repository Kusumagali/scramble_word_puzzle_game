import tkinter as tk
import random
import json

# Load words from JSON file
with open('words.json') as f:
    data = json.load(f)
    words = data['words']

# Shuffle word
def shuffle_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

# Check answer
def check_answer():
    user_input = entry.get()
    if user_input.lower() == current_word.lower():
        result_label.config(text="Correct!", fg="green")
    else:
        result_label.config(text="Try Again!", fg="red")

# Next word
def next_word():
    global current_word, shuffled
    current_word = random.choice(words)
    shuffled = shuffle_word(current_word)
    word_label.config(text=shuffled)
    entry.delete(0, tk.END)
    result_label.config(text="")

# GUI setup
root = tk.Tk()
root.title("Word Puzzle Game")

word_label = tk.Label(root, font=('Arial', 24))
word_label.pack(pady=20)

entry = tk.Entry(root, font=('Arial', 16))
entry.pack(pady=10)

check_btn = tk.Button(root, text="Check", command=check_answer)
check_btn.pack(pady=5)

next_btn = tk.Button(root, text="Next Word", command=next_word)
next_btn.pack(pady=5)

result_label = tk.Label(root, font=('Arial', 16))
result_label.pack(pady=10)

# Start with a word
next_word()
root.mainloop()
