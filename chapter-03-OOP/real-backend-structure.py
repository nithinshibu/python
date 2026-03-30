# Flow = Route → Service → DB

# Route Layer 

def get_user_route(user_id):
    return user_service.get_user(user_id)

# Service Layer

class UserService:
    def __init__(self,db):
        self.db=db # dependency injection

    def get_user(self,user_id):
        user=self.db.get(user_id)
        if not user:
            raise Exception("User not found")
        return user

""" 
| Layer   | Responsibility |
| ------- | -------------- |
| Route   | Handle HTTP    |
| Service | Business logic |
| DB      | Data           |

This separation = clean architecture
"""

# ❌ Common Mistakes

# 1) ❌ God Class - a class that does too many things — it controls most of the system, holds too much logic, and violates clean design principles.

class UserService:
    def get_user(self): ...
    def create_user(self): ...
    def send_email(self): ...

# Too many responsibilities
# Violates Single Responsibility Principle

# 2) ❌ Hardcoding dependencies

class UserService:
    def __init__(self):
        self.db = Database()  # ❌ bad

class UserService:
    def __init__(self, db):
        self.db = db  # ✅ injected


""" 
When building APIs:

👉 Classes = services
👉 Objects = instances with dependencies
👉 Composition = dependency injection
👉 Inheritance = optional reuse

"""

""" 
# Typical Project structure
project/
│
├── routes/
│   └── user_routes.py
│
├── services/
│   └── user_service.py
│
├── models/
│   └── user_model.py
│
├── db/
│   └── database.py

"""