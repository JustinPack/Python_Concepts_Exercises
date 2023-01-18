# This is an example of implementing a metaclass in python
# a metaclass is often used to create classes that are used
# as base classes, that is, classes that are not instantiated directly
# but are used to create other classes. Common uses of a metaclass include
# the creation of API wrappers, ORM, and other frameworks.
# A metaclass is sometimes called a class factory and can creat singleton classes.
# singleton classes are classes that can only have one instance.


class Meta(type):  # Meta is the name of the metaclass
    def __new__(mcs, name, bases, dct):
        print("Creating class %s" % name)
        # print the number of times the metaclass is called
        print("Meta class called %d times" % mcs.count)
        return super().__new__(mcs, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print("Initializing class %s" % name)
        super().__init__(name, bases, dct)

    # define a class attribute to track the number of times the class is instantiated
    count = 0

    # define a class method to return the number of times the class is instantiated
    def get_count(cls):
        return cls.count

    # define a class method to count the number of times the class is instantiated
    def __call__(cls, *args, **kwargs):
        cls.count += 1
        print("Creating instance %d of class %s" % (cls.count, cls.__name__))
        return super().__call__(*args, **kwargs)


class Base(metaclass=Meta):
    def __init__(self):
        print("Initializing Base")

    @staticmethod
    def foo():
        print("foo")


class Derived(Base):
    def __init__(self):
        print("Initializing Derived")
        super().__init__()


# d is initialized as an instance of Derived class which is a subclass of Base class
d = Derived()
b = Derived()


# d.foo() shows that the metaclass is working as expected
# This is because it is able to create a class that inherits the foo method
# from the base class.
d.foo()

# Output:
# Creating class Base
# Initializing class Base
# Creating class Derived
# Initializing class Derived
# Initializing Derived
# Initializing Base
# foo

# The metaclass is called twice, once for the Base class and once for the Derived class.
