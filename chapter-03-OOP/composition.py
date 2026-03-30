# Instance vs Class Variables

""" 
Instance variable → belongs to ONE object
Class variable → shared across ALL objects

"""

class Counter:
    total=0 # class variable (shared)

    def __init__(self):
        self.id = Counter.total # instance variable
        Counter.total +=1

a = Counter()
b = Counter()

print(a.id)  # 0
print(b.id)  # 1
print(Counter.total)  # 2

""" 
| Type     | Access    | Behavior          |
| -------- | --------- | ----------------- |
| Instance |  self.x   | Unique per object |
| Class    |  Class.x  | Shared            |


"""

# Inheritance (I want to reuse behavior) 

class BaseService:
    def log(self,message):
        print(f"[LOG]: {message}")

class UserService(BaseService):
    def get_user(self,user_id):
        self.log("Fetching user")
        return {"id":user_id}

# UserService inherits log() from BaseService
# So you don’t rewrite logging logic

# ⚠️ Problem with inheritance - If overused:

class A(B(C(D(E)))):
    pass

# You will NOT know where logic is coming from
# Debugging becomes HARDER

#✅ Composition (VERY IMPORTANT — real-world best practice)
# “Instead of inheriting, I PASS what I need

class Logger:
    def log(self,msg):
         print(f"[LOG]: {msg}")

class UserService: 
    def __init__(self,logger):
        self.logger = logger  # injected dependency

    def get_user(self,user_id):
        self.logger.log(f"Fetching user with id {user_id}")
        return {"id":user_id}

if __name__ == "__main__":
    logger=Logger()  # create dependency
    user_service = UserService(logger) #inject dependency

    user = user_service.get_user(101)
    print(user)


""" 
In composition, dependencies are created externally and injected into the class, making the system flexible, testable, and loosely coupled.


What is if __name__ == "__main__":?

👉 It checks whether the Python file is being run directly OR imported as a module

It ensures that certain code runs only when the script is executed directly, not when it is imported into another module.
1) Prevents unwanted execution
When importing modules, you don't want test/debug code to run
2) Used for testing / demo code
3)Clean modular design
Makes your file reusable as both:
Script ✅
Module ✅


"""