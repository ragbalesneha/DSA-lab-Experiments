class Node:
    """Represents a student record in the Binary Search Tree."""

    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.left = None
        self.right = None


class StudentAdmissionBST:
    """BST for managing student records with iterative traversals."""

    def __init__(self):
        self.root = None

    def insert(self, roll_no, name):
        """Inserts a new student record into the BST based on roll number."""
        new_node = Node(roll_no, name)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if roll_no < current.roll_no:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            elif roll_no > current.roll_no:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right
            else:
                print(f"Roll No {roll_no} already exists.")
                break

    def inorder_iterative(self):
        """Non-recursive Inorder Traversal using an explicit stack."""
        stack = []
        current = self.root

        print("Inorder Traversal (Sorted Ascending Order):")
        while current is not None or len(stack) > 0:
            # Reach the leftmost node of the current node
            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            print(f"Roll No: {current.roll_no} | Name: {current.name}")

            # Visit the right subtree
            current = current.right

    def preorder_iterative(self):
        """Non-recursive Preorder Traversal using an explicit stack."""
        if self.root is None:
            return

        stack = [self.root]

        print("Preorder Traversal (Root-First Order for Backup/Reconstruction):")
        while len(stack) > 0:
            current = stack.pop()
            print(f"Roll No: {current.roll_no} | Name: {current.name}")

            # Push right child first so left child is processed first (LIFO order)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)


# --- Example Usage ---
if __name__ == "__main__":
    bst = StudentAdmissionBST()

    # Inserting student admission records
    students = [(105, "Rahul"), (102, "Sneha"), (108, "Aman"), (101, "Priya"), (104, "Rohan")]
    for roll_no, name in students:
        bst.insert(roll_no, name)

    # Display Traversal Outputs
    bst.inorder_iterative()
    print("-" * 45)
    bst.preorder_iterative()