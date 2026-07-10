# Merge Sort Project (Enhanced Version)

## About

This project is based on the Merge Sort tutorial from **freeCodeCamp**. The original fCC version was a single file that only implemented the sorting algorithm. I took that version and turned it into a more complete, modular project.

## How It Works

![Merge Sort demo](merge_sort_demo.gif)

*The array `[8, 3, 7, 1, 9, 2, 6, 4]` is recursively split in half, then merged back together in sorted order. Each frame shows a comparison or placement step until the whole array is sorted.*

| Color | Meaning |
|---|---|
| 🟦 Blue | Segment currently being merged |
| ⬜ Gray | Not part of the current step |
| 🟩 Green | Final sorted array |

## Honest Disclosure About AI Assistance

This was the **first time** I modularized a project (i.e., splitting code into separate files with distinct responsibilities), and I didn't have much experience with it. To learn how to do this properly, I got help from AI (Claude):

- **Modular structure**: I learned how to separate the core logic (`merge_sort.py`), the user interface (`main.py`), and the tests (`test_merge_sort.py`) from each other.
- **Execution time measurement and comparison counting (`stats`)**: I copied this implementation based on AI guidance, then went through and understood why each line works (for example, why a dictionary is used for `stats` instead of a simple variable, due to scope issues in recursive functions).
- The core Merge Sort algorithm itself (the main divide-and-merge logic) I already knew and took directly from the freeCodeCamp tutorial; AI only helped with project structuring and the additional features.

## Comparison with the Original freeCodeCamp Version

| Feature | freeCodeCamp Version | My Version |
|---|---|---|
| File structure | Single file | Three separate files (logic, execution, tests) |
| Sort order | Ascending only | Ascending and descending (`reverse`) |
| Comparison counting | No | Yes (`stats`) |
| Execution timing | No | Yes (`time.perf_counter`) |
| Automated tests | No | 7 tests with `pytest` |
| User interface | Simple print in `__main__` | Interactive menu with user input |
| Stable sort | No (uses `<`) | Yes (uses `<=`) |

## Project Structure

```
├── test/
│   └── test_merge_sort.py   # Unit tests using pytest
├── main.py                  # CLI interactive interface
├── merge_sort.py            # Core Merge Sort implementation
├── .gitignore                # Files to ignore in Git (caches, etc.)
└── README.md                 # Project documentation
```

## How to Run

```bash
python main.py
```

## How to Run Tests

```bash
python -m pytest
```