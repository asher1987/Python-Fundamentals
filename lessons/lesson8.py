# Lesson 8 Collections

# list collection
# Ordered collection that can be changable and allow multiple duplicates
# and uses square brackets to define the collected data
# strings
colors = ['red', 'blue', 'green', 'purple', 'magenta', 'black',
          'white', 'orange']
# numbers
sizes = [42, 32, 156, 89, 34, 23, 8, 19]

# mixture of strings and numbers
mixed = [23, 'happy', 'python', 90, 45, 'snow', 'car', 56]
# direct print
def simple_print():
    print(colors)


# simple_print()


# print 1 iten
def simple_single():
    print(sizes[3])


# simple_single()


# for loop of list
def simple_for_print():
    for mix in mixed:
        print(mix)


# simple_for_print()

# range of the list
# range of values in a list is the same as it is in strings
def simple_range():
    print(colors[2:5])
    print(colors[-5:-2])


# simple_range()


# using len to get the length of a list
def simple_length():
    my_colors = len(colors)
    print(len(colors))
    value = 0
    while value < my_colors:
        print(colors[value])
        value += 1


# simple_length()

# using in keyword to search a list for the item
def simple_search():
    if 89 in sizes:
        print('89 is in the list')
    else:
        print( '89 is not in the list')


# simple_search()


# Append and insert to a list
# append will insert at the end of the list
def simple_append():
    mixed.append('Friday')
    for mix in mixed:
        print(mix)


# simple_append()

# insert will allow you to insert at a specific index position
def simple_insert():
    mixed.insert(3, 'Friday')
    for value in mixed:
        print(value)


# simple_insert()

# Removing items from a list by the remove(), pop(), del and clear()
# The remove function will remove from a specified value from the list
def simple_remove():
    colors.remove('green')
    for color in colors:
        print(color)


# simple_remove()


# The pop method will remove an item from a specified index
# not picking an index will take the last item
def simple_pop():
    colors.pop(5)
    for value in colors:
        print(value)


# simple_pop()

# the del keyword can remove a value at a specific index, and
# can also delete the list entirely. It's a keyword not a function.
def simple_del():
    del colors[3]
    for color in colors:
        print(color)


# simple_del()

# del with no index
# this statement is invalid because when we used the del keyword, the entire list was deleted
def simple_del_none():
    truck1 = ['chevy', 'ford', 'dodge']
    del truck1
    truck1.append('Toyota')
    for value in truck1:
        print(value)


# simple_del_none()

# clear method will empty a list, but not remove the list
# so you could delete the contents but still add to it.
def simple_clear():
    mixed.clear()
    mixed.append('Python')
    for mix in mixed:
        print(mix)


# simple_clear()


# list operations: concatenation, repeat, membership, and iterate
# Concatenation
def simple_join():
    values1 = [1, 2, 3, 4]
    values2 = [5, 6, 7, 8]
    total = values1 + values2
    for val in total:
        print(val)


# simple_join()

# repeat will repeat a list a certain amout of times
def simple_repeat():
    values = [1, 2, 3]
    print(values * 3)


# simple_repeat()



# membership
def simple_membership():
    result = 'red' in colors
    print(result)


# simple_membership()

# iterate
def simple_iterate():
    for color in colors:
        print(color, end=' ')


# simple_iterate()


# The Tuple Collection
# ordered collection that can not be changed.
my_fruits = ('apple', 'banana', 'cherry', 'orange')
# print(my_fruits)


def simple_tuple():
    for fruit in my_fruits:
        print(fruit)

    print(my_fruits[-3:-1])


# simple_tuple()


# Change a value in a tuple, by converting to list then back again
def simple_change_tuple():
    fruity = list(my_fruits)
    fruity.append('peach')
    my_fruit = tuple(fruity)
    for fruit in my_fruit:
        print(fruit)


# simple_change_tuple()


# Part 2 of collections with Set and Dictionary
# set collection
# This collection is an unordered and unindexed. This means
# the order of the items vary
ice_cream = {'chocolate', 'vanilla', 'strawbeery', 'neopolitain',
             'chocolate chip', 'Rocky Road', 'cookie dough'}

def simple_set():
    for flavor in ice_cream:
        print(flavor)


# simple_set()

# adding items to a set can be done by add() and update()
# add method
def simple_set_add():
    ice_cream.add('bunny tracks')
    for value in ice_cream:
        print(value)


# simple_set_add()

# update method
def simple_set_update():
    ice_cream.update({'butter pecan', 'bunny tracks', 'peanut butter cup'})
    for flavor in ice_cream:
        print(flavor)


# simple_set_update()

# removing items can be done in three ways: remove(), discard(), pop()
# remove will generate an error if the item being removed does not exist
def simple_set_remove():
    num_windows = {34, 23, 78, 98, 37}
    num_windows.remove(98)
    for num in num_windows:
        print(num)


# simple_set_remove()

# discard will remove without generating an error
# if the value is not in the list

def simple_set_discard():
    letters = {'a', 'b', 'c', 'd', 'e', 'f'}
    letters.discard('a')
    for letter in letters:
        print(letter)


# simple_set_discard()

# pop will remove the last item from the list so you don't know what it is

def simple_set_pop():
    letters = {'a', 'b', 'c', 'd', 'e', 'f'}
    letters.pop()
    for alpha in letters:
        print(alpha)


# simple_set_pop()

# joining set collections by update, union and the | operator
even = {2, 4, 6, 8, 10}
odd = {1, 3, 5, 7, 9}
tens = {10, 20, 30, 40, 50}


# update
def simple_set_join():
    even.update(odd)
    for num in even:
        print(num)

# simple_set_join()

# union
def simple_set_union():
    value = tens.union(odd)
    for item in value:
        print(item)


# simple_set_union()

# | operator
def simple_set_pipe():
    numbers = odd | even | tens
    for val in numbers:
        print(val)


# simple_set_pipe()

# Dictionaries are collections consisting of a key and value
# the key is unique anc cannot be duplicated making in immutable
# the value however can be duplicated. Defined using {}
trucks = {101: 'silverado', 102: 'f150', 103: 'ram'}
# print(trucks)
# print(trucks[102])
# print(trucks.get(103))

# This is add and update
# trucks[104] = 'titan'
# trucks[102] = 'f250'
# print(trucks)


# Looping through lists: basic print
def simple_dict_loop():
    for truck in trucks:
        print(truck)


# simple_dict_loop()


# loop using the [ ]
def simple_dict_square():
    for truck in trucks:
        print(trucks[truck])


# simple_dict_square()

# loop using values method
def simple_dict_values():
    for some in trucks.values():
        print(some)


# simple_dict_values()

# loop getting both key and value using .items (method)
def simple_dict_both():
    for able, beta in trucks.items():
        print(able, ' - ', beta)


# simple_dict_both()

# nested dictionaries refer to having a dictionary within a dictionary
my_pallet = {'color': {'primary': 'red', 'secondary': 'maroon'},
             'color2': {'primary': 'blue', 'secondary': 'royal'}}


def simple_dict_multi():
    for col1, col2 in my_pallet.items():
        print(col1, ' _ ', col2)


simple_dict_multi()
























