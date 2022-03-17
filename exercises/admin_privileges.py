from user import User

class Admin(User):

    def __init__(self, first_name, last_name, major, advisor_name, student_standing):
        super().__init__(first_name,last_name, major, advisor_name, student_standing)
        self.privileges = ['can delete users', 'can add users', 'can reset passwords']

    def show_privileges(self):
        for privilege in self.privileges:
            print('Only an admin can do', self.privileges)


class Privileges ():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print({privilege})
