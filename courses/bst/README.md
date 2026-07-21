# Binary Search Tree (BST) Implementation in Python

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![Status](https://img.shields.io/badge/status-complete-success)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A clean, modular, and fully-tested Python implementation of a Binary Search Tree (BST) with clean English comments.

<div align="center">
  <h3>Algorithmic Logic & Implementation Details</h3>
  <table border="0" cellpadding="10">
    <tr>
      <td valign="middle">
        <img src="assets/bst_diagram.png" width="300" alt="BST Logic Diagram">
      </td>
      <td valign="middle">
        <table border="1">
          <thead>
            <tr>
              <th>Implementation Logic</th>
              <th>Common Approach</th>
              <th>My Solution</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><b>Node Deletion</b></td>
              <td>Partial/Basic</td>
              <td>Recursive Successor Logic</td>
            </tr>
            <tr>
              <td><b>Traversal</b></td>
              <td>Iterative (Basic)</td>
              <td>Optimized Recursion</td>
            </tr>
            <tr>
              <td><b>Robustness</b></td>
              <td>No Error Checking</td>
              <td>Defensive `None` Handling</td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>
  </table>
</div>

## Features
- **Core Operations**: Insert, Search, and Delete (handling leaf nodes, single-child, and two-children nodes with inorder successor replacement).
- **Properties**: Tree height calculation and node counting.
- **Traversals**: In-order tree traversal (`left -> root -> right`).
- **Visualization**: Rotated 90-degree text representation of the tree structure.
- **Testing**: Complete unit test suite using `pytest`.

## Public API

The `BinarySearchTree` class exposes the following methods for direct use:

| Method | Description | Time Complexity |
| :--- | :--- | :--- |
| `insert(value)` | Add a new node to the tree while preserving BST ordering. | `O(h)` |
| `search(value)` | Check whether a value exists in the tree. | `O(h)` |
| `delete(value)` | Remove a node while preserving BST properties. | `O(h)` |
| `count_nodes()` | Count all nodes currently stored in the tree. | `O(n)` |
| `height()` | Compute the height of the tree. | `O(n)` |
| `display()` | Render the tree in a readable rotated format. | `O(n)` |

> `h` is the height of the tree, and `n` is the total number of nodes.

## Implementation Comparison

| Feature | FCC / Standard Tutorial | My Implementation |
| :--- | :--- | :--- |
| **Architecture** | Script-based / Monolithic | Modular (Class-based, OOP) |
| **Testing** | Manual (print statements) | Automated (`pytest` suite) |
| **Documentation** | Minimal | Professional English Docstrings |
| **Deletion Logic** | Basic (or incomplete) | Robust (Successor/Predecessor handling) |
| **Extensibility** | Hard to maintain | Highly maintainable |

## Project Structure
```text
├── bst.py            # Main BST and TreeNode implementation
├── test_bst.py       # Unit tests covering all operations
└── README.md         # Project documentation
```

## Getting Started

### Prerequisites
Make sure you have Python 3.x installed. It is recommended to use a virtual environment (`venv`).

### Setup and Testing
1. Clone this repository or copy the files.
2. Install testing dependencies:
   ```bash
   pip install pytest
   ```
3. Run the test suite:
   ```bash
   pytest test_bst.py -v
   ```

## Example Usage
```python
from bst import BinarySearchTree

# Initialize tree
bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]

# Insert nodes
for node in nodes:
    bst.insert(node)

# Display tree
print(bst.display())
```
