import unittest

from ..point_pattern import PointPattern
from ..point import Point


class TestPointPattern(unittest.TestCase):
    def setUp(self):
        self.point_pattern = PointPattern()
        self.point_pattern.add_point(Point(5, 6, color='red'))
        self.point_pattern.add_point(Point(6, 5, color='orange'))
        self.point_pattern.add_point(Point(5, 6, color='orange'))
        self.point_pattern.add_point(Point(5, 6))

    def test_coincident(self):
        self.assertEqual(self.point_pattern.count_coincident(), 3)

    def test_list_marks(self):
        self.assertEqual(self.point_pattern.list_marks(), ['red', 'orange'])

    def test_find_subset_with_mark(self):
        self.assertEqual(len(self.point_pattern.find_subset_with_mark('orange')), 2)
        self.assertEqual(len(self.point_pattern.find_subset_with_mark('red')), 1)

    def test_generate_random(self):
        # First test does not pass in n, making n = length of current point pattern.
        self.assertEqual(len(self.point_pattern.generate_random_points()), 4)
        # Second test explicitly passes in n.
        self.assertEqual(len(self.point_pattern.generate_random_points(10)), 10)

    def test_generate_realizations(self):
        self.assertEqual(len(self.point_pattern.generate_realizations(100)), 100)