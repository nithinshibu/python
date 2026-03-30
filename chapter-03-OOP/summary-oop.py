from abc import ABC, abstractmethod

# Abstraction
class Logger(ABC):
    @abstractmethod
    def log(self, msg):
        pass

# Implementations
class ConsoleLogger(Logger):
    def log(self, msg):
        print(f"[Console]: {msg}")

class FileLogger(Logger):
    def log(self, msg):
        print(f"[File]: {msg}")

# Business logic
class UserService:
    def __init__(self, logger: Logger):
        self.logger = logger

    def get_user(self, user_id):
        self.logger.log(f"Fetching user {user_id}")
        return {"id": user_id}


if __name__ == "__main__":
    logger = ConsoleLogger()
    user_service = UserService(logger)

    print(user_service.get_user(101))