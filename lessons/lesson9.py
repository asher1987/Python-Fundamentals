# Lesson 9 Classes & Functions

# Basic class definition
class Cat:
    # class variable
    kind = 'feline'

    # constructor
    # name and color are parameters
    def __init__(self, name, color):
        # instance variable
        self.name = name
        self.color = color

    # basic methods
    def cat_color(self):
        return self.color

    def cat_name(self):
        return self.name  # return is a keyword


# object creation
my_cat = Cat('Felix', 'white')
my_other = Cat('Garfield', 'orange')  # This is running the constructor.
# When the object is created: Cat('Garfield', 'orange') it assigns it to the variable: my_cat and/or my_other


# method is shared by all created objects
print(my_cat.cat_name())  # this is calling the function cat_name
print(my_cat.cat_color())
print(my_other.cat_color())

# name is unique to the created object
print(my_cat.name)
print(my_other.name)  # the methods are first and the names are second

# kind is shared by all created objects
print(my_other.kind)

# Functions Review
# keyword argument allows you to change the order of the function parameters
# when calling that method.


def my_fancy_function(arg, arg2):
    print(arg + ' ' + arg2)


# normal function call
# my_fancy_function('Friday', 'Fun')

# keyword = function call

# my_fancy_function(arg2='Weekend', arg='Saturday')

# Arbitrary Aruguments allow for many arguments that are unknown.
# Using *args and **kwargs will help define these arguments


# *args will allow a tuple of arguments
def favorite_color(*colors):
    print('My favorite color is ' + colors[1])


# favorite_color('red', 'blue', 'green')
# below is a tuple
# *args takes a tuple in values, but not as a variable. This will generate an error
# if you push a tuple variable directly
# favs = ('red', 'green', 'blue', 'yellow', 'orange')

# using **kwargs will allow a dictionary of arguments
def vehicles(**truck):
    print('My truck is a ' + truck['model'])


# vehicles(make='Chevy', model='Silverado')  # make and model are keywords


# Using the default argument allows you to have more than one, with one
# given a default value. Thse defaults come after other arguments.
def my_hello(arg, arg2='hi'):
    print(arg2 + ' ' + arg)


# my_hello('Tom')
# my_hello('Tim', 'Hello')


# Using a return keyword will return the value will return the value out of the function
# to a variable you define to the left of the function.
def simple_add(value1, value2):
    return value1 + value2


# total = simple_add(12, 23)
# print(total)
# print(simple_add(5, 10))


# The main function is what is called when a python file is ran through the compiler
# it will perform all actions in the file except functions unless they are called directly


if __name__ == '__main__':
    total = simple_add(12, 23)
    print(total)
























































