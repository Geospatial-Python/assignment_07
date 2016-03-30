import random
import unittest

import analytics  
import utils  
from point_pattern import PointPattern
from point import Point
class TestFunctionalPointPattern(unittest.TestCase):

    def setUp(self):
        self.marks=[]
        self.marks.append('r')
        self.marks.append('b')
        self.pattern=PointPattern()
        self.pattern.add_pt(Point(1,1,'r'))
        self.pattern.add_pt(Point(1,1,'r'))
        self.pattern.add_pt(Point(1,1,'r'))
        self.pattern.add_pt(Point(1,1,'r'))
        self.pattern.add_pt(Point(1,1,'r'))
        self.pattern.add_pt(Point(1,1,'r'))
        self.pattern.add_pt(Point(1,1,'r'))
        self.pattern.add_pt(Point(1,1,'r'))
        

        
        self.pattern.add_pt(Point(1,2,'b'))
        self.pattern.add_pt(Point(1,3,'b'))
        self.pattern.add_pt(Point(1,4,'b'))
        
    def test_num_coincident(self):
        self.assertEqual(self.pattern.number_coincident_points(),7)
        
    def test_list_mark(self):
        self.assertEquals(self.point_pattern.list_marks(),self.marks)
    
    def test_point_pattern(self):
        """
        This test checks that the code can compute an observed mean
         nearest neighbor distance and then use Monte Carlo simulation to
         generate some number of permutations.  A permutation is the mean
         nearest neighbor distance computed using a random realization of
         the point process.
        """
        random.seed(3673673)  # Reset the random number generator using system time
        # I do not know where you have moved avarege_nearest_neighbor_distance, so update the point_pattern module
        observed_avg = analytics.average_nearest_neighbor_distance(self.points)
        self.assertAlmostEqual(0.037507819095864134, observed_avg, 3)

        # Again, update the point_pattern module name for where you have placed the point_pattern module
        # Also update the create_random function name for whatever you named the function to generate
        #  random points
        rand_points = utils.create_n_rand_pts(100)
        self.assertEqual(100, len(rand_points))

        # As above, update the module and function name.
        permutations = analytics.p_perms(99)
        self.assertEqual(len(permutations), 99)
        self.assertNotEqual(permutations[0], permutations[1])

        # As above, update the module and function name.
        lower, upper = utils.critical_pts(permutations)
        self.assertTrue(lower > 0.03)
        self.assertTrue(upper < 0.07)
        self.assertTrue(observed_avg < lower or observed_avg > upper)

        # As above, update the module and function name.
        significant = analytics.monte_carlo_critical_bound_check(lower, upper, 0)
        self.assertTrue(significant)

        self.assertTrue(True)
        
    def test_marks(self):
        random.seed(942323)  # Reset the random number generator using system time
        # I do not know where you have moved avarege_nearest_neighbor_distance, so update the point_pattern module
        observed_avg = analytics.average_nearest_neighbor_distance(self.points)
        self.assertAlmostEqual(0.037507819095864134, observed_avg, 3)

        # Again, update the point_pattern module name for where you have placed the point_pattern module
        # Also update the create_random function name for whatever you named the function to generate
        #  random points
        rand_points = utils.create_marked_rand_pts(100,self.marks)
        self.assertEqual(100, len(rand_points))

        # As above, update the module and function name.
        permutations = analytics.p_perms_marks(99,self.marks)
        self.assertEqual(len(permutations), 99)
        #print(permutations)
        self.assertNotEqual(permutations[0], permutations[1])

        # As above, update the module and function name.
        lower, upper = utils.critical_pts(permutations)
        self.assertTrue(lower > 0.03)
        self.assertTrue(upper < 0.07)
        self.assertTrue(observed_avg < lower or observed_avg > upper)

        # As above, update the module and function name.
        significant = analytics.monte_carlo_critical_bound_check(lower, upper, 0)
        self.assertTrue(significant)

        self.assertTrue(True)
        