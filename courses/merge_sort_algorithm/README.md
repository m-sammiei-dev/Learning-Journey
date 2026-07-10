# Merge Sort Project (Enhanced Version)

## About

This project is based on the Merge Sort tutorial from **freeCodeCamp**. The original fCC version was a single file that only implemented the sorting algorithm. I took that version and turned it into a more complete, modular project.

## How It Works
<div align="center">
  <table>
    <tr>
      <!-- Left column: Educational GIF -->
      <td width="50%" align="center">
        <img src="merge_sort_demo.gif" alt="Merge Sort Animation" width="100%">
        <br>
        <em>Visualization of the Divide and Conquer algorithm</em>
      </td>
      <!-- Right column: Legend & Guide -->
      <td width="50%" valign="top">
        <h4>Legend & Guide</h4>
        <ul>
          <li>🟦 <b>Blue:</b> Currently being merged</li>
          <li>⬜ <b>Gray:</b> Inactive / Pending</li>
          <li>🟩 <b>Green:</b> Final sorted state</li>
        </ul>
        <hr>
        <p align="justify">
          <b>Logic:</b> This animation demonstrates how the array is recursively split into single-element sub-arrays and then merged back together in sorted order.
        </p>
      </td>
    </tr>
  </table>
</div>


### Logic

Merge Sort works by breaking a big problem (sorting *n* elements) into smaller, easier problems (sorting 1 element, which is trivially already sorted), then combining the solutions back together. This strategy is called **Divide and Conquer**.

**Step 1 — Divide**
The array is split in half recursively until each sub-array contains a single element. For example, `[8, 3, 7, 1, 9, 2, 6, 4]` breaks down like this:

```
[8, 3, 7, 1, 9, 2, 6, 4]
        ↓
[8, 3, 7, 1]        [9, 2, 6, 4]
    ↓                    ↓
[8, 3]   [7, 1]     [9, 2]   [6, 4]
  ↓        ↓          ↓        ↓
[8][3]   [7][1]     [9][2]   [6][4]
```

A single element is always "sorted" by definition, so this is the base case where recursion stops.

**Step 2 — Conquer (Merge)**
Starting from the smallest pieces, pairs of sorted sub-arrays are merged back together in the correct order. To merge two sorted sub-arrays, we compare their front elements one at a time and always take the smaller one first:

```
[8] and [3]  →  compare 8 vs 3  →  3 is smaller  →  [3, 8]
[7] and [1]  →  compare 7 vs 1  →  1 is smaller  →  [1, 7]
[3, 8] and [1, 7]  →  compare step by step  →  [1, 3, 7, 8]
```

This repeats level by level until the whole array is merged back into one fully sorted array.

**Why it's efficient**
- Splitting the array in half each time takes `log₂(n)` levels of recursion.
- Merging all elements at each level takes `O(n)` work.
- Combined, this gives Merge Sort a time complexity of **O(n log n)**, which is significantly better than simpler algorithms like Bubble Sort or Insertion Sort (`O(n²)`) for large inputs.
- The trade-off is space: Merge Sort needs `O(n)` extra memory to hold the temporary left/right sub-arrays during merging, unlike in-place algorithms such as Quick Sort.

**Where `stats` and `reverse` fit in**
- Every time two elements are compared inside the merge step, `stats["comparisons"]` is incremented — this is what lets the program report exactly how many comparisons were needed.
- The `reverse` flag simply flips the comparison condition (`>=` instead of `<=`), so the same merge logic works for descending order without duplicating any code.

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
---
**Developed by Mohammad Sammiei**  
*Junior Developer & AI Student*
