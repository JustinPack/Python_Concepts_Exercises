# This file will be an example of defining and using generators in python
# a generator is a function that returns an iterator
# a generator function is defined using the yield keyword
# the yield keyword pauses the function and saves the state of the function
# then yield keyword returns the value to the iterator
# the yield keyword can be used multiple times in a generator function

# define a generator function
def generator_function():
    for i in range(10):
        yield i


# create a generator object
gen = generator_function()

# iterate through the generator object
for item in gen:
    print(item)

# Output:
# 0-9 are printed to the console
