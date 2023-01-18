# This file will be an example of defining a context manager in python
# a context manager is a class that implements the __enter__ and __exit__ methods
# the __enter__ method is called when the context manager is entered
# the __exit__ method is called when the context manager is exited
# the __exit__ method is called even if an exception is raised in the context manager
# Context managers are often used to manage resources such as files, sockets, and locks
# Context managers are also used to manage transactions in databases.
#

# define a context manager class
class ContextManagerExample:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("entering context manager")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exiting context manager")


# define a function that uses the context manager
def use_context_manager():
    with ContextManagerExample("context manager") as cm:
        print("inside context manager")


# call the function that uses the context manager
use_context_manager()

# Output:
# entering context manager
# inside context manager
# exiting context manager
