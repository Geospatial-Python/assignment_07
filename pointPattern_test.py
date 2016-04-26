import unittest
from . pointPattern import PointPattern
from .point import Point

class TestPointPattern(unittest.TestCase):
    def setUp(self):
        self.pointPattern = PointPattern()

        self.pointPattern.add(Point(2,8, mark = 'James'))
        self.pointPattern.add(Point(5,2, mark = 'Paul'))
        self.pointPattern.add(Point(7,3, mark = 'Sarah'))
        self.pointPattern.add(Point(6,4, mark = 'Michael'))
        self.pointPattern.add(Point(1,9, mark = 'Nancy'))
        self.pointPattern.add(Point(3,5, mark = 'Henry'))
        self.pointPattern.add(Point(7,3, mark = 'James'))
        self.pointPattern.add(Point(5,3, mark = 'James'))

    def test_coincidentPoints(self):
        self.assertEqual(self.pointPattern.coincidentPoints(), 1)

    def test_listMarks(self):
        self.assertEqual(self.pointPattern.listMarks(), ['James', 'Paul', 'Sarah', 'Michael', 'Nancy', 'Henry'])

    def test_subsetPoints(self):
        self.assertEqual(len(self.pointPattern.subsetPoints('Sarah')), 1)

    def test_randomPoints(self):
        self.assertEqual(len(self.pointPattern.randomPoints(8)), 8)

    def test_realizationsPoints(self):
        self.assertEqual(len(self.pointPattern.randomPoints(108)), 108)

    def test_gFunction(self):
        self.assertAlmostEqual(self.pointPattern.Gfunction(10), 20.5, places = 4)



