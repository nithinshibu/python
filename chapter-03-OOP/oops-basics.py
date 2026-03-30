""" 
In real projects, you don't write everything in functions.

You structure code like:
routes → services → repositories → models

OOP helps you:

Organize logic
Avoid duplication
Make code testable
Enable dependency injection

"""

# Basic Class & Object

# Python class 

class UserService:
    def get_user(self,user_id):
        return {"id":user_id,"name":"Nithin"}

# self = current instance (like this in C#)

service = UserService()
service.get_user(1)

# init (Constructor)

class UserService:
    def __init__(self,db):
        self.db = db
    
    def get_user(self,user_id):
        return self.db.get(user_id)

""" 
💡 Real Meaning
Inject dependencies (DB, config, clients)
Store shared state

👉 This is dependency injection mindset

"""

# Real Backend Example

class Database:
    def get(self,user_id):
        return {"id":user_id,"name":"Nithin"}

class UserService:
    def __init__(self,db):
        self.db=db
    
    def get_user(self,user_id):
        return self.db.get(user_id)

db = Database()
service = UserService(db)

print(service.get_user(1))

# This is an example how backend services are structured