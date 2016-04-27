import os
import sys
import unittest
import random
sys.path.insert(0, os.path.abspath('..'))

from .. import analytics

class TestAnalytics(unittest.TestCase):

    def setUp(self):
        random.seed(12345)
        # A list comprehension to create 50 random points
        self.points = [(random.randint(0,100), random.randint(0,100)) for i in range(50)]


    def test_mean_center(self):
        """
        Something to think about - What values would you
         expect to see here and why?  Why are the values
         not what you might expect?
        """
        x, y = analytics.mean_center(self.points)
        self.assertEqual(x, 47.52)
        self.assertEqual(y, 45.14)

    def test_minimum_bounding_rectangle(self):
        mbr = analytics.minimum_bounding_rectangle(self.points)
        self.assertEqual(mbr, [0,0,94,98])

    def test_mbr_area(self):
        mbr = [0,0,94,98]
        area = analytics.mbr_area(mbr)
        self.assertEqual(area, 9212)

    def test_expected_distance(self):
        area = 9212
        npoints = 50
        expected = analytics.expected_distance(area, npoints)
        self.assertAlmostEqual(expected, 6.7867518, 5)

    def test_euclidean_distance(self):
        """
        A test to ensure that the distance between points
        is being properly computed.
        You do not need to make any changes to this test,
        instead, in point_pattern.py, you must complete the
        `eucliden_distance` function so that the correct
        values are returned.
        Something to think about: Why might you want to test
        different cases, e.g. all positive integers, positive
        and negative floats, coincident points?
        """
        point_a = (3, 7)
        point_b = (1, 9)
        distance = analytics.euclidean_distance(point_a, point_b)
        self.assertAlmostEqual(2.8284271, distance, 4)

        point_a = (-1.25, 2.35)
        point_b = (4.2, -3.1)
        distance = analytics.euclidean_distance(point_a, point_b)
        self.assertAlmostEqual(7.7074639, distance, 4)

        point_a = (0, 0)
        point_b = (0, 0)
        distance = analytics.euclidean_distance(point_b, point_a)
        self.assertAlmostEqual(0.0, distance, 4)