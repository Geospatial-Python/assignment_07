import random
import unittest

import point

class TestPointPatternClass(unittest.TestCase):

	@classmethod
	def setUp(self):
		pass

class TestPointPatternClassImplementation(unittest.TestCase):
	@classmethod
#	Tests that the class sets the x and y attribute correctly
	def setUpClassCourdinates(self):
		self.pointPattern = pointPattern.PointPattern();
		#self.pointPattern.add_point(point.)