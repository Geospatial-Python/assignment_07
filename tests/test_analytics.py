import os
import sys
import unittest
import numpy
sys.path.insert(0, os.path.abspath('..'))

from .. import analytics

class TestAnalytics(unittest.TestCase):

  def setUp(self):
    self.permutations = analytics.permutations(666)
    self.random = analytics.create_random(666)

  def test_compute_critical(self):
  	test_batch = [2, 3, 100, 5, 401, 502, 44, 90]
  	self.lower, self.upper = analytics.compute_critical(test_batch)
  	self.assertTrue(self.lower == 2, self.upper == 502)

  def test_permutations(self):
    self.assertEqual(len(analytics.permutations(100)), 100)

  def test_create_random(self):
    self.assertEqual(len(self.random), 666)