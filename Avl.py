class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    # Hash function (based on ASCII values)
    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    # Rehashing (linear probing)
    def rehash(self, index):
        return (index + 1) % self.size

    # Insert product
    def insert(self, key, value):
        index = self.hash_function(key)

        original_index = index
        while self.table[index] is not None:
            # If key already exists, update value
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = self.rehash(index)

            if index == original_index:
                print("Hash Table is full!")
                return

        self.table[index] = (key, value)
        print(f"Product '{key}' added successfully!")

    # Search product
    def search(self, key):
        index = self.hash_function(key)

        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]

            index = self.rehash(index)
            if index == original_index:
                break

        return None

    # Display table
    def display(self):
        print("\nHash Table:")
        for i, item in enumerate(self.table):
            print(f"{i} --> {item}")

