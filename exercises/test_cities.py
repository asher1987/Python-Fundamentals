# testing to see if this function works
import unittest
from exercise14 import city_country


class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        sample1 = city_country('Santiago', 'Chile')
        self.assertEqual(sample1, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()