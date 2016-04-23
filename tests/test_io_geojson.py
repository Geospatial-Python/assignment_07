import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))

from .. import io_geojson, analytics

class TestIoGeoJson(unittest.TestCase):

    def setUp(self):
    	self.input_url = "https://api.myjson.com/bins/4587l"


    def test_read_geojson(self):
    	response = io_geojson.read_geojson(self.input_url)
    	largest_city = analytics.find_largest_city(response)
    	self.assertEqual(largest_city[0], "New York")