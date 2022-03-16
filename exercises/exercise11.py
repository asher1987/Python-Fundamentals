# Question 1: On page 173 of your book, do 9-6 of the Try it Yourself. Put all your code in your exercise11.py file.
# 9-6
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


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type='ice cream.'):
           super().__init__(name, cuisine_type)
           self.flavors = []

    def ice_cream_flavors(self):
               for flavor in self.flavors:
                 print(flavor)


call_hall = IceCreamStand('Call Hall')
call_hall.flavors = ['vanilla', 'chocolate', 'strawberry']

call_hall.describe_restaurant()
call_hall.ice_cream_flavors()


# Question #2:
# Try it yourself 9-7
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


class Admin(User):

    def __init__(self, first_name, last_name, major, advisor_name, student_standing):
        super().__init__(first_name,last_name, major, advisor_name, student_standing)
        self.privileges = ['can delete users', 'can add users', 'can reset passwords']

    def show_privileges(self):
        for privilege in self.privileges:
            print('Only an admin can do', self.privileges)


instance_admin = Admin('ashley', 'likes', 'cloud', 'laura fowler', 'good')
instance_admin.describe_user()
instance_admin.show_privileges()


# Try it yourself 9-8
class Privileges ():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print({privilege})


my_user_admin =Admin('ashley', 'likes', 'cloud', 'laura fowler', 'good')
my_user_admin.describe_user()
my_user_admin.show_privileges()
# Write a separate Privileges class. The class should have one attribute, privileges
# that stores the string in 9-7. Move the show privileges method to this class.
# Make a Privileges instance as an attribute in the admin class.
# Create a new instance of admin and use your method to show its privileges
