# 🔨 Blind Auction

A command-line secret bidding program built with Python. Host anonymous auctions where bidders can't see each other's bids!

## 📖 Description

This project simulates a blind auction (also known as a sealed-bid auction). Each participant submits their bid secretly, and the program automatically determines the winner with the highest bid at the end.

## 🎮 How to Play

1. Enter your name
2. Enter your bid amount
3. Pass the device to the next bidder (screen clears for privacy)
4. Repeat until all bidders have entered their bids
5. Type 'no' when asked if there are more bidders
6. The winner is automatically announced!

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system

### Running the Program

```bash
# Clone the repository
git clone https://github.com/yoan9601/Small-Python-Projects.git

# Navigate to the project folder
cd Small-Python-Projects/blind-auction

# Run the program
python main.py
```

## 📁 Project Structure

```
blind-auction/
├── main.py         # Main auction logic
├── art.py          # ASCII art logo
└── README.md       # Project documentation
```

## 🎯 Features

- Anonymous bidding system
- Screen clearing between bidders for privacy
- Automatic winner detection
- Cross-platform support (Windows, macOS, Linux)
- ASCII art logo

## 📸 Example Output

```
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\

Welcome to the Secret Auction Program!

What is your name?: Alice
What is your bid?: $150
Are there any other bidders? Type 'yes' or 'no': yes

[Screen clears]

What is your name?: Bob
What is your bid?: $200
Are there any other bidders? Type 'yes' or 'no': no

The winner is Bob with a bid of $200!
```

## 🧠 What I Learned

- Working with dictionaries to store key-value pairs
- Creating and calling functions with parameters
- Using loops with boolean flags
- Clearing the terminal screen across different operating systems
- Importing and using external modules

## 🛠️ Built With

- Python 3
- OS module (for screen clearing)

## 👤 Author

**Yoan Boyadzhiev**

- GitHub: [@yoan9601](https://github.com/yoan9601)
- Email: yoan.boyadzhiev1@gmail.com

## 📝 License

This project is part of my Python learning journey through [Angela Yu's 100 Days of Code](https://www.udemy.com/course/100-days-of-code/) course.

---

⭐ If you found this helpful, feel free to star the repository!