# Quest 1
# Try it yourself 8-15

import printing_functions as pf
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)


# Question 1
# Try it yourself 8-16
# using a program you wrote that has one function in it, store that function in a separate file. import the function
# into your main program file, and call the function using each of these approaches:
# import_module_name

import one_function
from a_function import simple_word
from a_function import simple_word as sw
from a_function import*


# 8-17
# Choose any three programs you wrote for this chapter, and make sure they follow the styling guidelines described
# in this section.
# functions are descriptive in name. A comment appears immediately after the function. # number of characters is limited
# to 79 per line. # Each function is separated by two blank lines


def simple_word():
    """Will print the world 'Hello'"""
    print('Hello')


simple_word()


def simple_word_2():
    """Will print the world 'Python'"""
    print('Python')


simple_word_2()


def simple_word_3():
    """Will print the word 'Class'"""
    print('Class')


simple_word_3()

# Question 2: 9-10
# Using your latest Restaurant class, store it in a module. Make a separate file that imports restaurant. Make a
# restaurant instance, and call one of Restaurant's methods to show that the import state is working properly.
from restaurant import Restaurant

ashley_restaurant = Restaurant('Starbucks', 'coffee')
ashley_restaurant.describe_restaurant()
ashley_restaurant.open_restaurant()

# Question 2: 9-11
# Start with your work from 9-8. Store the classes User, Priviledges, and Admin in one module. Create a separate file
# make an Admin instance, and call show_privileges() to show that everything is working correctly.
from user_privileges_admin import Admin
from user_privileges_admin import Admin
ashley = Admin('Ashley', 'Likes', 'Cloud', 'Dajina', 'good')
ashley.describe_user()

ashley_privileges = ['can delete users', 'can add users', 'can reset passwords']
ashley.privileges.privileges = ashley_privileges

print(f"\n Ashley cannot do the following things:")
ashley.privileges.show_privileges()


# Question 3
def question_3():
    print('I read the random module.')
question_3()

# Question 2: 9-12
# Store the User class in one module and store the Privileges and Admin classes in a separate module. In a separate
# file, create an Admin instance and call show_privileges to show that everything is working correctly

from admin_privileges import Admin
ashley = Admin('Ashley', 'Likes', 'Cloud', 'Dajina', 'good')
ashley.describe_user()

ashley_privileges = ['can delete users', 'can add users', 'can reset passwords']
ashley.privileges = ashley_privileges

print('The admin can do the following things:')
print(ashley_privileges)
ashley.privileges.show_privileges()


