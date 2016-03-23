
import unittest
#from point_pattern import PointPattern
#from point import Point

from point_pattern import PointPattern
from point import Point


class TestPointPattern(unittest.TestCase):
    def setUp(self):
        self.point_pattern = PointPattern()
        self.point_pattern.add_point(Point(1, 2, 'burrito'))
        self.point_pattern.add_point(Point(2, 1, 'burrito'))
        self.point_pattern.add_point(Point(1, 2, 'burger'))
        self.point_pattern.add_point(Point(1, 2))

    def test_coincident(self):
        self.assertEqual(self.point_pattern.num_of_coincident(), 2)

    def test_list_marks(self):
        self.assertEqual(self.point_pattern.list_marks(), ['burrito', 'burger'])

    def test_find_subset_with_mark(self):
        self.assertEqual(len(self.point_pattern.find_subset_with_mark('burrito')), 2)
        self.assertEqual(len(self.point_pattern.find_subset_with_mark('burger')), 1)

    def test_generate_random(self):
        self.assertEqual(len(self.point_pattern.generate_random_points()), 4)
        self.assertEqual(len(self.point_pattern.generate_random_points(10)), 10)

    def test_generate_realizations(self):
        self.assertEqual(len(self.point_pattern.generate_realizations(100)), 100)

    def test_compute_g(self):
        self.assertAlmostEqual(self.point_pattern.compute_g(10), 0.111, places=3)
        self.assertAlmostEqual(self.point_pattern.compute_g(100), 0.010, places=3)
        self.assertAlmostEqual(self.point_pattern.compute_g(1000), 0.001, places=3)
