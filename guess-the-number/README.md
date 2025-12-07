# 🎯 Guess the Number

A simple number guessing game with multiple difficulty levels.

![Python Version](https://img.shields.io/badge/python-3.8+-blue?style=flat-square)
![Status](https://img.shields.io/badge/status-complete-success?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

---

## 📖 Description

A classic number guessing game where the computer generates a random number and you try to guess it within a limited number of attempts. Choose from three difficulty levels and test your guessing skills! 🎲

---

## ✨ Features

- 🎯 **Three Difficulty Levels** - Easy, Medium, and Hard modes
- 💪 **Limited Attempts** - Strategic guessing required
- ✅ **Input Validation** - Handles invalid inputs gracefully
- 🔄 **Replay Option** - Play multiple rounds
- 🎨 **ASCII Art Logo** - Beautiful game branding
- 🧹 **Simple Interface** - Clean and easy to understand

---

## 🎮 Difficulty Levels

| Difficulty | Range | Attempts | Challenge |
|------------|-------|----------|-----------|
| 🟢 **Easy** | 1-50 | 10 | Perfect for beginners |
| 🟡 **Medium** | 1-100 | 7 | Balanced gameplay |
| 🔴 **Hard** | 1-200 | 5 | Expert level |

---

## 🚀 How to Play

### 1️⃣ **Run the game**
```bash
python main.py
```

### 2️⃣ **Choose difficulty**
Select 1, 2, or 3 based on your skill level

### 3️⃣ **Make guesses**
Enter numbers to try and guess the target

### 4️⃣ **Follow hints**
- ⬆️ "Too low! Try higher."
- ⬇️ "Too high! Try lower."

### 5️⃣ **Win or lose**
Guess correctly within the attempt limit or game over!

---

## 🎮 Example Gameplay

```
 ██████╗ ██╗   ██╗███████╗███████╗███████╗
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝
██║  ███╗██║   ██║█████╗  ███████╗███████╗
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║
╚██████╔╝╚██████╔╝███████╗███████║███████║
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝

████████╗██╗  ██╗███████╗
╚══██╔══╝██║  ██║██╔════╝
   ██║   ███████║█████╗  
   ██║   ██╔══██║██╔══╝  
   ██║   ██║  ██║███████╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝

███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ 
████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

=======================================================
         Welcome! I'm thinking of a number.
            Can you guess what it is?
=======================================================

Choose your difficulty level:

1. EASY   - Number between 1-50  (10 attempts)
2. MEDIUM - Number between 1-100 (7 attempts)
3. HARD   - Number between 1-200 (5 attempts)

Enter your choice (1-3): 2

==================================================
Difficulty: MEDIUM
I'm thinking of a number between 1 and 100
You have 7 attempts to guess it!
==================================================

Enter your guess (1-100): 50
Too low! Try higher.
Attempts remaining: 6

Enter your guess (1-100): 75
Too high! Try lower.
Attempts remaining: 5

Enter your guess (1-100): 62
Too low! Try higher.
Attempts remaining: 4

Enter your guess (1-100): 68

==================================================
CONGRATULATIONS! YOU WIN!
You guessed the number: 68
It took you 4 attempt(s)!
==================================================

Do you want to play again? (yes/no): no

==================================================
Thanks for playing Guess the Number!
See you next time!
==================================================
```

---

## 💻 Technical Details

### 🛠️ Technologies Used
- **Python 3.8+** - Core programming language
- **random module** - Random number generation (built-in)

### 🎓 Key Concepts Demonstrated

| Concept | Implementation |
|---------|----------------|
| 🔢 **Random Generation** | `random.randint()` for number generation |
| 🔄 **While Loops** | Game loop and input validation |
| 🎯 **Functions** | Modular code organization with 7 functions |
| ✅ **Conditionals** | if/else statements for game logic |
| 🛡️ **Exception Handling** | Try/except for input validation |
| 📝 **Input Validation** | Ensuring valid user input with error messages |
| 🎨 **ASCII Art** | Visual branding with Unicode box characters |

---

## 📁 Code Structure

```
guess-the-number/
│
├── main.py          # Main game file
├── logo.py          # ASCII art logo
└── README.md        # This documentation
```

### 🧩 Files Overview

| File | Purpose | Lines |
|------|---------|-------|
| `main.py` | Core game logic and functions | ~100 |
| `logo.py` | ASCII art branding (imported by main.py) | ~20 |
| `README.md` | Project documentation | - |

### 🧩 Functions Overview

| Function | Purpose | Lines |
|----------|---------|-------|
| `main()` | Entry point, runs the game loop | ~10 |
| `play_game()` | Core game logic and flow | ~40 |
| `choose_difficulty()` | Handles difficulty selection | ~20 |
| `get_guess()` | Gets and validates user input | ~15 |
| `give_hint()` | Provides directional hints | ~8 |
| `ask_play_again()` | Prompts for replay | ~10 |
| `display_welcome()` | Shows ASCII logo and welcome | ~30 |

---

## 📦 Installation & Usage

### Prerequisites
```bash
python --version  # Should be 3.8 or higher
```

### Running the Game

1️⃣ **Clone or download the project**
```bash
git clone https://github.com/yoan9601/Small-Python-Projects.git
cd Small-Python-Projects/guess-the-number
```

2️⃣ **Run the game**
```bash
python main.py
```

3️⃣ **Follow the on-screen instructions**
- Choose difficulty
- Make guesses
- Have fun! 🎉

---

## 🎓 Learning Outcomes

By building this project, you'll learn:

- ✅ **Variables & Data Types** - Working with integers, strings, tuples
- ✅ **User Input** - Getting and validating input from users
- ✅ **Random Numbers** - Generating random values with the random module
- ✅ **While Loops** - Creating game loops and input validation loops
- ✅ **Conditionals** - if/elif/else for game logic and hints
- ✅ **Functions** - Breaking code into reusable, modular functions
- ✅ **Exception Handling** - Using try/except to handle errors gracefully
- ✅ **Code Organization** - Structuring programs with multiple functions
- ✅ **ASCII Art** - Creating visual elements with Unicode characters
- ✅ **Boolean Logic** - Working with True/False values for game control

---

## 🚀 Future Enhancements

Possible improvements for this project:

- 📊 **Score Tracking** - Save statistics across multiple games
- 🌡️ **Proximity Hints** - Add "warm/cold" feedback based on distance
- ⏱️ **Timer Mode** - Speed challenges with time limits
- 💾 **High Scores** - Save best scores to a file
- 🎨 **Color Output** - Add colored text with ANSI codes
- 🌐 **Multiplayer** - Two-player competitive mode
- 🔊 **Sound Effects** - Audio feedback (requires external library)
- 🎮 **GUI Version** - Graphical interface with Tkinter
- 📈 **Difficulty Scaling** - Adaptive difficulty based on performance
- 🏆 **Achievement System** - Unlockable badges and rewards

---

## 👤 Author

**Yoan Boyadzhiev**

- 📍 Location: Sofia, Bulgaria
- 💼 GitHub: [@yoan9601](https://github.com/yoan9601)
- 📸 Instagram: [@yoan.boyadzhiev](https://www.instagram.com/yoan.boyadzhiev/)
- 📧 Email: yoan.boyadzhiev1@gmail.com
- 🎓 Education: SoftUni Student

---

## 📜 License

This project is licensed under the MIT License - free to use, modify, and distribute.

```
MIT License - Feel free to use this code for learning and portfolio purposes!
```

---

## 🙏 Acknowledgments

- 🎓 Part of my Python learning journey at **SoftUni**
- 📚 Inspired by classic number guessing games
- 🐍 Built as part of **Small Python Projects** collection
- 💡 Thanks to the Python community for excellent documentation

---

## 💬 Feedback & Support

Found a bug? Have a suggestion? Want to contribute?

- 🐛 **Report Issues**: Open an issue on GitHub
- 💡 **Suggestions**: I'm always open to feedback!
- 📧 **Contact**: yoan.boyadzhiev1@gmail.com
- 📸 **Connect**: [@yoan.boyadzhiev](https://www.instagram.com/yoan.boyadzhiev/) on Instagram

---

<div align="center">

### ⭐ If you enjoyed this project, please consider giving it a star!

**🎯 Happy Guessing! 🎮**

---

**Made with ❤️ and Python**

</div>
