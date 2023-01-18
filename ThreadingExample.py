# This file is an example of using threading in python
# Threading: Python threading module provides a high-level interface for creating threads.
# The threading module provides the Thread class to create and manage threads.
# to find out more about the threading module, visit https://docs.python.org/3/library/threading.html

# import the threading module
import threading


# define a function that will be run in a thread
def thread_function():
    print("thread function ran")


# create a thread object
thread = threading.Thread(target=thread_function)

# start the thread
thread.start()

# Output:
# thread function ran
