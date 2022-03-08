# Lab Exercise-Numbers
# Try it Yourself 2-8
# Write addition, subtraction, multiplication, and division operations that each result in the number 8.
# Be sure to enclose your operations in print() calls to see the results. you should create four lines.
# Your output should be simply four lines with the number 8 each appearing once in each line.

print(5 + 3)
print(16/2)
print(16-8)
print(2*4)

# Try it Yourself 2-9
# Use a variable to represent your favorite number. Then, using the variable, create a message that
# reveals your favorite number. Print that message.

favorite_number = "3"
message = f"My favorite number is {favorite_number.title()}."
print(message)

# Question #2
# Assign variables to the following sets of numbers Use underscore to make them more readable. Write a function
# called number_sets and print each variable inside the function. Call each function to verify your results.


def number_sets():
    va = 456_234
    vb = 6_8423_791
    vc = 13_794_628
    vd = 96_374
    print(va)
    print(vb)
    print(vc)
    print(vd)


number_sets()

# Question #3
# Write a function that will take 2 arguments. Using type conversion, convert the first argument from int to float.
# Covert the second argument from float to int. Call the function and provide correct values for each argument
# to verify results. One argument should be a float and the other should be an int.


def q3_question(arg1, arg2):
    print("arg1 is being converted from an int to float:", float(arg1))
    print("arg2 is being converted from a float to an int:", int(arg2))


q3_question(10, 13.5)


# Question #4
# Write a function that will have two outputs. The first input method should ask "What is your favorite movie"
# the second output method should ask "How many times have you seen it?" The second input should be inside an int
# function. Each input method should be assigned to a variable. In a print statement using placeholders, the output
# result should be "I have seen {favorite movie}{number of times."


def favorite_movie():
    movie = input('What is your favorite movie?')
    times_seen = input('How Many times have you seen it?')
    message1 = 'My favorite movie is {0} and I have seen it {1} times'
    print(message1.format(movie, times_seen))


favorite_movie()



