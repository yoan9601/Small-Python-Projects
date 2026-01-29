# 🃏 Blackjack

A command-line Blackjack game built with Python. Play the classic casino card game against the computer dealer!

## 📖 Description

This project is a simplified version of the popular casino game Blackjack (also known as 21). The goal is to get as close to 21 as possible without going over, while beating the dealer's hand.

## 🎮 How to Play

1. You start with two cards, and so does the dealer (one card hidden)
2. Choose to **Hit** (draw another card) or **Stand** (keep your current hand)
3. Face cards (J, Q, K) are worth 10 points
4. Aces are worth 11 or 1 (automatically adjusted)
5. If you go over 21, you **bust** and lose
6. Dealer must hit until they reach 17 or higher

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system

### Running the Game

```bash
# Clone the repository
git clone https://github.com/yoan9601/Small-Python-Projects.git

# Navigate to the project folder
cd Small-Python-Projects/blackjack

# Run the game
python blackjack.py
```

## 📁 Project Structure

```
blackjack/
├── blackjack.py    # Main game logic
├── art.py          # ASCII art logo
└── README.md       # Project documentation
```

## 🎯 Features

- Classic Blackjack rules
- ASCII art logo
- Automatic Ace value adjustment (11 → 1)
- Dealer AI following casino rules
- Play again option

## 📸 Example Output

```
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                 
      `------'                           |__/                  

Your cards: [10, 8], current score: 18
Dealer's first card: 7

Type 'y' to get another card, type 'n' to pass:
```

## 🧠 What I Learned

- Working with lists and random selection
- Creating game loops with while statements
- Conditional logic for game rules
- Importing modules and organizing code
- Writing clean, documented Python code

## 🛠️ Built With

- Python 3
- Random module (for card dealing)

## 👤 Author

**Yoan Boyadzhiev**

- GitHub: [@yoan9601](https://github.com/yoan9601)
- Email: yoan.boyadzhiev1@gmail.com

## 📝 License

This project is part of my Python learning journey through [Angela Yu's 100 Days of Code](https://www.udemy.com/course/100-days-of-code/) course.

---

⭐ If you found this helpful, feel free to star the repository!
