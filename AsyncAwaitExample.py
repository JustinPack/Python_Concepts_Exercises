# This file is an example of using the async and await keywords in python
# Async/Await: Python introduced async and await keywords in version 3.5 to handle asynchronous programming.
# With these keywords, you can write asynchronous code in a synchronous style.
# The async keyword defines a function as a coroutine, a function defined with the async keyword.
# The await keyword can only be used inside a coroutine, and it can only be used to call another coroutine.
# The await keyword pauses the execution of the current coroutine,
# and waits for the coroutine that is called with the await keyword to complete.
# The await keyword then returns the value returned by the coroutine that is called with the await keyword.
# Await keyword can be used multiple times in a coroutine.
# The asyncio module provides the asyncio.run() function to run a coroutine.
# The asyncio.run() function creates an event loop and runs the coroutine until it completes.
# Async and await keywords are used to write asynchronous code in a synchronous style.
# for example, you might need to wait for a network request to complete,
# or you might need to wait for a file to be read from disk.


# import the asyncio module
import asyncio


# define a coroutine function
async def coroutine_function():
    print("coroutine function ran")


# define a function that calls the coroutine function
async def main():
    await coroutine_function()


# call the main function
asyncio.run(main())

# Output:
# coroutine function ran
