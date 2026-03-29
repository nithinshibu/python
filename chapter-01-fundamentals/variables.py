""" 
Python is dynamically typed
Type is decided at runtime

"""
age = 25
name = "Nithin"

x = 10
x = "hello"  # totally valid

""" 
Python is strongly typed but dynamically typed ❌ No implicit conversion like JS ✅ But type is decided at runtime

Strongly typed means every variable has a fixed type, and Python won’t mix incompatible types automatically.
For example, "5" + 2 will throw an error instead of converting "5" to a number.
This is different from JavaScript, which may implicitly convert types.

Dynamically typed means you dont declare the type explicitly.
The type is decided at runtime based on the value assigned.
Example: x = 10 → x is int, later x = "hello" → now x is string.
So Python enforces type safety (strong typing) but determines types automatically (dynamic typing).
In short: flexible assignment, strict usage.


"""
"10" + 5  # ❌ Error

# n / 10 → normal division (float result)
# n // 10 → floor division (integer result)

""" 
/ → gives decimal (float) → ❌ not suitable for digit problems
/ / → gives integer division → ✅ correct for digit extraction

👉 Rule:
For DSA digit problems → always use //, not /
"""