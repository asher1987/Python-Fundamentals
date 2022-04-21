# Ashley's Online Store Project
# This store will sell snacks and drinks.

user_cart = {}
print('Welcome to Ashley\'s online store! To begin, pick out what you would like to purchase. When complete, '
      'type "check out".')
stock = {'Mountain Dew': 10, 'Water': 6, 'Strawberry Pop': 12, 'Pretzels': 10, 'Popcorn': 3, 'Chips': 4}
print('These are the items we have in stock')
[print(key, ':', value) for key, value in stock.items()]
answer = (input('Please choose your first item:'))







