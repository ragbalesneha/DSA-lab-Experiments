#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

// Node Structure for Binary Search Tree
struct Node {
    int data;
    Node* left;
    Node* right;

    // Constructor
    Node(int val) {
        data = val;
        left = nullptr;
        right = nullptr;
    }
};

// Function Prototypes
Node* insert(Node* root, int value);
Node* copyTree(Node* root);
void levelOrder(Node* root);
int height(Node* root);
void printLeafNodes(Node* root);
void freeTree(Node* root);

int main() {
    Node* root = nullptr;
    Node* copyRoot = nullptr;
    int choice;

    do {
        cout << "\n=====================================\n";
        cout << "  Employee Database Analysis (BST)   \n";
        cout << "=====================================\n";
        cout << "1. Insert Employee IDs\n";
        cout << "2. Display Original BST (Level Order)\n";
        cout << "3. Copy BST\n";
        cout << "4. Display Copied BST (Level Order)\n";
        cout << "5. Find Height of BST\n";
        cout << "6. Display Leaf Nodes\n";
        cout << "7. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1: {
                int n, val;
                cout << "Enter number of employee IDs to insert: ";
                cin >> n;
                for (int i = 0; i < n; ++i) {
                    cout << "Enter Employee ID " << (i + 1) << ": ";
                    cin >> val;
                    root = insert(root, val);
                }
                break;
            }
            case 2:
                cout << "\nOriginal BST (Level Order Traversal):\n";
                levelOrder(root);
                break;

            case 3:
                if (root == nullptr) {
                    cout << "Cannot copy an empty tree.\n";
                } else {
                    // Free existing copy if any
                    freeTree(copyRoot);
                    copyRoot = copyTree(root);
                    cout << "BST copied successfully!\n";
                }
                break;

            case 4:
                cout << "\nCopied BST (Level Order Traversal):\n";
                levelOrder(copyRoot);
                break;

            case 5:
                if (root == nullptr) {
                    cout << "Tree is empty.\n";
                } else {
                    cout << "Height of BST: " << height(root) << endl;
                }
                break;

            case 6:
                if (root == nullptr) {
                    cout << "Tree is empty.\n";
                } else {
                    cout << "Leaf Nodes: ";
                    printLeafNodes(root);
                    cout << endl;
                }
                break;

            case 7:
                cout << "Exiting program. Cleaning up memory...\n";
                freeTree(root);
                freeTree(copyRoot);
                break;

            default:
                cout << "Invalid choice! Please enter a option between 1 and 7.\n";
        }
    } while (choice != 7);

    return 0;
}

// 1. Insert Node into BST (Rejects Duplicates)
Node* insert(Node* root, int value) {
    if (root == nullptr) {
        return new Node(value);
    }

    if (value < root->data) {
        root->left = insert(root->left, value);
    } else if (value > root->data) {
        root->right = insert(root->right, value);
    } else {
        cout << "Duplicate Employee ID (" << value << ") detected. Skipping insertion.\n";
    }

    return root;
}

// 2. Copy Binary Search Tree Recursively
Node* copyTree(Node* root) {
    if (root == nullptr) {
        return nullptr;
    }

    Node* newNode = new Node(root->data);
    newNode->left = copyTree(root->left);
    newNode->right = copyTree(root->right);

    return newNode;
}

// 3. Level Order Traversal using dynamic queue
void levelOrder(Node* root) {
    if (root == nullptr) {
        cout << "Tree is empty.\n";
        return;
    }

    queue<Node*> q;
    q.push(root);

    while (!q.empty()) {
        Node* current = q.front();
        q.pop();

        cout << current->data << " ";

        if (current->left != nullptr) {
            q.push(current->left);
        }
        if (current->right != nullptr) {
            q.push(current->right);
        }
    }
    cout << endl;
}

// 4. Calculate Height of BST
int height(Node* root) {
    if (root == nullptr) {
        return -1; // Edge count height (-1 for empty, 0 for single root node)
    }

    int leftH = height(root->left);
    int rightH = height(root->right);

    return max(leftH, rightH) + 1;
}

// 5. Display Leaf Nodes
void printLeafNodes(Node* root) {
    if (root == nullptr) {
        return;
    }

    if (root->left == nullptr && root->right == nullptr) {
        cout << root->data << " ";
        return;
    }

    printLeafNodes(root->left);
    printLeafNodes(root->right);
}

// Utility Function to free allocated memory
void freeTree(Node* root) {
    if (root == nullptr) return;
    freeTree(root->left);
    freeTree(root->right);
    delete root;
}
