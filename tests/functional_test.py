import random
import unittest

from .. import point
from .. import analytics
from .. import io_geojson
from .. import utils



class TestFunctionalPointPattern(unittest.TestCase):

    def setUp(self):
        random.seed(123)
        self.marks=['red','blue','green']
        mark_list=[ random.choice(self.marks) for i in range(100)]
        random.seed(12345)
        i = 0
        self.points = []
        while i < 100:
            seed = (round(random.random(),2), round(random.random(),2))
            self.points.append(point.Point(seed[0],seed[1],mark_list[i]))
            n_additional = random.randint(5,10)
            i += 1
            c = random.choice([0,1])
            if c:
                for j in range(n_additional):
                    x_offset = random.randint(0,10) / 100
                    y_offset = random.randint(0,10) / 100
                    pt =point.Point(round(seed[0] + x_offset, 2), round(seed[1] + y_offset,2),mark_list[i])
                    self.points.append(pt)
                    i += 1
                    if i == 100:
                        break
            if i == 100:
                break
        #print([(points.x,points.y)for points in self.points])
    def test_point_pattern(self):
        """
        This test checks that the code can compute an observed mean
         nearest neighbor distance and then use Monte Carlo simulation to
         generate some number of permutations.  A permutation is the mean
         nearest neighbor distance computed using a random realization of
         the point process.
        """
        random.seed()  # Reset the random number generator using system time
        # I do not know where you have moved avarege_nearest_neighbor_distance, so update the point_pattern module
        observed_avg = analytics.average_nearest_neighbor_distance(self.points)
        self.assertAlmostEqual(0.027, observed_avg, 3)

        # Again, update the point_pattern module name for where you have placed the point_pattern module
        # Also update the create_random function name for whatever you named the function to generate
        #  random points
        rand_points = utils.generate_random_points(100)
        self.assertEqual(100, len(rand_points))

        # As above, update the module and function name.
        permutations = utils.permutation(99)
        self.assertEqual(len(permutations), 99)
        self.assertNotEqual(permutations[0], permutations[1])

        # As above, update the module and function name.
        lower, upper = utils.critical_points(permutations)
        self.assertTrue(lower > 0.03)
        self.assertTrue(upper < 0.07)
        self.assertTrue(observed_avg < lower or observed_avg > upper)

        # As above, update the module and function name.
        significant = utils.is_observed_distance_significant(lower, upper, observed_avg)
        self.assertTrue(significant)

        self.assertTrue(True)

    def test_mark_point_pattern(self):

        random.seed(12345)
        # I do not know where you have moved avarege_nearest_neighbor_distance, so update the point_pattern module
        observed_avg_red = analytics.average_nearest_neighbor_distance(self.points,self.marks[0])
        self.assertAlmostEqual(0.041, observed_avg_red, 3)

        observed_avg_blue = analytics.average_nearest_neighbor_distance(self.points,self.marks[1])
        self.assertAlmostEqual(0.045, observed_avg_blue, 3)
        observed_avg_green = analytics.average_nearest_neighbor_distance(self.points,self.marks[2])
        self.assertAlmostEqual(0.059, observed_avg_green, 3)

        # Again, update the point_pattern module name for where you have placed the point_pattern module
        # Also update the create_random function name for whatever you named the function to generate
        #  random points
        rand_points = utils.create_random_marked_points(100,self.marks)
        self.assertEqual(100, len(rand_points))

        # As above, update the module and function name.
        permutations = utils.permutation_mark(99,marks=self.marks)
        self.assertEqual(len(permutations), 99)
        self.assertNotEqual(permutations[0], permutations[1])

        # As above, update the module and function name.
        permutations = utils.permutation_mark(99,marks=self.marks,mark=self.marks[0])
        lower, upper = utils.critical_points(permutations)
        self.assertTrue(lower > 0.03)
        self.assertTrue(upper < 0.20)
        self.assertTrue(observed_avg_red < lower or observed_avg_red > upper)

        significant = utils.is_observed_distance_significant(lower, upper, observed_avg_red)
        self.assertTrue(significant)

        permutations = utils.permutation_mark(99,marks=self.marks,mark=self.marks[1])
        lower, upper = utils.critical_points(permutations)
        self.assertTrue(lower > 0.03)
        self.assertTrue(upper < 0.20)
        self.assertTrue(observed_avg_blue < lower or observed_avg_blue > upper)
        significant = utils.is_observed_distance_significant(lower, upper, observed_avg_blue)
        self.assertTrue(significant)


        permutations = utils.permutation_mark(99,marks=self.marks,mark=self.marks[2])
        lower, upper = utils.critical_points(permutations)

        self.assertTrue(lower > 0.03)
        self.assertTrue(upper < 0.20)
        self.assertTrue(observed_avg_green < lower or observed_avg_green > upper)
        significant = utils.is_observed_distance_significant(lower, upper, observed_avg_green)
        self.assertTrue(significant)

        self.assertTrue(True)