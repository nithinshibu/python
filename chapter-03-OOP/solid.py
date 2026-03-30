""" 
SOLID = 5 design principles for writing maintainable, scalable code

S → Single Responsibility Principle
O → Open/Closed Principle
L → Liskov Substitution Principle
I → Interface Segregation Principle
D → Dependency Inversion Principle


"""

# 👉 1. S — Single Responsibility Principle (SRP)

# A class should have only ONE reason to change

# ❌ Bad Example (violates SRP)

class UserService:
    def get_user(self, user_id):
        print(f"[LOG]: Fetching user {user_id}")  # logging
        # DB logic
        return {"id": user_id}
    
""" 
👉 Problem:

Handles logging + business logic
If logging changes → class changes
If DB changes → class changes

"""

# ✅ Correct SRP
class Logger:
    def log(self, msg):
        print(f"[LOG]: {msg}")

class UserService:
    def __init__(self, logger):
        self.logger = logger

    def get_user(self, user_id):
        self.logger.log(f"Fetching user {user_id}")
        return {"id": user_id}
    
""" 
Logger → logging responsibility
UserService → business logic

In real APIs:

Service → business logic
Repository → DB
Logger → logging

"""

# 👉 2. O — Open/Closed Principle (OCP)

# Open for extension, closed for modification

# ❌ Bad Example
class Logger:
    def log(self, msg, type):
        if type == "console":
            print(msg)
        elif type == "file":
            print("writing to file")

# Adding new type → modify existing code ❌

# ✅ Better Design (Polymorphism)

from abc import ABC,abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self,msg):
        pass

class ConsoleLogger(Logger):
    def log(self,msg):
        print(f"[Console]: {msg}")

class FileLogger(Logger):
    def log(self, msg):
        print(f"[File]: {msg}")

""" 
Add new logger → no modification
Just extend

Polymorphism means different objects can be used through the same interface, and each behaves in its own way.
Here, both ConsoleLogger and FileLogger implement the same log() method, so they can be used interchangeably via the Logger type.
At runtime, Python decides which log() implementation to call based on the actual object — that's polymorphism.
🔥 Your UserService stays unchanged:
user_service = UserService(ConsoleLogger())
user_service = UserService(FileLogger())
Avoid if/else explosion → use polymorphism
"""

#👉 3. L — Liskov Substitution Principle (LSP)

# Subclasses should be replaceable without breaking behavior

# ❌ Violation Example
class Logger:
    def log(self, msg):
        print(msg)

class BrokenLogger(Logger):
    def log(self, msg):
        raise Exception("I don't log")
    
# Problem - Replacing Logger breaks system ❌

# ✅ Correct Behavior
class SafeLogger(Logger):
    def log(self, msg):
        print(f"[SAFE]: {msg}")
# Works everywhere Logger is expected ✅
# If subclass changes expected behavior → LSP violation

""" 
`SafeLogger` is better because it respects the contract of the base `Logger` class — when you call `log()`, it actually logs something instead of failing.
In simple terms, any code using `Logger` expects “give message → it gets logged,” and `SafeLogger` still does exactly that.
`BrokenLogger`, on the other hand, breaks that expectation by throwing an exception, which can crash the system unexpectedly.
This means if you replace `Logger` with `BrokenLogger`, existing working code can suddenly fail — that’s what LSP warns against.
`SafeLogger` may change *how* the message is logged (adds `[SAFE]`), but it doesn’t change *what* the method is supposed to do.
So technically, `SafeLogger` is a valid substitute, while `BrokenLogger` violates the expected behavior contract.

"""

#👉 4. I — Interface Segregation Principle (ISP)

# Don’t force classes to implement methods they don’t use

# ❌ Bad Interface

class Logger:
    def log(self, msg): pass
    def save_to_file(self, msg): pass
    def send_email(self, msg): pass

# Every logger must implement everything ❌

# ✅ Better Design
class Logger(ABC):
    @abstractmethod
    def log(self, msg):
        pass
# Keep interfaces small and focused
# Prefer multiple small interfaces over one big “God interface”

#👉 5. D — Dependency Inversion Principle (DIP)

""" 
High-level modules should NOT depend on low-level modules
Both should depend on abstractions

"""
# ❌ Bad Example

class UserService:
    def __init__(self):
        self.logger = Logger()  # tightly coupled ❌

# ✅ Correct Example

class UserService:
    def __init__(self, logger):
        self.logger = logger  # injected dependency

""" 
Dependency Injection ✅
Loose coupling ✅

"""

# 🔥 Even Better (with abstraction)
class UserService:
    def __init__(self, logger: Logger):
        self.logger = logger

# Now depends on interface, not implementation