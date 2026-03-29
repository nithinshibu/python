# *args (Variable Positional Arguments)

# Accept any number of positional arguments

def add_numbers(*args):
    return sum(args)

print(add_numbers(1,2,3)) # 6 

# What is args internally? - It’s a tuple


def debug(*args):
    print(type(args))  # <class 'tuple'>


# Real Backend Use Case 

def log_events(*events):
    for event in events:
        print(f"Logging: {event}")

# Flexible logging, metrics, etc.

# **kwargs (Variable Keyword Arguments)

# Accept any number of named arguments 

def print_user(**kwargs):
    print(kwargs)

print_user(name="Nithin",age=27)

# {'name': 'Nithin', 'age': 27}

# What is kwargs internally? - It’s a dictionary

# Real Backend Use Case 

def create_user(**data):
    return {
        "status": "created",
        "data": data
    }

create_user(name="Nithin", age=27)
# This is very similar to handling request bodies

# Combining Everything (IMPORTANT 🚨)

def example(a, b=10, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

# We can call this function like
example(1, 2, 3, 4, x=100, y=200)

"""
a = 1
b = 2
args = (3, 4)
kwargs = {'x': 100, 'y': 200}

"""

# Order Rule - 👉 WE MUST follow this order
def func(
    required_args,
    default_args,
    *args,
    **kwargs
): 
    pass

# Unpacking (VERY USEFUL) 

# List → Arguments 

nums = [1,2,3]

def add(a,b,c):
    return a + b + c

add(*nums)

# Dict → Keyword Arguments

user = {"name": "Nithin", "age": 27}

def print_user(name, age):
    print(name, age)

print_user(**user)

""" 
👉 This is used heavily in:

API request handling
Passing configs

"""
user = {"name": "Nithin", "age": 27}
print_user(**user)  # works because keys match parameters

# What if dictionary has extra keys? 
user = {"name": "Nithin", "age": 27, "phone": "12345"}
print_user(**user)  # ❌ Error - TypeError: got an unexpected keyword argument 'phone'

# How to handle extra keys?  - Use **kwargs:
def print_user(name, age, **kwargs):
    print(name, age)

print_user(**user)  # now works

