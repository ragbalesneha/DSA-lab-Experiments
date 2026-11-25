#include <iostream>
using namespace std;

class HashTable {
    int hash[10];
    int size;

public:
    HashTable() {
        size = 10;
        for (int i = 0; i < size; i++) {
            hash[i] = -1;
        }
    }

    void insert(int key) {
        int index = key % size;
        int start = index;
        while (hash[index] != -1) {
            index = (index + 1) % size;
            if (index == start) {
                cout << "Hash Table is Full!" << endl;
                return;
            }
        }
        hash[index] = key;
        cout << key << " inserted at index " << index << endl;
    }

    void display() {
        cout << "\nIndex\tValue\n";
        for (int i = 0; i < size; i++) {
            cout << i << "\t";
            if (hash[i] == -1)
                cout << "Empty";
            else
                cout << hash[i];
            cout << endl;
        }
    }
};

int main() {
    HashTable h;
    int n, key;
    cout << "Enter number of keys: ";
    cin >> n;
    cout << "Enter keys:\n";
    for (int i = 0; i < n; i++) {
        cin >> key;
        h.insert(key);
    }
    h.display();
    return 0;
}
```[cite: 1]

### 10B. Linear Probing With Replacement[cite: 1]

```cpp
#include <iostream>
using namespace std;

class HashTable {
    int hash[10];
    int size;

public:
    HashTable() {
        size = 10;
        for (int i = 0; i < size; i++) {
            hash[i] = -1;
        }
    }

    void insert(int key) {
        int index = key % size;
        if (hash[index] == -1) {
            hash[index] = key;
            return;
        }

        if (hash[index] % size != index) {
            int temp = hash[index];
            hash[index] = key;
            cout << temp << " is displaced from index " << index << endl;

            int i = (index + 1) % size;
            while (hash[i] != -1 && i != index) {
                i = (i + 1) % size;
            }
            if (hash[i] == -1) {
                hash[i] = temp;
            } else {
                cout << "Hash Table is Full!" << endl;
            }
        } else {
            int i = (index + 1) % size;
            while (hash[i] != -1 && i != index) {
                i = (i + 1) % size;
            }
            if (hash[i] == -1) {
                hash[i] = key;
            } else {
                cout << "Hash Table is Full!" << endl;
            }
        }
    }

    void display() {
        cout << "\nIndex\tValue\n";
        for (int i = 0; i < size; i++) {
            cout << i << "\t";
            if (hash[i] == -1)
                cout << "Empty";
            else
                cout << hash[i];
            cout << endl;
        }
    }
};

int main() {
    HashTable h;
    int n, key;
    cout << "Enter number of keys: ";
    cin >> n;
    cout << "Enter keys:\n";
    for (int i = 0; i < n; i++) {
        cin >> key;
        h.insert(key);
    }
    h.display();
    return 0;
}
```[cite: 1]

---

## Assignment No. 11: Heap Sort[cite: 1]

### 11A. Heap Sort using Min Heap (Descending Order)[cite: 1]

```cpp
#include <iostream>
using namespace std;

class HeapSort {
    int a[50];
    int n;

public:
    void read() {
        cout << "Enter number of elements: ";
        cin >> n;
        cout << "Enter elements:\n";
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
    }

    void heapify(int n, int i) {
        int smallest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        if (left < n && a[left] < a[smallest]) {
            smallest = left;
        }
        if (right < n && a[right] < a[smallest]) {
            smallest = right;
        }
        if (smallest != i) {
            int temp = a[i];
            a[i] = a[smallest];
            a[smallest] = temp;
            heapify(n, smallest);
        }
    }

    void sort() {
        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(n, i);
        }
        for (int i = n - 1; i > 0; i--) {
            int temp = a[0];
            a[0] = a[i];
            a[i] = temp;
            heapify(i, 0);
        }
    }

    void display() {
        cout << "\nSorted elements in Descending Order:\n";
        for (int i = 0; i < n; i++) {
            cout << a[i] << " ";
        }
        cout << endl;
    }
};

int main() {
    HeapSort h;
    h.read();
    h.sort();
    h.display();
    return 0;
}
```[cite: 1]

### 11B. Heap Sort using Max Heap (Ascending Order)[cite: 1]

```cpp
#include <iostream>
using namespace std;

class HeapSort {
    int a[50];
    int n;

public:
    void read() {
        cout << "Enter number of elements: ";
        cin >> n;
        cout << "Enter elements:\n";
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
    }

    void heapify(int n, int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        if (left < n && a[left] > a[largest]) {
            largest = left;
        }
        if (right < n && a[right] > a[largest]) {
            largest = right;
        }
        if (largest != i) {
            int temp = a[i];
            a[i] = a[largest];
            a[largest] = temp;
            heapify(n, largest);
        }
    }

    void sort() {
        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(n, i);
        }
        for (int i = n - 1; i > 0; i--) {
            int temp = a[0];
            a[0] = a[i];
            a[i] = temp;
            heapify(i, 0);
        }
    }

    void display() {
        cout << "\nSorted elements in Ascending Order:\n";
        for (int i = 0; i < n; i++) {
            cout << a[i] << " ";
        }
        cout << endl;
    }
};

int main() {
    HeapSort h;
    h.read();
    h.sort();
    h.display();
    return 0;
}
```[cite: 1]