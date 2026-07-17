# Sudoku Solver

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![Status](https://img.shields.io/badge/status-complete-success)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A simple Python Sudoku solver built with object-oriented design and a backtracking algorithm.

## 🧩 Overview

This project solves standard 9x9 Sudoku puzzles using recursion and backtracking. The solver searches for empty cells, checks whether candidate numbers follow Sudoku rules, and continues until the puzzle is solved.

The project includes:

- a `Board` class for representing and solving the puzzle
- a `solve_sudoku()` helper function
- a small command-line interface in `main.py`
- automated tests written with `pytest`

## ✅ Features

- Solves standard 9x9 Sudoku puzzles
- Uses a recursive backtracking algorithm
- Validates board size, values, and duplicate entries
- Checks rows, columns, and 3x3 subgrids for valid moves
- Includes unit tests for core behavior
- Provides a simple terminal-based interface

## 📁 Project Structure

```text
courses/sudoku_solver/
├── sudoku_solver.py
├── main.py
└── tests/
    └── test_sudoku_solver.py
```

## 🧠 How It Works

The solver uses a backtracking algorithm to complete the Sudoku board.

It works step by step:

1. Search the board for the next empty cell.
2. Try placing numbers `1` to `9` in that position.
3. Check whether the number is valid based on Sudoku rules:
   - it must not already exist in the same row
   - it must not already exist in the same column
   - it must not already exist in the same 3x3 subgrid
4. If the number is valid, place it on the board.
5. Recursively attempt to solve the rest of the puzzle.
6. If a dead end is reached, reset the cell to `0` and try the next number.

This process continues until the puzzle is completely solved or no valid solution exists.

## Requirements

To run this project, you need:

- Python 3.10 or higher
- `pytest` for running the test suite

## Installation

Clone the repository and move into the project directory:

```bash
git clone <your-repository-url>
cd courses/sudoku_solver
```

If needed, install `pytest` to run the tests:

```bash
pip install pytest
```

## 💻 Usage

Run the program from the project directory:

```bash
python main.py
```

When prompted, enter 9 rows of the Sudoku puzzle.  
Use spaces between numbers and enter `0` for empty cells.

## 🎬 Example Input Board

```text
+-------+-------+-------+
| 0 0 2 | 0 0 8 | 0 0 0 |
| 0 0 0 | 0 0 3 | 7 6 2 |
| 4 3 0 | 0 0 0 | 8 0 0 |
+-------+-------+-------+
| 0 5 0 | 0 3 0 | 0 9 0 |
| 0 4 0 | 0 0 0 | 0 2 6 |
| 0 0 0 | 4 6 7 | 0 0 0 |
+-------+-------+-------+
| 0 8 6 | 7 0 4 | 0 0 0 |
| 0 0 0 | 5 1 9 | 0 0 8 |
| 1 7 0 | 0 0 6 | 0 0 5 |
+-------+-------+-------+
```

## 🔍 Solver Flow

The program works like this:

- 🔍 Finds the next empty cell
- 🧠 Tries numbers from `1` to `9`
- ✅ Checks row, column, and 3x3 box rules
- 🔁 Backtracks if a move leads to a dead end
- 🏁 Stops when the puzzle is solved

## 🏁 Example Solved Board

```text
+-------+-------+-------+
| 6 9 2 | 1 7 8 | 5 4 3 |
| 5 1 8 | 9 4 3 | 7 6 2 |
| 4 3 7 | 6 2 5 | 8 1 9 |
+-------+-------+-------+
| 7 5 1 | 2 3 6 | 4 9 8 |
| 8 4 3 | 1 5 9 | 0 2 6 |
| 2 6 9 | 4 8 7 | 3 5 1 |
+-------+-------+-------+
| 9 8 6 | 7 5 4 | 2 3 1 |
| 3 2 4 | 5 1 9 | 6 7 8 |
| 1 7 5 | 3 9 2 | 0 8 5 |
+-------+-------+-------+
```

## 🧪 Running Tests

Run the test suite with:

```bash
python -m pytest tests/test_sudoku_solver.py -v
```

## Test Coverage

The test suite checks important behavior such as:

- accepting a valid puzzle
- rejecting invalid board shapes
- rejecting duplicate values in a row
- locating empty cells correctly
- validating legal and illegal moves
- solving a valid puzzle
- raising an error for an invalid puzzle

## Validation Rules

The board validator checks that:

- the puzzle contains exactly 9 rows
- each row contains exactly 9 values
- every value is an integer from `0` to `9`
- no duplicate non-zero values exist in any row
- no duplicate non-zero values exist in any column
- no duplicate non-zero values exist in any 3x3 subgrid

## Learning Goals

This project demonstrates:

- object-oriented programming in Python
- recursion and backtracking
- input validation
- clean method decomposition
- unit testing with `pytest`

## 🚀 Future Improvements

Possible enhancements for this project:

- read puzzles from a file
- add multiple built-in puzzle examples
- build a graphical user interface
- improve CLI input handling
- package the project as an installable module

## Notes

Do not commit temporary folders such as:

- `.pytest_cache/`
- `__pycache__/`
- `.venv/`

A `.gitignore` file is recommended for these entries.

## License

This project is intended for educational use. If you plan to publish it on GitHub, you can add an MIT License.
