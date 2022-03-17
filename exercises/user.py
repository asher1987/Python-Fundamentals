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


