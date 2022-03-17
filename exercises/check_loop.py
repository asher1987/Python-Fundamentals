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
    except ValueError:
        print('You can\'t use a string.')

sample_add()

# 10-7
while True:
    try:
        first = input('This first number is?:')
        if first == 'stop':
            break
        first = int(first)
        second = input('The second number is?:')
        if second == 'stop':
            break
        second = int(second)
    except ValueError:
        print('You can\'t use a string.')
    else:
        answer = first + second
        print(f'The answer is {answer}.')

