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