# ⏰ Time Calculator

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![Status](https://img.shields.io/badge/status-complete-success)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

## About
A Python function that calculates a new time by adding a duration to a
starting time — with optional weekday tracking across day rollovers.

Originally based on the freeCodeCamp Time Calculator project, then extended
with robust validation, a structured return format, an interactive CLI, and
a comprehensive automated test suite.

---

## ✨ Features

- Parses 12-hour time input (`"3:00 PM"`) and adds a duration in `H:MM` format
- Correctly rolls over across midnight, multiple days, and even AM/PM boundaries
- Optional weekday tracking — pass in a starting day and get the correct final weekday back
- Full input validation: raises `TypeError` for wrong types, `ValueError` for malformed or out-of-range values
- Returns a structured `dict` instead of a plain string, so callers can use the parts they need
- Interactive CLI (`main.py`) for manual testing
- 33 unit tests (written in `unittest` style, run with `pytest`) covering boundaries, overflow, weekday normalization, and invalid input

---

## 🚀 Usage

```python
from time_calculator import add_time

add_time("3:00 PM", "3:10")
# {'time': '6:10 PM', 'day': None, 'days_later': 0, 'result': '6:10 PM'}

add_time("11:43 PM", "24:20", "Tuesday")
# {'time': '12:03 AM', 'day': 'Thursday', 'days_later': 2,
#  'result': '12:03 AM, Thursday (2 days later)'}
```

Or run the interactive CLI:

```bash
python main.py
```

```
Welcome to the time calculator program.
1. Start program
2. Exit

Enter your choice (1 or 2): 1
Enter start time: 11:30 PM
Enter duration: 2:32
Enter day of week (optional): Friday

Result: 2:02 AM, Saturday (next day)
```

---

## 📥 Input Format

| Parameter     | Format               | Example      | Required |
|---------------|----------------------|--------------|----------|
| `start`       | `H:MM AM/PM`         | `"3:00 PM"`  | ✅ |
| `duration`    | `H:MM` (hours can exceed 24) | `"24:20"` | ✅ |
| `day_of_week` | Weekday name, any case | `"tuesday"` | ❌ |

> `day_of_week` defaults to `None` when omitted.

---

## ⚠️ Error Handling

| Input problem                          | Exception    |
|-----------------------------------------|--------------|
| `start` / `duration` / `day_of_week` not a string | `TypeError`  |
| `start` missing AM/PM or wrong format   | `ValueError` |
| Hour outside 1–12, minute outside 0–59  | `ValueError` |
| `duration` not in `H:MM` format         | `ValueError` |
| `day_of_week` not a real weekday name   | `ValueError` |

---

## 🧠 How It Works

1. Validate the types of all three inputs.
2. Parse `start` into hour/minute/AM-PM and convert to 24-hour format.
3. Parse `duration` into hours/minutes.
4. Add everything together in total minutes, then split back into `days_later`, `final_hour`, `final_minute`.
5. Convert the final hour back to 12-hour format.
6. If a weekday was given, shift it forward by `days_later` (wrapping with `% 7`).
7. Assemble the human-readable result string (`"6:10 PM"`, `"12:03 AM, Thursday (2 days later)"`, etc.).

---

## 🧪 Tests

33 test cases, written in `unittest` style and run with `pytest`, covering:

- Basic addition and next-day rollover
- Noon/midnight boundaries (`11:59 AM` → `12:00 PM`, `11:59 PM` → `12:00 AM`)
- Exact 12h / 24h durations
- Minute overflow (`:50` + `:15` → next hour)
- Multi-day durations (2, 3, 10, even 41 days later)
- Weekday case normalization (`monday` / `MONDAY` / `MoNdAy`)
- Invalid types and invalid values (bad hour, bad minute, bad weekday name)

Test file lives in `tests/test_time_calculator.py`. Run the whole suite from the project root with:

```bash
pip install -r requirements.txt
python -m pytest -v
```

---

## 🔁 From Tutorial to This Version

| | Original freeCodeCamp version | This version |
|---|---|---|
| Return value | Plain string | Structured `dict` (`time`, `day`, `days_later`, `result`) |
| Input validation | None — invalid input crashes with an unrelated error | Explicit `TypeError` / `ValueError` with clear messages |
| Interface | Function call only | Function + interactive CLI (`main.py`) |
| Documentation | Inline comments only | Full docstring + this README |
| Tests | None | 33 unit tests covering edge cases and invalid input |

---

## 📂 Project Structure

```
.
├── main.py                  # Interactive CLI
├── time_calculator.py       # Core add_time() function
├── tests/
│   └── test_time_calculator.py  # Unit tests (33 cases)
├── requirements.txt
├── .gitignore
└── README.md
```