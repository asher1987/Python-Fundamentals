# Using your Horse Objects from the Encapsulation exercise, create your 2 child objects from the OOP section of the
# previous class. Use the property decorator for your child objects. Put both children objects
# inside your horse.py file.
class MyHorse:
    def __init__(self, size, color, gender):
        self._size = size
        self._color = color
        self._gender = gender

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

    @gender.setter
    def gender(self, gender):
        self._gender = gender


ashley_horse = MyHorse('brown', 'large', 'male')


class Pony (MyHorse):
    def __init__(self, size, color, gender, breed):
        super().__init__(size, color, gender)
        self._breed = breed # underscore makes the value protected

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, breed):
        self._breed = breed


Pony = Pony('brown', 'large', 'male', 'mustang')
print('Ashley\'s pony is a {0}.'.format(Pony.breed)) # takes child horse breed and puts it in the
# place holder.

class Pony (MyHorse):
    def __init__(self, size, color, gender, breed):
        super().__init__(size, color, gender)
        self._breed = breed # underscore makes the value protected

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, breed):
        self._breed = breed


Pony = Pony('brown', 'large', 'male', 'mustang')
print('Ashley\'s pony is a {0}.'.format(Pony.breed)) # takes child horse breed and puts it in the
# place holder.

# child number 2


class Clydesdale (MyHorse):
    def __init__(self, size, color, gender, hoof_size):
        super().__init__(size, color, gender)
        self._hoof_size = hoof_size  # underscore makes the value protected

    @property
    def hoof_size(self):
        return self._hoof_size

    @hoof_size.setter
    def hoof_size(self, hoof_size):
        self._hoof_size = hoof_size


Clydesdale = Clydesdale('brown', 'large', 'male', 'large hooves')
print('Ashley\'s clydesdale has {0}.'.format(Clydesdale.hoof_size)) # takes child horse breed and puts it in the
# place holder.