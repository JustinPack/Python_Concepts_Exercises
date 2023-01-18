# This file will be a demonstration of how to use the unittest module in python
# The unittest module is a framework for unit testing in Python. It is a part of the standard library.
# The unittest module provides a rich set of tools for constructing and running tests.
# It supports test automation, sharing of setup and shutdown code for tests,
# aggregation of tests into collections,
# and independence of the tests from the reporting framework.

# import the unittest module
import unittest


# define a function that will be tested
def add(x, y):
    return x + y


# define a class that will be used to test the add function
class TestAdd(unittest.TestCase):
    # define a function that will be used to test the add function
    def test_add(self):
        # assert that the add function returns the correct value
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(10, 3), 13)
        self.assertEqual(add(5, 10), 15)
        self.assertEqual(add(5, 5), 10)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-5, 5), 0)
        self.assertEqual(add(-5, -5), -10)
        self.assertEqual(add(-5, 0), -5)
        self.assertEqual(add(0, -5), -5)
        self.assertEqual(add(-5, 10), 5)
        self.assertEqual(add(10, -5), 5)
        self.assertEqual(add(-10, -5), -15)
        self.assertEqual(add(-10, 5), -5)

        # assert that the add function returns the incorrect value
        self.assertNotEqual(add(5, 3), 9)
        self.assertNotEqual(add(10, 3), 12)
        self.assertNotEqual(add(5, 10), 14)
        self.assertNotEqual(add(5, 5), 11)
        self.assertNotEqual(add(5, 0), 6)
        self.assertNotEqual(add(0, 0), 1)
        self.assertNotEqual(add(-5, 5), 1)
        self.assertNotEqual(add(-5, -5), -9)
        self.assertNotEqual(add(-5, 0), -4)
        self.assertNotEqual(add(0, -5), -4)

        # assert that the add function returns the correct value when the arguments are floats
        self.assertEqual(add(5.5, 3.5), 9)
        self.assertEqual(add(10.5, 3.5), 14)
        self.assertEqual(add(5.5, 10.5), 16)

        # assert that the add function returns the incorrect value when the arguments are floats
        self.assertNotEqual(add(5.5, 3.5), 10)
        self.assertNotEqual(add(10.5, 3.5), 13)
        self.assertNotEqual(add(5.5, 10.5), 15)

        # assert that the add function returns the correct value when the arguments are strings
        self.assertEqual(add("Hello ", "World"), "Hello World")
        self.assertEqual(add("Hello ", "World!"), "Hello World!")
        self.assertEqual(add("Hello ", "World!!!"), "Hello World!!!")

        # assert that the add function returns the incorrect value when the arguments are strings
        self.assertNotEqual(add("Hello ", "World"), "Hello World!")
        self.assertNotEqual(add("Hello ", "World!"), "Hello World")
        self.assertNotEqual(add("Hello ", "World!!!"), "Hello World!")


# run the tests
if __name__ == '__main__':
    unittest.main()
