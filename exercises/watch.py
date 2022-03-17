# Using your Horse Objects from the Encapsulation exercise, create your 2 child objects from the OOP section of the
# previous class. Use the property decorator for your child objects. Put both children objects
# inside your horse.py file.
class MyWatch:
    def __init__(self, size, color, weight):
        self._size = size
        self._color = color
        self._weight = weight

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight


ashley_watch = MyWatch('small', 'pink', 'light')
print('Ashley\'s watch is  {0}.'.format(MyWatch.weight))


class PocketWatch (MyWatch):
    def __init__(self, size, color, weight, type):
        super().__init__(size, color, weight)
        self._type = type # underscore makes the value protected

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type


pocket_watch = PocketWatch('small', 'grey', 'heavy', 'pocket watch')
print('Ashley\'s child watch is a {0}.'.format(PocketWatch._type))

# child number 2


class StopWatch (MyWatch):
    def __init__(self, size, color, weight, lanyard):
        super().__init__(size, color, weight)
        self._lanyard = lanyard  # underscore makes the value protected

    @property
    def lanyard(self):
        return self._lanyard

    @lanyard.setter
    def lanyard(self, lanyard):
        self._lanyard = lanyard


stop_watch = StopWatch('large', 'red', 'light', 'blue lanyard')
print('Ashley\'s child watch 2 has {0}.'.format(StopWatch._lanyard)) # takes child horse breed and puts it in the
# place holder.