# 🧮 Arithmetic Formatter

A Python tool that receives a list of strings which are arithmetic problems and returns them arranged vertically and side-by-side. This project is part of the **Scientific Computing with Python** certification from **FreeCodeCamp**.

## 🚀 Features

- **Vertical Alignment:** Automatically aligns operands and operators based on the longest number in each problem.
- **Strict Validation:** Implements comprehensive error handling as per project requirements:
  - Limits input to a maximum of **5 problems**.
  - Accepts only **addition (+)** and **subtraction (-)** operators.
  - Ensures all operands contain **only digits**.
  - Limits operand length to a maximum of **4 digits**.
- **Optional Results:** Provides an optional argument to display the answers to the problems.

## 🛠 Installation & Usage

### Usage
The function `arithmetic_arranger` takes two arguments:
1. A list of strings (the arithmetic problems).
2. An optional boolean to display answers (default is `False`).
```python
from arithmetic_arranger import arithmetic_arranger

# Formatting without answers
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

# Formatting with answers
print(arithmetic_arranger(["32 + 8", "1 - 3"], show_answer=True))

### Sample Output:


    32      3801      45      123
+  698    -    2    + 43    +  49
------    ------    ----    -----
   730      3799      88      172

```
## 💻 Tech Stack

- **Language:** Python 3.x
- **Core Concepts:**
  - **String Manipulation:** Advanced use of `.rjust()` for precise vertical alignment and `.join()` for efficient string concatenation.
  - **Error Handling:** Robust validation logic to ensure input constraints (operator types, digit-only checks, and length limits).
  - **Formatting:** Dynamic width calculation based on operand lengths to ensure a clean, mathematical layout.
  - **Logic:** Conditional formatting to optionally display calculation results.

---
---

**Developed by Mohammad**   
*Junior Developer | Python Enthusiast*

If you found this project helpful, feel free to give it a ⭐!

