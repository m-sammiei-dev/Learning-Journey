# 🔐 Password Generator

A secure, interactive command-line password generator built with Python.  
Based on the [freeCodeCamp](https://www.freecodecamp.org/) curriculum — extended with input validation, regex safety fixes, and a full interactive menu.

---

## ✨ Features

- 🔒 Cryptographically secure generation using Python's `secrets` module
- ✅ Fully customizable constraints (length, digits, uppercase, lowercase, symbols)
- 🛡️ Input validation with clear error messages
- 🧩 `re.escape()` applied to symbols — prevents regex pattern bugs
- 🎲 Generate multiple **unique** passwords in a single run (via `set()`)
- 💬 Interactive CLI menu for a real user experience

---

## 📋 What I Added Beyond the Course

| Feature | freeCodeCamp Version | My Version |
|---|---|---|
| Input validation | ❌ | ✅ `ValueError` with messages |
| Regex safety (`re.escape`) | ❌ (had a bug) | ✅ Fixed |
| Interactive CLI menu | ❌ | ✅ Loop with options |
| Multiple unique passwords | ❌ | ✅ Using `set()` |
| Docstring | ❌ | ✅ |

---

## 🚀 How to Run

**Requirements:** Python 3.6+

```bash
git clone https://github.com/m-sammiei-dev/Learning-Journey.git
cd Learning-Journey/courses/password_generator
python password_generator.py
```

---

## 🖥️ Example Usage

```
Welcome to password generator
1. Create New Password
2. Exit

Please choose your option: 1
How many passwords do you want? 3
Please enter the length of each password: 20
How many numbers do you want in each password at least? 2
How many lowercase letters do you want in each password at least? 4
How many uppercase letters do you want in each password at least? 4
How many symbols do you want in each password at least? 2

Generated passwords:
1. kR7@mQz!Xv2LpN8wYsT
2. A3#nWqE!mJ9rKv5xLpYu
3. Tz$8BwNm!3rKvLpXs2Yq
```

---

## 🧠 Key Concepts Used

- `secrets` module for cryptographically secure randomness
- `string` module (`ascii_letters`, `digits`, `punctuation`)
- Regular expressions with `re.findall()` and `re.escape()`
- `set()` for unique password collection
- `ValueError` for defensive input validation
- CLI interaction with `input()` and loop control flow

---

## 📁 Project Structure

```
password_generator/
└── password_generator.py
```

---

## 🗺️ Part of My Learning Journey

This project is part of my path toward **AI Engineering**.  
[→ View the full roadmap](https://github.com/m-sammiei-dev/Learning-Journey)
