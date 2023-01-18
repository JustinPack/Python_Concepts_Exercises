# This file will be an example of defining and using decorators in python
# a decorator is a function that takes another function as an argument
# the decorator function can modify the function that is passed to it
# the decorator function can return a new function that replaces the function that is passed to it
# Decorators are often used to add functionality to existing classes and functions without modifying them.
#

# define a decorator function
def decorator_function(func):
    def wrapper_function():
        print("wrapper executed this before {}".format(func.__name__))
        return func()

    return wrapper_function


# define a function that will be decorated
def display():
    print("display function ran")


# decorate the display function
display = decorator_function(display)

# call the display function
display()

# Output:
# wrapper executed this before display
# display function ran
