import random
import unittest

from .. import point

class TestFunctionalPointPattern(unittest.TestCase):

    def setUp(self):
        random.seed(12345)
        i = 0
        marks = ["elf", "dwarf", "human", "orc"]
        rand_marks = []
        for i in range(100):
            rand_marks.append(random.choice(marks))

        self.points = []
        while i < 100:
            seed = point.Point(round(random.random(),2), round(random.random(),2), rand_marks[i])
            self.points.append(seed)
            n_additional = random.randint(5,10)
            i += 1
            c = random.choice([0,1])
            if c:
                for j in range(n_additional):
                    x_offset = random.randint(0,10) / 100
                    y_offset = random.randint(0,10) / 100
                    pt = point.Point(round(seed.x + x_offset, 2), round(seed.y + y_offset,2), random.choice(marks))
                    self.points.append(pt)
                    i += 1
                    if i == 100:
                        break
            if i == 100:
                break

    def test_magic(self):
        random.seed(11223)
        list_of_rands = []
        rand_points = []
        for j in range(80):
            list_of_rands.append(random.randint(1,4))
        marks = ['r','b']
        for i in range(40):
            rand_points.append(point.Point(list_of_rands[i],list_of_rands[i+1],random.choice(marks)))

        point1 = point.Point(2,2,"yes")
        point2 = point.Point(2,2,"no")

        self.assertTrue(point1 == point2)

        direction = ""
        point3 = point.Point(3,3,"meh") #NE
        point4 = point.Point(1,1,"ok")  #SW
        self.assertEqual(point1>point2,"--") #coincident
        self.assertEqual(point1>point3, "SW") #point1 is sw of point3
        self.assertEqual(point1>point4, "NE") #point1 is NE of point3

        point5 = point.Point(-2,-2,"yes")
        point1_neg = -point1
        self.assertEqual(point5, point1_neg)

