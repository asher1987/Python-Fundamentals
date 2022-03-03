# Lab Exercise-My Application Overview

# This is Question One
# Write a function called simple().
# Assign a different message to 5 variables and print each message.

def simple ():
    """Days of the week"""
    day1 = 'Monday'
    day2 = 'Tuesday'
    day3 = 'Wednesday'
    day4 = 'Thursday'
    day5 = 'Friday'
    print(day1)
    print(day2)
    print(day3)
    print(day4)
    print(day5)

simple()





# This is Question 2
# Write a function called simple2(). Assign a message to a variable,
# then print out that variable. Change the message and assign it to the
# variable again, but after the first print statement.
# Print the second message. Do these steps 2 more times.
# You should have 4 messages assigned to the same variable and
# 4 print functions showing the results.

def simple2():
    """Displays days of the week"""
    day1 = 'Monday'
    print(day1)
    day1 = 'Tuesday'
    print(day1)
    day1 = 'Wednesday'
    print(day1)
    day1 = 'Thursday'
    print(day1)


simple2()

# This is Question 3
# Write a function called message that takes 1 argument.
# Inside that function, write a print function that takes the argument.

def message(first_name):
    print(first_name + " Likes ")


message('Ashley')