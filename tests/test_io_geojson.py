import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))

from .. import io_geojson

class TestIoGeoJson(unittest.TestCase):

    def setUp(self):
        self.gj = io_geojson.read_geojson('data/us_cities.geojson')

    def test_read_geojson(self):
        self.assertIsInstance(self.gj, dict)

    def test_find_largest(self):
        city, pop = io_geojson.find_largest_city(self.gj)
        self.assertEqual(city, 'New York')
        self.assertEqual(pop, 19040000)

    def test_write_your_own(self):
        """
        Here you will write a test for the code you write in
        point_pattern.py.
        """
        avg_pop_max,avg_pop_min = io_geojson.write_your_own(self.gj)
        self.assertTrue(avg_pop_max,308473.3217503218)
        self.assertTrue(avg_pop_min,115237.50321750322)
