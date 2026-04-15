🧠 Hash Map (Hash Table) Implementation

A Hash Map (or Hash Table) is a data structure that stores data in key–value pairs, allowing for fast insertion, deletion, and lookup operations.

This project demonstrates a simple and efficient implementation of a Hash Map using fundamental concepts like hashing, collision handling, and dynamic storage.
🧠 Hash Map (Hash Table) Implementation

A Hash Map (or Hash Table) is a data structure that stores data in key–value pairs, allowing fast insertion, lookup, and deletion.

This project demonstrates a simple implementation of a hash map using hashing and collision handling.

🚀 Features
Store data as key → value pairs
Fast operations (average O(1) time complexity)
Handles collisions using chaining
Simple and beginner-friendly implementation
⚙️ How It Works

A hash function converts a key into an index:

index = hash(key) % size
This index determines where the value is stored
If multiple keys map to the same index → collision occurs
Collisions are handled using a list (chaining)
🧩 Core Operations
➕ Insert (Put)
hash_map.put("name", "Alice")
🔍 Search (Get)
hash_map.get("name")  # Alice
❌ Delete (Remove)
hash_map.remove("name")

Example usage

hm = HashMap()

hm.put("age", 20)
hm.put("name", "John")

print(hm.get("age"))   # 20

hm.remove("age")
print(hm.get("age"))   # None

