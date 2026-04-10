""" 
1. Why Exception Handling Matters

In APIs:

DB fails
External API fails
Input is invalid
Something unexpected happens

👉 Your job:

Don't crash
Return meaningful errors
Log properly

"""

# 💡Basic try / except

try:
    x =10/0
except:
    print("Error occured")

# Never catch blindly - Bad Practice 

# Better way 

try:
    x=10/0
except ZeroDivisionError:
    print("Cannot divide by zero")


# 💡 Catching Multiple Exceptions

try:
    value = int("abc")
except(ValueError,TypeError):
    print("Invalid input")


# 💡Exception Object

try:
    x = int("abc")
except ValueError as e:
    print(str(e))

""" 
👉 Use this for:

Logging
Debugging

"""

# 💡 Else and Finally 

try:
    x = int("10")
except ValueError:
    print("Error")
else:
    print("Success")  # runs if no error
finally:
    print("Always runs")

""" 
💡 Real Use Case
finally → closing DB, files
else → clean success path

"""

# 💡Raising Exceptions

# Basic 

def get_user(user):
    if not user:
        raise Exception("User not found")

# Better Practice (use specific expections)

def get_user(user):
    if user is None:
        raise TypeError("User cannot be None")


# Custom Exceptions ✔️🔽

# 1. Define Custom Exception (with context) - Instead of a plain exception, include useful metadata.

class UserNotFoundException(Exception):
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.message = f"User with id {user_id} not found"
        super().__init__(self.message)


# 2. Simulate a Data Source (DB / Cache) 
# Fake database
USERS_DB = {
    1: {"id": 1, "name": "Nithin"},
    2: {"id": 2, "name": "Mathew"},
}

# 3. Service Layer (Where exception is raised)
import logging

logger = logging.getLogger(__name__)
def get_user(user_id: int) -> dict:
    user = USERS_DB.get(user_id)
    
    if not user:
        logger.error(f"User {user_id} not found")
        raise UserNotFoundException(user_id)
    
    return user

# 4. Caller Layer (Controller / API Layer)

def main():
    try:
        user = get_user(3)  # invalid user
        print("User found:", user)
    
    except UserNotFoundException as e:
        print("Handled Exception:", e)
    
    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    main()

# Output - Handled Exception: User with id 3 not found

# We can also catch it like 
try:
    get_user(2)
except UserNotFoundException as e:
    print(e)

""" 

💡 Real Backend Use
Domain-specific errors
Clean error handling
Better readability

"""


# 💡 Real API Style Error Handling 

# ❌ Bad Code
def get_user(user_id):
    return USERS_DB[user_id]  # crash if missing

# ✅ Good Code
def get_user(user_id):
    user = USERS_DB.get(user_id)

    if not user:
        raise UserNotFoundException("User not found")

    return user

# Service Layer + Handling
try:
    user = get_user(10)
    response = {"data": user}
except UserNotFoundException as e:
    response = {"error": str(e)}


# ADVANCED - Exception Chaining

try:
    int("abc")
except ValueError as e:
    raise RuntimeError("Parsing failed") from e

""" 
👉 Why?

Preserve original error
Useful in debugging complex systems

"""

# Logging + Exceptions (VERY IMPORTANT)

# ❌ Wrong
try:
    x=10/0
except Exception:
    pass

# Silent failure = nightmare

# ✅ Correct

import logging

try:
    x = int("abc")
except ValueError as e:
    logging.error(f"Error occurred: {e}")

# Designing Error Responses (Backend Thinking)

def get_user(user_id):
    if user_id is None:
        raise UserNotFoundException("User not found")
    
try:
    user = get_user(2)
    response = {
        "status": "success",
        "data": user
    }
except UserNotFoundException as e:
    response = {
        "status": "error",
        "message": str(e)
    }

# Clean, predictable API responses

class OrderNotFound(Exception):
    pass


def process_order(order_id):
    order = db.get(order_id)

    if not order:
        raise OrderNotFound("Order not found")

    try:
        amount = order["amount"]
        total = amount / order["quantity"]
    except KeyError as e:
        raise ValueError(f"Missing field: {e}")

    return total

try:
    result = process_order(10)
except OrderNotFound as e:
    print("404:", e)
except ValueError as e:
    print("400:", e)
except Exception as e:
    print("500:", e)