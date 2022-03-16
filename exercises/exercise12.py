# On page 201 of your book, do  through 10-6 of the Try it Yourself. Put all your code in your exercise12.py file.
# One common problem when prompting for numerical input occurs when people provide text instead of numbers. When you
# try to convert the input to an int, you'll get a ValueError. Write a program that prompts for two numbers. Add them
# together and print the results. Catch the ValueError if either input value is not a number, and print a friendly error
# message. Test your program by entering two numbers and then by entering text instead of a number.

def sample_add():
    print('Let\'s add two numbers.')
    try:
        first = input('The first number is?')
        second = input('The second number is?')
        answer = int(first) + int(second)
        print(answer)
    except (ZeroDivisionError, ValueError):
        print('You can\'t use a string to add')


sample_add()

# Question 10-7

# Question 3:
# On page 202 of your book, do 10-8 of the Try it Yourself.
# Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three names
# of dogs in the second file. Write a program that tries to read these files and print the contents of the file to
# the screen. Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message
# if a file is missing. Move one of the files to a different location on your system, and make sure the code in the
# except block executes properly.

def multiple_files(filename):
    try:
        with open(filename) as f:
            animal_names = f.read()
    except FileNotFoundError:
        print(f'Ashley moved the {filename}  so you can\'t read it.')
    else:
        document_info = animal_names
        animal_names = len(document_info)
        print(f"The file {filename} has the following animal names in in: {animal_names}.")

    filename = 'cat.txt'
    multiple_files(filename)
    filenames = ['cat.txt', 'dog.text']
    for filename in filenames:
        multiple_files(filename)


# 10-9
# modify except block to fail silently
def multiple_files(filename):
    try:
        with open(filename) as f:
            animal_names = f.read()
    except FileNotFoundError:
        pass
     else:
        document_info = animal_names
        animal_names = len(document_info)
        print(f"The file {filename} has the following animal names in in: {animal_names}.")


filename = 'cat.txt'
multiple_files(filename)
filenames = ['cat.txt', 'dog.text']
for filename in filenames:
    multiple_files(filename)