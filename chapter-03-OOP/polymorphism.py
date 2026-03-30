# Polymorphism (Same Interface, Different Behavior)

# “Same method name, different behavior”

def process(logger: Logger):
    logger.log("Processing...")

# Works with ANY logger:

process(ConsoleLogger())
process(FileLogger())

""" 
Python uses duck typing
No strict interface enforcement required

"""