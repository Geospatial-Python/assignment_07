from .. import point 
from .. import analytics
from .. import utils


import unittest
import random

class Test_Point(unittest.TestCase):

    def test_points(self):

        """set up random x and y values for point instantiation"""
        random.seed(12345)
        rand_tup = (random.randint(0,10),random.randint(0,10))
        x_val = rand_tup[0]
        y_val = rand_tup[1]
        new_tup = (random.randint(0,10),random.randint(0,10))
        x_new = new_tup[0]
        y_new = new_tup[1]

        """check that point is created properly"""
        rand_point = point.Point(x_val, y_val, "random_mark") #(6,0,"random_mark")
        self.assertEqual(rand_point.x, 6)
        self.assertEqual(rand_point.y, 0)

        """check for whether the points are checking coincidence properly"""
        new_point = point.Point(x_new, y_new, "different_mark") #(4,5,"different_mark")
        self.assertTrue(rand_point.check_coincident(rand_point))
        self.assertFalse(rand_point.check_coincident(new_point))

        """check whether points can be shifted"""
        rand_point.shift_point(2,2) 
        self.assertEqual(rand_point.x, 8)
        self.assertEqual(rand_point.y, 2)
        
    def test_marks(self):
        
        random.seed(12345)
        marks = ['ying', 'yang', 'black', 'white']
        marked_points =[]
        for i in range(20):
            marked_points.append(point.Point(0,0, random.choice(marks)))
        
        ying_count = 0
        yang_count = 0
        white_count = 0
        black_count = 0
        for i in marked_points:
            if i.mark == 'ying':
                ying_count += 1
            if i.mark == 'yang':
                yang_count += 1
            if i.mark == 'black':
                black_count += 1
            else:
                white_count += 1
        self.assertEqual(ying_count, 3)
        self.assertEqual(yang_count, 7)
        self.assertEqual(black_count, 6)
        self.assertEqual(white_count, 14)
        
    def test_nearest_neighbor(self):
        random.seed(12345)
        marks = ['ying', 'yang', 'black', 'white']
        point_list = point.create_random_marked_points(20, marks)
        
        points_with_mark = point.average_nearest_neighbor_distance(point_list,
                marks) 
        points_without_mark = point.average_nearest_neighbor_distance(point_list)

        self.assertNotEqual(points_with_mark, 0.2, 5)
        self.assertAlmostEqual(points_without_mark,  0.11982627009007044, 1)
        

    def test_magic_methods(self):
        """check whether add and eq magic methods work"""
        new_point = point.Point(2,4)
        point_to_add = point.Point(3,6)
        added = new_point + point_to_add
        #This asserts that the add method worked as well as eq method
        self.assertEqual(added, point.Point(5,10))
        
        """check whether reverse adding works on random points"""
        point_list = point.create_random_marked_points(20)
        self.assertTrue(type(random.choice(point_list) +
            random.choice(point_list)), point.Point)

class Point_Pattern_Test(unittest.TestCase):
    
    def setUp(self):
        self.point_pattern = point.PointPattern()
        self.point_pattern.add_point(point.Point(3, 6, 'ying'))
        self.point_pattern.add_point(point.Point(9, 6, 'yang'))
        self.point_pattern.add_point(point.Point(3, 9, 'black'))
        self.point_pattern.add_point(point.Point(9, 6))
        
    def test_remove_point(self):
        length_after_removal = len(self.point_pattern) - 1
        self.point_pattern.remove_point(0)
        self.assertEqual(length_after_removal, len(self.point_pattern))

    def test_coincident(self):
        self.assertEqual(self.point_pattern.count_coincident(), 2)
    
    def test_list_marks(self):
        self.assertEqual(len(self.point_pattern.list_marks()), 4)
    
    def test_points_by_mark(self):
        self.assertEqual(len(self.point_pattern.points_by_mark('yang')), 1)

    def test_point_generation(self):
        self.assertEqual(len(self.point_pattern.generate_random_points(10)), 10)
        self.assertEqual(len(self.point_pattern.generate_random_points()), 4)

    def test_g(self):
        self.assertEqual(self.point_pattern.comupte_g(100), 0)

        
        



            
