# Question #2: Try it yourself 9-11
# first_name, last_name, major, advisor_name, student_standing
from user_privileges_admin import Admin
from user_privileges_admin import Admin
ashley = Admin('Ashley', 'Likes', 'Cloud', 'Dajina', 'good')
ashley.describe_user()

ashley_privileges = ['can delete users', 'can add users', 'can reset passwords']
ashley.privileges.privileges = ashley_privileges

print(f"\n Ashley cannot do the following things:")
ashley.privileges.show_privileges()






