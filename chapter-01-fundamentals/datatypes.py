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