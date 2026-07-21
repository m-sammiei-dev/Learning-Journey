class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.key)
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def _insert(self, node, key):
        # Create a new node when the correct position is found.
        if node is None:
            return TreeNode(key)
        
        # Move left for smaller keys and right for larger keys.
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node
    def insert(self, key):
        self.root = self._insert(self.root, key)
        
    def _search(self, node, key):
        # Stop when the node is missing or the key is found.
        if node is None or node.key == key:
            return node
        
        # Continue searching in the correct subtree.
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)
    def search(self, key):
        return self._search(self.root, key)
    
    def _delete(self, node, key):
         # Return the node unchanged if the key does not exist.
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # If the node has only one child or no child,
            # return the existing child directly.
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Replace the node with its inorder successor.
            min_key = self._min_value(node.right)
            node.key = min_key
            node.right = self._delete(node.right, min_key)

        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _min_value(self, node):
        # The leftmost node in a subtree has the minimum value.
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node.key

    
    def _inorder_traversal(self, node, result):
        # Visit left subtree, current node, then right subtree.
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)
            
    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result
    
    def _get_height(self, node):
        # An empty node contributes 0 to the current height logic.
        if node is None:
            return 0
        return 1 + max(self._get_height(node.left), self._get_height(node.right))
    def get_height(self):
        return self._get_height(self.root)

    def _count_nodes(self, node):
        # Count the current node plus all nodes in both subtrees.
        if node is None:
            return 0
        return 1 +  self._count_nodes(node.left) + self._count_nodes(node.right)  
    def count_nodes(self):
        return self._count_nodes(self.root)
    
    def _display(self, node, level, profix="Root: "):
        # Build a rotated text view of the tree.
        if node is None:
            return ""
        right_str = self._display(node.right, level + 1, "R--")
        indent = " " * (level * 4)
        current_node_str = indent + profix + str(node.key) + "\n"
        left_str = self._display(node.left, level + 1, "L--")
        
        return right_str + current_node_str + left_str
    
    def display(self):
        if self.root is None:
            print("Tree is empty")
        return self._display(self.root, level=0, profix="Root: ") 
      
if __name__ == "__main__":    
    bst = BinarySearchTree()
    nodes = [50, 30, 20, 40, 70, 60, 80]

    for node in nodes:
        bst.insert(node)
    print(bst.display())