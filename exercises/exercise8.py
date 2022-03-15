# Lab Exercise-Collections
# Question 1: Try it yourself 5-8 and 5-9.
# Try it yourself 5-8
# Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a
# greeting such as "Hello admin. Would you like to see a status report?" and print each greeting for the users.
usernames = ['alikes', 'ablencoe', 'akissinger', 'ascott', 'admin']
for user_name in usernames:
    if user_name == 'admin':
        print("Hello admin. Everything is one fire.")
    else:
        print("Hello", user_name, ". Everything is fine")

# Try it yourself 5-9
# Add an if test to hello_admin.py to make sure the list of users is not empty.
# If the list is empty, print hte message, "We need to find some users!"
# Remove all of the usernames from the list, and make sure the correct message is printed.
# I wasn't sure if I should delete the values from above or make another one without values.

usernames_1 = []
if usernames_1:
    for user_name1 in usernames_1:
        if user_name1 == 'admin':
            print('Hello admin. Everything is on fire.')
else:
    print("We need to find some users!")

# Question 2: Try it yourself 5-10
current_users = ['anasteroid', 'Astar', 'agalaxy', 'Auniverse', 'aplanet']
new_users = ['anasteroid', 'Astar', 'acrater', 'amoon', 'Asun']
lower_case_users = [user.lower() for user in current_users]
for new_user1 in new_users:
    if new_user1.lower() in lower_case_users:
        print("The username:", new_user1, "is not available.")
    else:
        print("The", new_user1, "is available.")

# Question number 3: Try it yourself 5-11
# 5-11: Ordinal numbers indicate their position in a list, such as first or second.
# Most ordinal numbers end in th, except 1, 2, and 3.
# Store the numbers 1-9 in a list.
# Loop through the list.
# Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.
# Your output should read: 1st, 2nd, 3rd etc.
# Each result should be on a separate line.

ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for ordinal in ordinal_numbers:
    if ordinal == 1:
        print('1st')
    elif ordinal ==2:
        print('2nd')
    elif ordinal == 3:
        print('3rd')
    else:
        print(ordinal, 'th')

# Question #4: Try it yourself 6-1
# Use a dictionary to store information about a person you know. Store their first, and last name, age
# and the city they live in. Print each piece of information.
husband_info = {'first.name': 'Andrew', 'last.name': 'Likes', 'age': 34, 'city': 'Independence'}
print(husband_info['first.name'])
print(husband_info['last.name'])
print(husband_info['age'])
print(husband_info['city'])

kid_info1 = {'first.name': 'Aiden', 'last.name': 'Likes', 'age': 9, 'city': 'Manhattan'}
kid_info2 = {'first.name': 'Adelynn', 'last.name': 'Likes', 'age': 6, 'city': 'Wichita'}
people = (husband_info, kid_info1, kid_info2)
for person in people:
    first_name = person['first.name']
    last_name = person['last.name']
    age = person['age']
    city = person['city']
    print(first_name, last_name, 'is', age, 'years old and was born in', city, ',' ' Kansas.')

