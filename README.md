# 🧮 Simple Calculator

A simple **command-line calculator** built with Python that performs basic arithmetic operations. It allows users to perform multiple calculations in a single session by continuing with the previous result or clearing it to start over.

---

## ✨ Features

- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- 🔢 Exponentiation (Power)
- 🔄 Continue calculations using the previous result
- 🧹 Clear the current result and start a new calculation
- ✅ Input validation for operators
- 🚫 Division by zero handling

---

## 📋 Requirements

- 🐍 Python 3.x
- 📦 No external libraries required

---

## 🚀 How to Run

1. Make sure **Python 3** is installed on your system.
2. Download or clone this repository.
3. Open a terminal or command prompt.
4. Navigate to the project folder.
5. Run the program:

```bash
python calculator.py
```

> **Note:** If your system uses `python3` instead of `python`, run:

```bash
python3 calculator.py
```

---

## 💻 Example Usage

```text
Enter first number: 10
Enter operator(+, -, *, /, ^): +
Enter second number: 5
Result: 15.0

Do you want to continue(y,n) or clear(c): y

Enter operator(+, -, *, /, ^): *
Enter second number: 2
Result: 30.0

Do you want to continue(y,n) or clear(c): n

Final results: 30.0
Bye!
```

---

## 🔄 Continue Options

After every calculation, the program asks:

```text
Do you want to continue(y,n) or clear(c):
```

| Option | Description |
|--------|-------------|
| ✅ `y` | Continue using the current result |
| 🧹 `c` | Clear the result and start a new calculation |
| ❌ `n` | Exit the program and display the final result |

---

## 📁 Project Structure

```text
Simple-Calculator/
│
├── calculator.py
└── README.md
```

---

## ⚙️ Functions

| Function | Purpose |
|----------|---------|
| `add()` | ➕ Adds two numbers |
| `sub()` | ➖ Subtracts two numbers |
| `mul()` | ✖️ Multiplies two numbers |
| `div()` | ➗ Divides two numbers |
| `power()` | 🔢 Calculates the power of a number |
| `main()` | 🎯 Controls program flow and user interaction |

---

## 🛡️ Error Handling

The calculator safely handles:

- ⚠️ Invalid operator selection
- 🚫 Division by zero
- ❌ Invalid continuation choices (`y`, `n`, or `c`)

---

## 🚀 Future Improvements

- 📊 Modulus (%) operation
- √ Square root function
- 🧠 Scientific calculator features
- 📝 Calculation history
- 🖥️ Graphical User Interface (GUI)
- 🔒 Improved input validation with exception handling

---

## 👨‍💻 Author

**Muhammad Hanzla**

---

⭐ If you found this project useful, consider giving it a **star** on GitHub!
