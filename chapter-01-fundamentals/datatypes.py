""" 
2. Core Data Types


"""
# Numbers & Strings

age = 25          # int
price = 99.9      # float
name = "Nithin"   # str
is_active = True  # bool

# List (Like C# List<T>)

nums = [1, 2, 3, 4]
mixed = [1, "hello", True]

#Ordered (keeps the elements in the same sequence you add them),Mutable (you can modify the list after creating it)

nums.append(5)
nums[0] = 10

# Tuple (Immutable List)
# Cannot change values, Faster than list

point = (10,20)


# Set (Unique Values only)
# No duplicates,Unordered

s = {1, 2, 3, 3}
# {1, 2, 3}

# Dictionary - IMPORTANT 
user = {
    "name":"Maxwell",
    "age": 30
}

# Access elements 
user["name"] # Maxwell
user.get("age") #30 - More Safer approach

#Modify elements
user["age"] = 32

user["missing"]     # ❌ KeyError
user.get("missing") # ✅ None

""" 
Mutable:

list
dict
set

Immutable:

int
str
tuple

"""


""" 
🔹 List (mutable, ordered)

append(x) → add element
extend(iterable) → add multiple
insert(i, x) → insert at index
remove(x) → remove value
pop() → remove last / by index
sort() → sort in-place
reverse() → reverse list
index(x) → find position
count(x) → frequency

🔹 Dictionary (key-value, mutable)

get(key) → safe access
keys() → all keys
values() → all values
items() → key-value pairs
update(dict) → merge
pop(key) → remove key
popitem() → remove last pair
setdefault(key, val) → insert if missing

🔹 Tuple (immutable, ordered)

count(x) → frequency
index(x) → position

👉 (Very limited because immutable)

🔹 Set (mutable, unordered, unique)

add(x) → add element
remove(x) → remove (error if missing)
discard(x) → remove safely
union(set) → combine
intersection(set) → common elements
difference(set) → subtract
update(set) → modify in-place

"""