# Lab Exercise-Looping
# Question 1: Try it Yourself 4-3
# Use a for loop to print the numbers from 1-20, inclusive.
for numbers in range(1, 21):
    print(numbers)

# Question 2: Try it yourself 4-6
# Use the third argument of the range() function to make a list of the odd
# numbers from 1-20. Use a for loop to print each number.
odd = []
odd = list(range(1, 21, 2))
for number in odd\
        :
    print(number)

# Question 3: Try it yourself 4-7
# Make a list of the multiples of 3 from 3-30. Use a for loop to print the numbers in your list.
multiple_three = list(range(3, 31, 3))
for number in multiple_three:
    print(number)

# Question 4: Try it yourself 4-8
# A number raised to the third power is called a cube. For example, a cube of 2 is written as 2**3
# make a list of the first 10 cubes and use a for loop to print out the value of each cube.
third_power = []
for integers in range(1, 11):
    third_power.append(integers**3)
print(third_power)