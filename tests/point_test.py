from .. import point
from .. import utils

import unittest
import random

class TestPointClass(unittest.TestCase):

    def set_up(self):
        pass

    def test_set_xy(self):

        new_point=point.Point(1,1,'red')
        self.assertEqual(new_point.x, 1)
        self.assertEqual(new_point.y, 1)

    def test_coincident(self):

        new_point=point.Point(1,1,'red')
        peer_point=point.Point(1,1,'red')
        self.assertTrue(new_point.check_coincident(peer_point))
        peer_point=point.Point(1,2,'red')
        self.assertFalse(new_point.check_coincident(peer_point))

    def test_shift(self):

        new_point=point.Point(1,1,'red')
        new_point.shift_point(1,1)
        self.assertEqual(new_point.x, 2)
        self.assertEqual(new_point.y, 2)

    def test_magic_methods(self):

        new_point=point.Point(1,1,'red')
        peer_point=point.Point(1,1,'red')
        self.assertEqual(str(new_point), "x=1.000000,y=1.000000,mark=red")
        new_add_point=new_point+peer_point
        self.assertEqual(new_add_point.x, 2)
        self.assertEqual(new_add_point.y, 2)
        self.assertEqual(new_point==peer_point, True)

    def test_mark_points(self):

        random.seed(12345)
        marks=['red','yellow','blue','green']
        list_of_points = utils.create_random_marked_points(10,marks)
        sum_color_list=[0,0,0,0]
        for points in list_of_points:
            if points.mark=='red':
                sum_color_list[0]+=1
            elif points.mark=='yellow':
                sum_color_list[1]+=1
            elif points.mark=='blue':
                sum_color_list[2]+=1
            elif points.mark=='green':
                sum_color_list[3]+=1

        self.assertEqual(sum_color_list[0], 2)
        self.assertEqual(sum_color_list[1], 4)
        self.assertEqual(sum_color_list[2], 2)
        self.assertEqual(sum_color_list[3], 2)
