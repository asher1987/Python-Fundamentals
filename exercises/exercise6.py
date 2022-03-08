# Lab Exercise-Control Flow
# Question 1- 5-3 Do it yourself
# Imagine an alien was just shot down in a game. Create a variable
# called alien_color and assign it a value of 'green', 'yellow', or 'red'.

# Part 1: Write an if statement to test whether the alien's color is green. If it is,
# print a message that the player just earned 5 points.
alien_color = ['green', 'red', 'yellow']
if 'green' in alien_color:
    print('Congratulations! You earned 5 points!')

# Part 2: Write one version of this program that passes the if test and another
# that fails. (The version will have no output).
if 'yellow' in alien_color:
    print('Your alien leveled up!')
if 'pink' in alien_color:
    print('Your alien is pink')

# Question 2: Try it yourself 5-4
# Choose a color for an alien and write an if else statement
# Part 1
if 'pink' in alien_color:
    print(' Congratulations! You earned 5 points!')
else:
    print('Your alien is now pink')


# Part 2
# If the alien's color isn't green, print a statement that the player just earned 10 points
if 'red' in alien_color:
    print("Congratulations! You've earned 10 points!")
elif 'yellow' in alien_color:
    print("Congratulations! You've earned 10 points!")

# Part 3
# Write one version of this program that runs the if block and another that runs the else block
# if block


def if_version():
    alien_colors1 = ['Green', 'Yellow', 'Red']
    if 'Green' in alien_colors1:
        print("Your alien is green. His name is Alan.")
    if 'Red' in alien_colors1:
        print("Your alien is red. His name is Stu.")
    if 'Yellow' in alien_colors1:
        print("Your alien is yellow. His name is Phil.")


if_version()


# else block
def else_version(alien_color2):
    if alien_color2 == ['Green', 'Yellow', 'Red']:
        print("Your Alien is green. His name is Alan.")
    else:
        print("Your alien is a goner.")


else_version('pink')


# Question 3: Try it yourself 5-5
# Turn your if-else statement chain from 5-4 into an if-elif-else chain
# If the alien is green print a message that says the player earned 5 points
def green_alien():
    alien_color_1 = 'green'
    if 'green' in alien_color_1:
        print("Your alien is green. You have earned 5 points!")
    elif 'yellow' in alien_color_1:
        print("You have earned 10 points.")
    elif 'red' in alien_color_1:
        print("You have earned 15 points.")
    else:
        print('Your alien is a goner.')

green_alien()

def yellow_alien():
    alien_color_2 = 'yellow'
    if 'yellow' in alien_color_2:
        print("Your alien is yellow. You've earned 10 points!")
    elif 'green' in alien_color_2:
        print("You have earned 5 points.")
    elif 'red' in alien_color_2:
        print("You have earned 5 points.")
    else:
        print('Your alien is a goner.')


yellow_alien()

def red_alien():
    alien_color_3 = 'red'
    if 'red' in alien_color_3:
        print("Your alien is red. You've earned 15 points!")
    elif 'green' in alien_color_3:
        print("You've earned 10 points.")
    elif 'yellow' in alien_color_3:
        print("You've earned 5 points.")
    else:
        print("Your alien is a goner.")


red_alien()


# Question #4
# Try it yourself 5-6
# Write an if-elif-else chain that determines a person's stage of life. Set a value for the variable 'age' and then:
# If the person is less than 2 years old, print a message that hte person is a baby
def stage_life():
    age = 12
    if age < 2:
        print('This person is a baby.')
    elif age <= 2 and age < 4:
        print('This person is a toddler.')
    elif age <= 4 and age < 13:
        print('This person is a kid.')
    elif age <= 13 and age < 20:
        print('This person is a teenager.')
    elif age <= 20 and age < 65:
        print('This person is an adult.')
    elif age > 65:
        print('This person is an elder.')


stage_life()


# Question #5
# Write a function that takes an argument. Check this argument to see if it is a Boolean using the bool method.
# Call the method and use the below values as your argument. Using comments, provide the name of the argument and
# if it was true or false from running the code.

def q5_question(arg1):
    print(bool(arg1))


q5_question(10)
