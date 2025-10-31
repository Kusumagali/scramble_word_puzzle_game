# Scramble Word Puzzle Game  
![Python](https://img.shields.io/badge/Python-3.8%2B-blue) 
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green) 
![NLTK](https://img.shields.io/badge/NLTK-NLP-purple)
![JSON](https://img.shields.io/badge/JSON-Config-yellow)

## 🎮 Project Overview  
An interactive **word scramble puzzle game** built using **Python (Tkinter GUI)** with **multiple difficulty levels** and **score tracking**.  
Users must rearrange the scrambled letters into the correct word before the timer runs out.  
Designed to **improve vocabulary, logical thinking, and reaction time.**

## 🧰 Tech Stack  
- Python  
- Tkinter (Graphical User Interface)  
- NLTK (Word dictionary validation)  
- JSON (Level configuration & score storage)

## 🔍 Key Features  
- ✅ Multiple difficulty levels  
- ✅ Timed gameplay with increasing challenge  
- ✅ Real dictionary-based validation using **NLTK**  
- ✅ Score increases for correct answers  
- ✅ Clean, simple and interactive UI  

## 🚀 What I Did  
- Developed the complete GUI using Tkinter (buttons, layout, text fields).  
- Implemented **word shuffling logic** and randomized puzzles.  
- Used **NLTK corpus** to verify that the player's answer is a real word.  
- Stored level data and game configuration in JSON for easy expansion.  
- Designed **progression system** where difficulty increases every few rounds.

## 🛠 How to Run  
```bash
git clone https://github.com/Kusumagali/scramble_word_puzzle_game.git
cd scramble_word_puzzle_game
pip install -r requirements.txt
python game.py

```
## Requirement:
If NLTK data is not installed, run:

import nltk
nltk.download('words')

## 🕹️ How to Play

A scrambled word appears on screen

Type the correct word in the input box

Submit before time runs out

Score increases with correct answers

Levels get harder as you progress

## Future Improvements

Add leaderboard or scoring history

Add hint system (reveal 1 letter)

Convert to Android APK using Kivy or BeeWare

Add background music & animations using Pygame
