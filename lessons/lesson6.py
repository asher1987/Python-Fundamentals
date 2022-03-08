# Lesson 6- Control Flow Statements

# Boolean
# These values are either true or false
def boolean_sample():
    print(bool('sample'))
    print(bool(0.0))


boolean_sample()


# if statement
# used to find out if a condition is true
def basic_if(arg1, arg2):
    if arg1 > arg2:
        print('argument1 is greater than argument2')

    if arg1 == arg2:
        print('both values are the same')


basic_if(5, 10)


# elif example
# Used when the first condition is false and you want to try another
def basic_if_elif(arg):
    if arg > 10:
        print('sum is greater than 10')
    elif arg == 10:
        print('arg is less than 10')
    elif arg < 10:
        print('sum is less than 10')


basic_if_elif(12)


