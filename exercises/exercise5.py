# Lab Exercise-Operators
# Question 1: Try it yourself 5-1
# Write a series of conditional tests. Print a statement describing each test
# and your prediction for the results of each test.

# Conditional Test 1 (True)
house = 'home'
print("Is house == 'home'? I predict true")
print(house == 'home')

# Conditional Test 2 (False)
house = 'apartment'
print(" Is house == 'Home'? I predict false because it is case sensitive")
print(house == 'Apartment')

# Conditional Test 3 (True)
house = 'mansion'
print(" Is house =='mansion'? I predict true.")
print( house == 'mansion')

# Conditional Test 4 (True)
ashley = 34
aiden = 10


def who_is_older():
    result1 = ashley > aiden
    print(" Is ashley older than aiden? I predict true.")
    print(result1)


who_is_older()

# Conditional Test 5 (False)
aiden = 9
adelynn = 6


def who_is_older():
    result2 = adelynn > aiden
    print(" Is adelynn older than aiden? I predict false.")
    print(result2)


who_is_older()


# Conditional Test 6 (False)
def who_is_older():
    result3 = adelynn >= ashley
    print(" Is adelynn the same age as ashley? I predict false.")
    print(result3)


who_is_older()

# Conditional Test 7 (True)
result4= ashley >= 21 and adelynn <=7
print("Is ashley older than 21? Is adelynn younger than 7? I predict true.")
print(result4)

# Conditional Test 8 (False)
result5= aiden >=10 and adelynn >=9
print(" Is aiden older than 10? Is adelynn older than 9? I predict false.")
print(result5)

# Conditional Test 9 (False)
favorite_color =['pink', 'purple']
print( "Is black one of Ashley's favorite colors? I predict false.")
print( 'black' in favorite_color)

# Conditional Test 10 (False)
color = 'yellow'
if color not in favorite_color:
    print("Is yellow one of Ashley's favorite colors? I predict false")
    print('yellow' in favorite_color)


# Try it yourself 5-2 Question 2

# Tests for equality with strings (True)
result3 = "Ashley Likes is a mom" == "Ashley Likes is a mom"
print("This is for equality with strings.Is Ashley Likes a mom? I predict true.")
print(result3)

# Tests for inequality with strings (False)
result4 = "Ashley Likes is a dad" != "Ashley Likes is a dad"
print("This is for inequality with strings. Is Ashley Likes a dad? I predict false.")
print(result4)

# Test using lower() method (True)
color = 'Yellow'
print("This is for the lower method:", color.lower == 'Yellow')

# Test using lower() method (False)
print("This is for the lower method:", 'Yellow' == color.lower)

# Numerical tests (False)
# equality
result6 = (ashley == aiden)
print("This is for the equality one:", result6)

# inequality (True)
result7 = (ashley != aiden)
print("This is for the inequality one:", result7)

# great than (True)
result8 = (ashley > aiden)
print("This is for the greater than one:", result8)

# less than (False)
result9 = (adelynn > aiden)
print("This is for the less than one:", result9)

# greater than or equal to (False)
result10 = (adelynn >= aiden)
print( "This is for the greater than or equal to one:", result10)

# less than or equal to (True)
result11 = (adelynn <= adelynn)
print("This is for the less than or equal to one:", result11)

# Test using keywords
# keyword and (True)
result12= aiden >=5 and adelynn >=5
print("This is for the 'and' keyword:", result12)

# keyword or (False)
result13= aiden >= 10 or adelynn >=10
print("This is for the 'or' keyword:", result13)

# Whether an item is on a list (True)
kids = ['Aiden', 'Adelynn']
print("Is Aiden one of Ashley's kids?", 'Aiden' in kids)

# Whether an item is not on a list (False)
print("Is Alex one of Ashley's kids?", 'Alex' in kids)

# Question 3: Write a function that takes two arguments. Inside the function
# provide examples of all the arithmetic operators. Provide a variable for
# each solution and print the results of each.


def ashley_kids(kid1, kid2):
    result1 = kid1 * kid2
    print(result1)


ashley_kids(9, 6)


def ashley_kids(kid1, kid2):
    result2 = kid1 / kid2
    print(result2)


ashley_kids(10, 2)


def ashley_kids (kid1, kid2):
    result3 = kid1 % kid2
    print(result3)


ashley_kids(20, 8)


def ashley_kids(kid1, kid2):
    result4 = kid1 ** kid2
    print(result4)


ashley_kids(6, 3)


# Question 4
# Write a function that takes one argument. Inside the function provide examples
# of assignment operators
# Modulus Equals
def assignment_operator(value):
    value %= 5
    print(value)


assignment_operator(10)


# exponent equals
def assignment_operator(value):
    value **= 5
    print(value)


assignment_operator(11)


# plus equals
def assignment_operator(value):
    value += 8
    print(value)


# minus equals
def assignment_operator(value):
    value -= 6
    print(value)


assignment_operator(12)








