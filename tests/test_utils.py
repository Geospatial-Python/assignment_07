import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))

from .. import utils

class TestUtils(unittest.TestCase):

    def setUp(self):
        pass

    def test_getx(self):
        """
        A simple test to ensure that you understand how to access
        the x coordinate in a tuple of coordinates.
        You do not need to make any changes to this test,
        instead, in point_pattern.py, you must complete the
        `getx` function so that the correct
        values are returned.
        """
        point = (1,2)
        x = utils.getx(point)
        self.assertEqual(1, x)

    def test_gety(self):
        """
        As above, except get the y coordinate.
        You do not need to make any changes to this test,
        instead, in point_pattern.py, you must complete the
        `gety` function so that the correct
        values are returned.
        """
        point = (3,2.5)
        y = utils.gety(point)
        self.assertEqual(2.5, y)

    def test_shift_point(self):
        """
        Test that a point is being properly shifted
         when calling point_pattern.shift_point
        """
        point = (0,0)
        new_point = utils.shift_point(point, 3, 4)
        self.assertEqual((3,4), new_point)

        point = (-2.34, 1.19)
        new_point = utils.shift_point(point, 2.34, -1.19)
        self.assertEqual((0,0), new_point)



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
        distance = utils.manhattan_distance(point_a, point_b)
        self.assertEqual(4.0, distance)

        point_a = (-1.25, 2.35)
        point_b = (4.2, -3.1)
        distance = utils.manhattan_distance(point_a, point_b)
        self.assertEqual(10.9, distance)

        point_a = (0, 0)
        point_b = (0, 0)
        distance = utils.manhattan_distance(point_b, point_a)
        self.assertAlmostEqual(0.0, distance, 4)

    def test_check_coincident(self):
        """
        As above, update the function in point_pattern.py
        """
        point_a = (3, 7)
        point_b = (3, 7)
        coincident = utils.check_coincident(point_a, point_b)
        self.assertEqual(coincident, True)

        point_b = (-3, -7)
        coincident = utils.check_coincident(point_a, point_b)
        self.assertEqual(coincident, False)

        point_a = (0, 0)
        point_b = (0.0, 0.0)
        coincident = utils.check_coincident(point_b, point_a)
        self.assertEqual(coincident, True)

    def test_check_in(self):
        """
        As above, update the function in point_pattern.py
        """
        point_list = [(0,0), (1,0.1), (-2.1, 1),
                      (2,4), (1,1), (3.5, 2)]

        inlist = utils.check_in((0,0), point_list)
        self.assertTrue(inlist)

        inlist = utils.check_in((6,4), point_list)
        self.assertFalse(inlist)

    def test_generate_random_points(self):

        rand_points = utils.generate_random_points(20)
        self.assertEqual(20, len(rand_points))

    def test_permutation(self):

        permutations = utils.permutation(88)
        self.assertEqual(len(permutations), 88)
        self.assertNotEqual(permutations[0], permutations[1])

    def test_critical_points(self):

        avg_des_list = [0.5,0.001,0.2,0.9,0.91]
        lower,upper=utils.critical_points(avg_des_list)
        self.assertEqual(0.001, lower)
        self.assertEqual(0.91, upper)

    def test_is_observed_distance_significant(self):
        lower,upper=(0.1,0.5)
        result=utils.is_observed_distance_significant(lower,upper,0.51)
        self.assertTrue(result)
