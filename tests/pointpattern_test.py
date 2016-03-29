import unittest

from .. import PointPattern
from .. import point

class TestPointPattern(unittest.TestCase):
    def setUp(self):
        self.test = PointPattern()
        self.test.add_point(point.Point(2, 5, mark='North'))
        self.test.add_point(point.Point(4, 1, mark='North'))
        self.test.add_point(point.Point(2, 5, mark='South'))
        self.test.add_point(point.Point(1, 1))

    def check_coincident(self):
        self.assertEqual(self.test.count_coincident_points(), 2)

    def check_list_marks(self):
        self.assertEqual(self.test.list_marks(), ['North', 'South'])

    def check_return_subset(self):
        self.assertEqual(len(self.test.return_subset('South')), 2)

    def check_generate_points(self):
        self.assertEqual(len(self.test.create_random_points(20)), 20)

    def check_realizations(self):
        self.assertEqual(len(self.test.create_realizations(20)), 20)

    def check_critical_points(self):
        self.assertEqual(self.test.critical_points(), (1, 100))

    def check_g_function(self):
        self.assertAlmostEqual(self.test.compute_g(100), 1, places=4)