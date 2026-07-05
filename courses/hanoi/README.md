# Tower of Hanoi — Interactive Console Edition

An enhanced, interactive command-line implementation of the classic **Tower of Hanoi** puzzle, built in Python. This project started as a freeCodeCamp recursion exercise and was significantly leveled up with a visual board, an interactive menu, move statistics, and timing.

## Overview

The Tower of Hanoi is a classic recursive algorithm problem: move a stack of disks from one rod to another, using a third rod as an auxiliary, while never placing a larger disk on top of a smaller one.

This version takes the original recursive solver and wraps it in a full interactive experience:

- A text-based **visual board** that redraws after every move
- A **menu-driven interface** for starting or exiting the program
- **User-defined disk count** (1–8) instead of a hardcoded value
- **Move counter** and **elapsed time** tracking
- **Animated output** with a short delay between moves for readability

## Features

| Feature                  | freeCodeCamp Original | Leveled-Up Version |
|---------------------------|:---:|:---:|
| Recursive Hanoi algorithm | ✅ | ✅ |
| Fixed number of disks     | ✅ | ❌ (user input, 1–8) |
| Visual rod/disk rendering | ❌ | ✅ |
| Interactive menu          | ❌ | ✅ |
| Move counter              | ❌ | ✅ |
| Execution timer           | ❌ | ✅ |
| Move animation delay      | ❌ | ✅ |
| Input validation          | ❌ | ✅ |

## How It Works

1. Run the program and choose **1** to start.
2. Enter the number of disks (between 1 and 8).
3. Press **Enter** to begin the animation.
4. Watch as the algorithm solves the puzzle move-by-move, printing:
   - The move number
   - Which disk is moving and between which rods
   - A live text-rendering of all three rods
5. Once solved, a summary is displayed showing the **total number of moves** and the **time taken**.
6. Choose **2** at the menu to exit the program.

## Example Output

```
--- Tower of Hanoi ---
1. Start program
2. Exit

Please enter your choice: 1
How many disks? (max 8): 3

Initial State:
   =    |    |
  ===   |    |
 =====  |    |
--------------------
   A     B    C

Press Enter to start...

[1] Moving disk 1 from A to C:
...

========================================
 Puzzle Solved Successfully!
Total Moves: 7
Time Taken: 5.62 seconds
========================================
```

## Requirements

- Python 3.x
- No external dependencies (uses only the built-in `time` module)

## Running the Program

```bash
python hanoi.py
```

## Project Structure

```
.
├── hanoi.py     # Main program (menu, display, and recursive solver)
└── README.md
```

## Algorithm Notes

The recursive core follows the standard Tower of Hanoi strategy:

1. Move `n - 1` disks from the source rod to the auxiliary rod.
2. Move the largest remaining disk (`n`) from the source rod to the target rod.
3. Move the `n - 1` disks from the auxiliary rod onto the target rod.

This project keeps that logic intact from the original freeCodeCamp exercise, while adding a `stats` dictionary to track move counts and a `rods` dictionary to keep the state of all three rods in one place for rendering.

## Possible Future Improvements

- Add a difficulty-based scoring or leaderboard system
- Allow the user to manually input moves and validate them against the rules
- Add color-coded disks using a terminal color library (e.g., `colorama`)
- Export move history to a text or JSON log file

## Credits

- Base recursive algorithm adapted from a **freeCodeCamp** learning exercise
- Interactive UI, visualization, statistics, and overall program structure designed and implemented independently as an enhancement of the original exercise

---

**Developed by Mohammad**   
*Junior Developer | Python Enthusiast*