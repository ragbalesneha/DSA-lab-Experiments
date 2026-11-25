class Node:
    """Represents a single node in a Binary Tree."""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """Handles tree operations and recursive traversals."""

    def __init__(self):
        self.root = None

    def inorder(self, node):
        """Left -> Root -> Right"""
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        """Root -> Left -> Right"""
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        """Left -> Right -> Root"""
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")


# --- Example Usage ---
if __name__ == "__main__":
    # Constructing a sample binary tree:
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5

    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    print("In-order Traversal  : ", end="")
    tree.inorder(tree.root)
    print()

    print("Pre-order Traversal : ", end="")
    tree.preorder(tree.root)
    print()

    print("Post-order Traversal: ", end="")
    tree.postorder(tree.root)
    print()