# # Latest Restaurant class stored in a new module

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.served = 0

    def describe_restaurant(self):
        print('The name of this restaurant is', self.name, '.')
        print('This restaurant serves', self.cuisine)

    def open_restaurant(self):
        print(self.name, ' is open.')

    def set_number_served(self, number_served):
        self.served = number_served

    def increment_number_served(self, more_people):
        self.served += more_people
