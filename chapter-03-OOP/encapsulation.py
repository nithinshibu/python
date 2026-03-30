# Encapsulation (Data Hiding + Control)

# Don’t expose everything directly — control access

# ❌ Bad (No encapsulation)

class UserService:
    def __init__(self):
        self.users = {}  # directly exposed


# ✅ Good (Encapsulation)

class UserService:
    def __init__(self,logger):
        self._users = {} #protected (internal use)
        self.logger=logger
    
    def add_user(self,user_id,name):
        self._users[user_id] = name
        self.logger.log(f"User {name} added")
    
    def get_user(self,user_id):
        return self._users.get(user_id)
    
""" 
_var → "protected" (by convention)
__var → name mangling (stronger protection)
Encapsulation = control + safety + maintainability

✅ Best Practices:
Never expose raw internal state directly
Use methods instead of direct attribute access
Validate data inside methods

"""

