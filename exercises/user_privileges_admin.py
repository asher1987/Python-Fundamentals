# User class
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


# Admin class

class Admin(User):

    def __init__(self, first_name, last_name, major, advisor_name, student_standing):
        super().__init__(first_name,last_name, major, advisor_name, student_standing)
        self.privileges = ['can delete users', 'can add users', 'can reset passwords']

    def show_privileges(self):
        for privilege in self.privileges:
            print('Only an admin can do', self.privileges)


# Privileges
class Privileges ():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print({privilege})