# Lab Exercise-Strings

# Try it yourself 2-3
# Use a variable to represent a person's name, and print a message
# to that person. Your message should be simple.

first_name = 'Ashley'
print(f" Hi, {first_name.title()}! I hope you have a great day!")

# Try it yourself 2-4
# Use a variable to represent a person's name, and then print that person's name in lowercase, uppercase, and titlecase

name = 'Ashley'
print(name.upper())
print(name.lower())
print(name.title())

# Try it yourself 2-5
# Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look
# something like the following, including quotation marks
# Albert Einstein once said, "A person who never made a mistake never tried anything new."
# “Do extraordinary things with love.”

quote_name= 'mother teresa'
print(f'{quote_name.title()} once said, "Do extraordinary things with love."')

# Try it yourself 2-6
# Repeat exercise 2-5, but this time represent the famous person's name using a variable famous_person. Then
# compose your message and represent it with a new variable called message. Print your message.

famous_person = 'Mother Teresa'
message = f'{famous_person} once said, "Do extraordinary things with love."'
print(message)

# Try it yourself 2-7
# Use a variable to represent a person's name, and include some whitespace characters at the beginning
# and the end of the name. Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once so the whitespace around the name is displayed. Then print the name using each of the three
# stripping functions, lstrip(), rstrip(), and strip()

name_first = '\tAshley\n'
print(name_first)

# 1strip(), rstrip(), and strip()
print(name_first.rstrip())
print(name_first.strip())
print(name_first.lstrip())



