import pytest
# Assuming your code is in bst.py
from bst import BinarySearchTree, TreeNode

# Fixture to create a sample Binary Search Tree
@pytest.fixture
def sample_bst():
    bst = BinarySearchTree()
    nodes_to_insert = [10, 5, 15, 2, 7, 12, 18]
    for key in nodes_to_insert:
        bst.insert(key)
    return bst

# Fixture for an empty tree
@pytest.fixture
def empty_bst():
    return BinarySearchTree()

# --- Insertion and Traversal Tests ---

def test_insert_and_inorder_traversal(empty_bst):
    """
    Tests inserting nodes and verifies that inorder traversal returns sorted keys.
    """
    bst = empty_bst
    keys = [50, 30, 70, 20, 40, 60, 80]
    for key in keys:
        bst.insert(key)
    assert bst.inorder_traversal() == [20, 30, 40, 50, 60, 70, 80]

def test_insert_duplicate_key(sample_bst):
    """
    Ensures that inserting a duplicate key does not modify the tree structure.
    """
    initial_inorder = sample_bst.inorder_traversal()
    sample_bst.insert(10) 
    assert sample_bst.inorder_traversal() == initial_inorder

# --- Search Tests ---

def test_search_existing_key(sample_bst):
    """
    Checks if search returns a node (not None) for existing keys.
    """
    assert sample_bst.search(7) is not None
    assert sample_bst.search(10) is not None 

def test_search_non_existing_key(sample_bst):
    """
    Checks if search returns None for non-existing keys.
    """
    assert sample_bst.search(99) is None
    assert sample_bst.search(1) is None

def test_search_in_empty_tree(empty_bst):
    """
    Verifies that searching an empty tree returns None.
    """
    assert empty_bst.search(10) is None

# --- Deletion Tests ---

def test_delete_leaf_node(sample_bst):
    """
    Verifies deletion of a leaf node.
    """
    sample_bst.delete(2)
    assert sample_bst.search(2) is None
    assert sample_bst.inorder_traversal() == [5, 7, 10, 12, 15, 18]

def test_delete_node_with_one_child(sample_bst):
    """
    Verifies deletion of a node that has exactly one child.
    """
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(7) 
    bst.delete(5)
    assert bst.search(5) is None
    assert bst.search(7) is not None
    assert bst.inorder_traversal() == [7, 10]

def test_delete_node_with_two_children(sample_bst):
    """
    Verifies deletion of a node with two children; successor should replace it.
    """
    sample_bst.delete(10)
    assert sample_bst.search(10) is None
    # 12 is the in-order successor of 10 in this specific tree
    assert sample_bst.search(12) is not None 
    assert sample_bst.inorder_traversal() == [2, 5, 7, 12, 15, 18]

def test_delete_non_existing_key(sample_bst):
    """
    Ensures deleting a non-existent key does not affect the tree.
    """
    initial_inorder = sample_bst.inorder_traversal()
    sample_bst.delete(99)
    assert sample_bst.inorder_traversal() == initial_inorder

def test_delete_from_empty_tree(empty_bst):
    """
    Ensures deleting from an empty tree handles gracefully (no crash).
    """
    empty_bst.delete(10) 

# --- Height Tests ---

def test_get_height_of_empty_tree(empty_bst):
    """
    Verifies height of an empty tree is 0 based on current implementation.
    """
    assert empty_bst.get_height() == 0

def test_get_height_of_single_node_tree(empty_bst):
    """
    Verifies height of a single node tree is 1.
    """
    empty_bst.insert(10)
    assert empty_bst.get_height() == 1

def test_get_height_of_sample_tree(sample_bst):
    """
    Verifies height calculation for the sample tree (3 levels).
    """
    assert sample_bst.get_height() == 3

# --- Node Counting Tests ---

def test_count_nodes_of_empty_tree(empty_bst):
    """
    Verifies node count for an empty tree is 0.
    """
    assert empty_bst.count_nodes() == 0

def test_count_nodes_of_single_node_tree(empty_bst):
    """
    Verifies node count for a single node tree is 1.
    """
    empty_bst.insert(10)
    assert empty_bst.count_nodes() == 1
