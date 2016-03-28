import unittest

from . import pointPattern
from . import point


class TestPointPattern(unittest.TestCase):
    def setUp(self):
        #initilize points into point pattern
        self.pointPattern = pointPattern.PointPattern(); #create list
        #now add points into that list
        self.pointPattern.add_point(point.Point(1,1,'lavender'))
        self.pointPattern.add_point(point.Point(2,2,'orange'))
        self.pointPattern.add_point(point.Point(3,3,'rose'))
        self.pointPattern.add_point(point.Point(4,4,'ash'))
        self.pointPattern.add_point(point.Point(5,5,'violet'))
        self.pointPattern.add_point(point.Point(1,1,'lavender'))
        self.pointPattern.add_point(point.Point(1,1,'lavender'))
        self.pointPattern.add_point(point.Point(1,1,'lavender'))

    def test_coin(self):
        self.assertEqual(self.pointPattern.coin_count(),4)

    def test_markList(self):
        self.assertEqual(self.pointPattern.mark_list(),['lavender','orange','rose','ash','violet'])

    def test_mark_subset(self):
        m1 = self.pointPattern.mark_subset('lavender')
        m2 = self.pointPattern.mark_subset('violet')
        self.assertEqual(len(m1),4)
        self.assertEqual(len(m2),1)

    def test_random_points(self):
        #check with user passed n
        l1 = self.pointPattern.create_n_random_points(5)
        self.assertEqual(len(l1),5)

        l2 = self.pointPattern.create_n_random_points()
        self.assertEqual(len(l2),8)

    def test_k_realizations(self):
        self.assertEqual(len(self.pointPattern.create_k_patterns(10)),10)


    def test_g_function(self):
        self.assertAlmostEqual(self.pointPattern.compute_g(10), 0.111, places=3)
        self.assertAlmostEqual(self.pointPattern.compute_g(50), 0.020, places=3)
        self.assertAlmostEqual(self.pointPattern.compute_g(100), 0.010, places=3)