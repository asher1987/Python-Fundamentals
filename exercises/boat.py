# In your boat.py file, write your boat object using your notes from the Intro to Programming class.
# Refine your attributes for your constructor.
# Utilize the property() along with the getter and setter for each of your variable attributes.
# Be sure to test your class and properties.
class Boat:
    def __init__(self, color='blue'):
        self._color = color

    # getter method
    def get_color(self):
        return self._color

    # setter method
    def set_color(self, x):
        self._age = x


ashley = Boat()

print(ashley.get_color())
print(ashley._color)


#property
class Boat:
    def __init__(self):
        self._color = 'blue'

    def get_color(self):
        return self._color

    def set_color(self, y):
        self._age = y

    color = property(get_color, set_color)

ashley = Boat()
ashley.color = 'blue'

ashley = Boat()
print(ashley.get_color())
print(ashley._color)