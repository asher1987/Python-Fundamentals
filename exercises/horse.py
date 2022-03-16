# Using your Horse Objects from the Encapsulation exercise, create your 2 child objects from the OOP section of the
# previous class. Use the property decorator for your child objects. Put both children objects
# inside your horse.py file.
class MyHorse:
    def __init__(self, size, color, gender):
        self.size = size
        self.color = color
        self.gender = gender

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size_value):
        self._size = size_value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def gender(self):
        return self._gender

    @gender
    def gender(self, gender):
        self._gender = gender


ashley_horse = MyHorse('brown', 'large', 'male')


class ChildHorse1 (MyHorse):
    def __init__(self, size, color, gender, breed):
        super().__init__(size, color, gender)
        self.breed = breed


@property
def breed(self):
    return self._breed


@breed.setter
def breed(self, breed):
    self._breed = breed


child_horse1 = MyHorse('brown', 'large', 'male', 'mustang')
print('Ashley\'s first child horse is a', self.breed)