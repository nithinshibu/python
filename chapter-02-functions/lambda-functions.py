# Lambda Functions (Use, Don’t Overuse) 

square = lambda x:x * x

# Real Usage (sorting) 
users = [
    {"name": "A", "age": 30},
    {"name": "B", "age": 20}
]

users.sort(key=lambda x: x["age"])

""" 
⚠️ Rule
Use only for small one-line logic
Donot replace normal functions blindly

"""

# COMMON MISTAKES 

# 1. Confusing args vs kwargs

def test(*args, **kwargs):
    pass

""" 
args → tuple
kwargs → dict

"""

# 2. Forgetting unpacking 

user = {"name": "Nithin", "age": 27}
def print_user(name, age):
    print(name, age)

print_user(user)    # ❌
print_user(**user)  # ✅

# 3. Overusing lambda

# If it’s more than 1 line → use def

# Practice Questions 

# 1) Sum all numbers using *args

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # 10

# 2) Create flexible user function 

def create_user(**kwargs):
    return kwargs

print(create_user(name="Nithin", age=27))

# 3) Mixed function

def process(order_id, *items, **meta):
    print(f"Order ID: {order_id}")
    
    print("Items:")
    for item in items:
        print(f" - {item}")
    
    print("Meta:")
    for key, value in meta.items():
        print(f" {key}: {value}")

# process(101, "apple", "banana", user="Nithin", location="Kerala")

""" 
Order ID: 101
Items:
 - apple
 - banana
Meta:
 user: Nithin
 location: Kerala
 
"""