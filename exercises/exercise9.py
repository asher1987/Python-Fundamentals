# Classes and Functions
# Question 1: Try it yourself 8-3
# Write a function called make_shirt() that accepts a size and the text of a message
# that should be printed on the shirt. The function should print a sentence summarizing
# the size of the shirt and the message printed.
# Call the function once using positional arguments. Call it a second time using keyword args
from typing import List


def make_shirt(size, message):
    print('The shirt you ordered is a', size, 'and it says', message)


make_shirt('small', '"Rose All Day"')


make_shirt(size='small', message='"Rose All Day"')

# Question 1: Try it yourself 8-4
# Modify the make_shirt() function so that shirts are large by default with a message that reads
# I love Python. Make a large shirt and a medium shirt with the default message, and a shirt
# of any size with a different message.


def make_shirt1(size='large', message='I Love Python'):
    print('The shirt you ordered is a', size, 'and the message is', message)


make_shirt1()
make_shirt1(size='medium')
make_shirt1(size='small', message='Rose All Day')

# Question 1: Try it yourself 8-5
# Write a function called describe_city() that accepts the name of a city and its country.
# The function should print a simple sentence. Give the parameter for the country a defalut value.
# Call your function for three different cities, at least one of which is not the default country.


def describe_city(city_name, city_country='USA'):
    print(city_name, 'is in', city_country)


describe_city('Rose Hill')
describe_city('Derby')
describe_city('London', 'England')


# Question 2: Try it yourself 8-9
# 8-9: Make a list containing a series of short text messages. Pass the list to a function
# called show_messages(), which prints each text message.

def show_messages(text_message):
    for message in text_message:
        print(message)


text_messages = ['Today is Monday.', 'Tomorrow is Tuesday.', 'The following day is Wednesday.']
show_messages(text_messages)

# Try it yourself 8-10
# Start with a copy of your program from Exercise 8-9. Write a function called send_messages()
# that prints each text message and moves each message to a new list called sent_messages as it’s printed.
# After calling the function, print both of your lists to make sure the messages were moved correctly.


def show_messages(text_message):
    print('These are the text messages.')
    for message in text_message:
        print(message)


def send_messages(text_messages, sent_messages):
    print('These are the messages for sent messages.')
    while text_messages:
        draft_messages = text_messages.pop()
        print(draft_messages)
        sent_messages.append(draft_messages)


text_messages = ['Today is Monday.', 'Tomorrow is Tuesday.', 'The following day is Wednesday.']
sent_list = [text_messages]

sent_messages = []
send_messages(text_messages, sent_messages)
print(text_messages)
print(sent_messages)

# 8-11
send_messages(text_messages[:], sent_messages)

# Question 3: 9-1, 9-2, 9-3
# 9-1

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print('The name of this restaurant is', self.name)
        print('This restaurant serves', self.cuisine)


    def open_restaurant(self):
        print('This restaurant is open.')


restaurant = Restaurant('Freddy\'s', 'burgers' )
print(restaurant.name)
print(restaurant.cuisine)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2
restaurant1 = Restaurant('McDonalds', 'fries')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant2 = Restaurant('Arby\'s', 'curly fries')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()
restaurant3 = Restaurant('Braum\'s', 'ice cream')
restaurant3.describe_restaurant()
restaurant3.open_restaurant()


# 9-3
class User:
    def __init__(self, first_name, last_name, major, advisor_name, student_standing):
        self.name = first_name
        self.last = last_name
        self.major = major
        self.advisor = advisor_name
        self.standing = student_standing

    def describe_user(self):
        print('The student\'s first name is', self.name)

    def greet_user(self):
        print(f"\nWelcome, {self.name}, {self.last}! You are enrolled into {self.major}. Your advisor is "
              f"{self.advisor}. You are in {self.standing} standing.")


student1 = User('Ashley', 'Likes', 'Cloud Programming', 'Dajina Kiel', 'good')
student1.describe_user()
student1.greet_user()

student2 = User('Andrew', 'Likes', 'Business', 'Alex Harmon', 'good')
student2.describe_user()
student2.greet_user()

student3 = User('Aiden', 'Likes', '4th Grade', 'Mommy', 'good')
student3.describe_user()
student3.greet_user()