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

