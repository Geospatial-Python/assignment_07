import os
import sys
import unittest
import random
sys.path.insert(0, os.path.abspath('..'))

from .. import analytics as point_pattern
from .. import point

class TestAnalytics(unittest.TestCase):

    def setUp(self):
        # Seed a random number generator so we get the same random values every time
        random.seed(12345)
        # A list comprehension to create 50 random points
        self.points = [(random.randint(0,100), random.randint(0,100)) for i in range(50)]
        self.gj = []

    def test_average_nearest_neighbor_distance(self):
        temp_points = [point.Point(random.randint(0,100), random.randint(0,100)) for i in range(20)]
        mean_d = point_pattern.average_nearest_neighbor_distance(temp_points)
        self.assertAlmostEqual(mean_d, 11.8949885, 5)

    def test_mean_center(self):
        """
        Something to think about - What values would you
         expect to see here and why?  Why are the values
         not what you might expect?
        """
        x, y = point_pattern.mean_center(self.points)
        self.assertEqual(x, 47.52)
        self.assertEqual(y, 45.14)

    def test_minimum_bounding_rectangle(self):
        mbr = point_pattern.minimum_bounding_rectangle(self.points)
        self.assertEqual(mbr, [0,0,94,98])

    def test_mbr_area(self):
        mbr = [0,0,94,98]
        area = point_pattern.mbr_area(mbr)
        self.assertEqual(area, 9212)

    def test_expected_distance(self):
        area = 9212
        npoints = 50
        expected = point_pattern.expected_distance(area, npoints)
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
        distance = point_pattern.euclidean_distance(point_a, point_b)
        self.assertAlmostEqual(2.8284271, distance, 4)

        point_a = (-1.25, 2.35)
        point_b = (4.2, -3.1)
        distance = point_pattern.euclidean_distance(point_a, point_b)
        self.assertAlmostEqual(7.7074639, distance, 4)

        point_a = (0, 0)
        point_b = (0, 0)
        distance = point_pattern.euclidean_distance(point_b, point_a)
        self.assertAlmostEqual(0.0, distance, 4)

    def test_manhattan_distance(self):
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
        distance = point_pattern.manhattan_distance(point_a, point_b)
        self.assertEqual(4.0, distance)

        point_a = (-1.25, 2.35)
        point_b = (4.2, -3.1)
        distance = point_pattern.manhattan_distance(point_a, point_b)
        self.assertEqual(10.9, distance)

        point_a = (0, 0)
        point_b = (0, 0)
        distance = point_pattern.manhattan_distance(point_b, point_a)
        self.assertAlmostEqual(0.0, distance, 4)

    def test_permutations(self):
        self.assertEqual(len(point_pattern.permutations(100)), 100)

    def test_find_criticals(self):
        crit_values = point_pattern.find_criticals([1, 2, 3, 4, 5, 6, 7])
        self.assertTrue(crit_values[0] == 1 and crit_values[1] == 7)

    def test_check_significance(self):
        self.assertTrue(point_pattern.check_significance(22, 4, 40))
        