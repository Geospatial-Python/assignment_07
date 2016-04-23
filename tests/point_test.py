import os
import sys
import random
from nose.tools import set_trace
import unittest
sys.path.insert(0, os.path.abspath('..'))

from .. import point

class TestPoint(unittest.TestCase):
  

  def setUp(self):
    self.x = 3
    self.y = 1
    self.marks = []

  def test_set_x_and_y_correctly(self):
    self.assertEqual(self.x, 3)
    self.assertEqual(self.y, 1)

  def test_should_catch_coincident_point(self):
    self.assertTrue(point.check_coincident(self, self))

  def test_should_catch_noncoincident_point(self):
    common_point = point.Point(1, 4, ['Pizza', 'BBQ', 'Calzones'])
    self.assertFalse(point.check_coincident(self, common_point))

  def test_shift_the_point(self):
    common_point = point.Point(1, 4, ['Pizza', 'BBQ', 'Calzones'])
    old_x = common_point.x
    new_x = point.shift_point(common_point, 1, 2)[0]
    self.assertNotEqual(old_x, new_x)

  def test_mark_creation(self):
    random_n = int(random.random() * 100)
    list_o_marks = ['Bernie Sanders', 'Ted Cruz', 'Donald Trump', 'Hillary Clinton', 'John Kasich', 'Jill Stein']
    random_mark = random.choice(list_o_marks)
    list_o_points = [point.Point(random.random(), random.random()) for i in range(random_n)]
    for p in list_o_points:
      p.mark = random_mark
    self.assertEqual(random_n, len(list_o_points))

  # def test_create_random_marked_points(self):
    # I can't for the life of me get this to work, may be staring at it for too long
    # set_trace()
    # point.create_random_marked_points(100, ['Water', 'Fire', 'Earth'])

  def test_should_add_points_with_magic(self):
    other_point = point.Point(300, 2, ["blurb"])
    self.assertEqual(self.x + other_point.x, 303)

  def test_should_subtract_points_with_magic(self):
    other_point = point.Point(300, 2, ["blurb"])
    self.assertEqual(self.x - other_point.x, -297)

  def test_should_divide_points_with_magic(self):
    other_point = point.Point(300, 2, ["blurb"])
    self.assertEqual(self.x / other_point.x, 0.01)


