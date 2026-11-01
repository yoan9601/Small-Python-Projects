# Calculator ➕

Console calculator with the four basic operations and a continuous calculation mode.

## Features
- Addition, subtraction, multiplication and division
- A dictionary maps each operation symbol to its function
- Keep calculating with the previous result, or start a new calculation
- ASCII art logo

## Example

```
What is the first number?: 8
What operation would you like to perform? +, -, *, /: *
What is the next number?: 5
8.0 * 5.0 = 40.0
Type 'y' to continue calculating with 40.0, or type 'n' to start a new calculation: y
What operation would you like to perform? +, -, *, /: -
What is the next number?: 10
40.0 - 10.0 = 30.0
```

## How to Run

```bash
python main.py
```

The calculator keeps running until you stop it with `Ctrl+C`.

## Files
- `main.py` – calculator logic
- `art.py` – logo

Pure Python • No dependencies
