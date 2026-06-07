# 🛡️ Luhn Card Validator (Python CLI)

A clean and interactive Python implementation of the **Luhn Algorithm** used to validate credit/debit card numbers.

This project is part of my learning journey in backend and algorithmic programming.

---

## 🚀 Features

- ✅ Credit card validation using the Luhn algorithm
- ✅ Automatic card type detection (Visa, MasterCard, American Express)
- ✅ Input sanitization (removes spaces and dashes)
- ✅ Interactive CLI with continuous execution
- ✅ Graceful exit using `exit` command
- ✅ Proper input validation (prevents runtime errors)

---

## 🧠 What is the Luhn Algorithm?

The **Luhn Algorithm** (also known as Modulus 10 or Mod 10 algorithm) is a checksum formula used to validate identification numbers such as credit card numbers.

### Algorithm Steps:

1. Reverse the card number.
2. Double every second digit (starting from index 1).
3. If doubling results in a number greater than 9, split and sum its digits.
4. Add all digits together.
5. If the total modulo 10 equals 0 → the card number is **valid**.

Mathematically:

\[
\text{Valid if} \quad \sum digits \mod 10 = 0
\]

---

## 📂 Project Structure
courses/
└── luhn_algorithm/
└── main.py

---

## 🛠️ Installation & Run

Make sure you have **Python 3.x** installed.

### 1️⃣ Navigate to the project folder
```bash
cd courses/luhn_algorithm

2️⃣ Run the program

python main.py

💻 Example Usage
Enter card number to validate (or type exit to quit): 4539-1488-0343-6467
VALID 
Card Type: Visa

If invalid:
INVALID 

If incorrect input:
Please enter numbers only.
