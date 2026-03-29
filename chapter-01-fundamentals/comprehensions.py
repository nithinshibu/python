nums = [1, 2, 3, 4]

squares = [x * x for x in nums]

# With condition

evens = [x for x in nums if x % 2 == 0 ]

# Dictionary Comprehension 

nums = [1,2,3]
sqaure_map = {x: x*x for x in nums}

# {1: 1, 2: 4, 3: 9}

users = [
    {"name": "A", "active": True},
    {"name": "B", "active": False}
]

active_users = [u for u in users if u["active"]]

# IMPORTANT POINTS TO REMEMBER 

# 1. Mutable default arguments ❌ - WRONG IMPLEMENTATION

def add_item(lst=[]): #BAD
    lst.append(1)
    return lst

""" 
This is bad because default arguments in Python are evaluated only once, not every time the function is called.
So the same list "lst" is reused across multiple function calls instead of creating a new one each time.

This leads to unexpected behavior:
add_item()  # [1]
add_item()  # [1, 1]
add_item()  # [1, 1, 1]

The list keeps growing because its the same object in memory, not a fresh list per call.
This can cause hidden bugs, especially in larger programs where the function is called multiple times.

"""
# ✅ Correct Way

def add_item(lst=None):
    if lst is None:
        lst = []
    lst.append(1)
    return lst


# Using == instead of is

a = None

if a is None:  # ✅ correct
    pass

""" 
"is" checks identity (whether both variables point to the exact same object), while == checks value equality.
None is a singleton in Python, so there is only one instance of it in memory.
So "a is None" is the correct and safest way to check for None, instead of a == None.
"""

a = [1, 2]
b = [1, 2]

print(a == b)  # True  (same values)
print(a is b)  # False (different objects)

# Even though contents are same, they are different objects in memory, so is is False.

""" 
Simple rule:

== → compare data
is → compare identity (memory reference)

"""

# Count frequency
# ["a","b","a","c","b","a"]
# output: {"a":3, "b":2, "c":1}

nums = ["a","b","a","c","b","a"]

freq = {}

for x in nums:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

print(freq)