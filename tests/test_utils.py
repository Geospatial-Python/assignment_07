import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))

from .. import utils

class TestUtils(unittest.TestCase):

  def setUp(self):
    self.points_a = (1,4)
    self.points_b = (1,4)


  def check_coincident(self):
    self.assertEqual(check_coincident(self.points_a), check_coincident(self.points_b))