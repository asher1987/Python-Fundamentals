# Try it yourself 11-1
import unittest
def city_country(city, country):
    return f'{city}, {country}'
# I put this all in the same file, but I have the actual test in test_cities.py that I included.

# testing to see if this function works


class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        sample1 = city_country('Santiago', 'Chile')
        self.assertEqual(sample1, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()

# Question 2
# 11-2


def city_country(city, country, population):
    return f'{city}, {country}, {population}'