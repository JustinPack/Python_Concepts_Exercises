# This is a simple demonstration of how to use the multiprocessing module in Python 3.10.
# The multiprocessing module is used to run multiple processes in parallel.
# The multiprocessing module is a package that supports spawning processes
# using an API similar to the threading module. The multiprocessing package
# offers both local and remote concurrency, effectively side-stepping the
# Global Interpreter Lock by using subprocesses instead of threads. Due to this,
# the multiprocessing module allows the programmer to fully leverage multiple
# processors on a given machine. It runs on both Unix and Windows.


import multiprocessing
import time


# define a function for calculating square of a number
def calc_square(numbers):
    for n in numbers:
        print('square: ', n * n)
        time.sleep(0.2)


# define a function for calculating cube of a number
def calc_cube(numbers):
    for n in numbers:
        print('cube: ', n * n * n)
        time.sleep(0.2)


# we will use the multiprocessing module to run the above functions in parallel
# create a list of numbers and pass it to the functions in parallel.
if __name__ == "__main__":
    arr = [2, 3, 8, 9]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))  # create a process for calc_square
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))  # create a process for calc_cube
    # note you can also use the multiprocessing.Process class as a context manager
    # with multiprocessing.Process(target=calc_square, args=(arr,)) as p1:
    # you must start the processes before you can join them
    p1.start()
    p2.start()
    # joining the processes will wait for them to finish before continuing with the rest of the code.
    p1.join()
    p2.join()

    print("Done!")

# Output:
# square:  4
# cube:  8
# square:  9
# cube:  27
