# Abstraction (Hide Complexity)

# Show WHAT to do, hide HOW it's done

# Example using abstraction

from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, msg):
        pass

# Concrete implementations:
class ConsoleLogger(Logger):
    def log(self,msg):
        print(f"[Console]: {msg}")

class FileLogger(Logger):
    def log(self, msg):
        print(f"[File]: {msg}")  # imagine writing to file

# UserService depends on abstraction 👇

class UserService:
    def __init__(self,logger:Logger):
        self.logger = logger
    
    def get_user(self, user_id):
        self.logger.log(f"Fetching user {user_id}")
        return {"id": user_id}

""" This is Dependency Inversion Principle (SOLID)
You depend on interface, not implementation 
✅ Best Practices:
Always code against interfaces (ABC)
Makes testing & swapping easy (mock logger, etc.)

"""

if __name__ == "__main__":
    logger = ConsoleLogger()   # decision happens HERE
    # logger = FileLogger()    # just swap this line

    service = UserService(logger)
    service.get_user(123)

""" 
You switch behavior without touching UserService
This is loosely coupled design

"""