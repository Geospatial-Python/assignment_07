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
        self.assertAlmostEqual(points_without_mark,  0.11982627009007044, 2)
        


            
