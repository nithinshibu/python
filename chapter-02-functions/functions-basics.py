def get_user_name(user_id):
    return f"user_{user_id}"

""" No type required
Return anything (even multiple values) """

# Multiple Returns (Used Often)

def get_user():
    return "Maxwell", 30

name, age = get_user() # Tuple unpacking = assigning multiple variables from a tuple in one line

# Python returns a tuple automatically

# Default Arguments 

def greet(name="Guest"):
    return f"Hello {name}"

greet()        # Hello Guest
greet("Maxwell") # Hello Maxwell


#Bug Trap: Mutable Defaults ❌
def add_item(lst=[]):  # BAD
    lst.append(1)
    return lst

# This list is shared across calls (hidden bug)
""" 
This is a bug because the list is created only once when the function is defined, not every time it runs.
So every call to the function uses the same list instead of a new one.
This makes the list keep growing unexpectedly across calls.
Its confusing because you think each call is independent, but they are actually sharing state.
👉 In short: hidden shared memory leads to unexpected results.

"""
# ✅ Correct Pattern

def add_item(lst=None):
    if lst is None:
        lst = []
    lst.append(1)
    return lst

# Positional vs Keyword Arguments
def create_user(name, age):
    return f"{name} is {age}"

# Positional 
create_user("Maxwell",27)

# Keyword
create_user(age=27,name="Maxwell") # in the keyword arguments order does NOT matter

""" You are explicitly telling Python which value goes to which parameter
So position becomes irrelevant

👉 Rule:

Positional → order matters
Keyword → order doesnot matter """

""" ⚠️ Rule
Positional first
Then keyword
"""

create_user("Nithin", age=27)  # ✅ Correct way of calling the function


