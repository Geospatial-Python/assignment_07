import unittest
import random

from .. import point

class TestPoint(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.test = point.Point(2,3)
		cls.test2 = point.Point(1,1)

	def test_setup(self):
		self.assertEqual(self.test.x, 2)
		self.assertEqual(self.test.y, 3)

	def test_coincident(self):
		coincident = self.test.check_coincident((2,3))
		self.assertTrue(coincident)
		coincident = self.test.check_coincident((4,2))	
		self.assertFalse(coincident)

	def test_shift(self):
		new_point = ((self.test.x + 2), (self.test.y + 4))
		self.test.shift_point(2, 4)
		self.assertEqual((self.test.x, self.test.y), new_point)

	#I did this part wrong, not 100% sure what is required for this test
	def test_marked(self):
		random.seed(12345)
		marks = ['North', 'East', 'South', 'West']
		temp = []
		dic = {}
		i = 0

		while i < 15:
			temp.append(random.choice(marks))
			i += 1

		for mark in marks:
			if mark not in dic:
				dic[mark] = 1
			else:
				dic[mark] += 1

		test1 = point.Point(0,0, dic)
		self.assertTrue(test1.mark['North'] == dic['North'])


	def test_magic_methods(self):
		#Checks the __ne__ magic method
		self.assertTrue(self.test != self.test2)

		#Checks the __eq__ magic method
		self.assertFalse(self.test == self.test2)

		#Checks the __add__ magic method
		self.assertEqual(self.test + self.test2, point.Point(3,4))