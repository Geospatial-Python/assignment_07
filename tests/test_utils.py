import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))

from .. import utils as point_pattern

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
        x = point_pattern.getx(point)
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
        y = point_pattern.gety(point)
        self.assertEqual(2.5, y)

    def test_shift_point(self):
        """
        Test that a point is being properly shifted
         when calling point_pattern.shift_point
        """
        point = (0,0)
        new_point = point_pattern.shift_point(point, 3, 4)
        self.assertEqual((3,4), new_point)

        point = (-2.34, 1.19)
        new_point = point_pattern.shift_point(point, 2.34, -1.19)
        self.assertEqual((0,0), new_point)

    def test_check_coincident(self):
        """
        As above, update the function in point_pattern.py

        """
        point_a = (3, 7)
        point_b = (3, 7)
        coincident = point_pattern.check_coincident(point_a, point_b)
        self.assertEqual(coincident, True)

        point_b = (-3, -7)
        coincident = point_pattern.check_coincident(point_a, point_b)
        self.assertEqual(coincident, False)

        point_a = (0, 0)
        point_b = (0.0, 0.0)
        coincident = point_pattern.check_coincident(point_b, point_a)
        self.assertEqual(coincident, True)

    def test_check_in(self):
        """
        As above, update the function in point_pattern.py
        """
        point_list = [(0,0), (1,0.1), (-2.1, 1),
                      (2,4), (1,1), (3.5, 2)]

        inlist = point_pattern.check_in((0,0), point_list)
        self.assertTrue(inlist)

        inlist = point_pattern.check_in((6,4), point_list)
        self.assertFalse(inlist)

    def test_create_random_points(self):
        self.assertEqual(len(point_pattern.create_random_points(100)), 100)