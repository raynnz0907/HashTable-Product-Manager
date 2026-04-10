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


# ---------------- MAIN PROGRAM ----------------

ht = HashTable()

while True:
    print("\n1. Add Product")
    print("2. Search Product")
    print("3. Display Table")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter product name: ")
        price = input("Enter product price: ")
        ht.insert(name, price)

    elif choice == '2':
        name = input("Enter product name to search: ")
        result = ht.search(name)

        if result:
            print(f"Product found! Price: {result}")
        else:
            print("Product not found!")

    elif choice == '3':
        ht.display()

    elif choice == '4':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")

