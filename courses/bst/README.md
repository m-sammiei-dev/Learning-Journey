# Binary Search Tree (BST) Implementation in Python

A clean, modular, and fully-tested Python implementation of a Binary Search Tree (BST) with clean English comments.

## Features
- **Core Operations**: Insert, Search, and Delete (handling leaf nodes, single-child, and two-children nodes with inorder successor replacement).
- **Properties**: Tree height calculation and node counting.
- **Traversals**: In-order tree traversal (`left -> root -> right`).
- **Visualization**: Rotated 90-degree text representation of the tree structure.
- **Testing**: Complete unit test suite using `pytest`.

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
