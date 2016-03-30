import random
import unittest

import point

class TestPointClass(unittest.TestCase):

	@classmethod
	def setUp(self):
		pass




class TestPointClassImplementation(unittest.TestCase):
	@classmethod
#	Tests that the class sets the x and y attribute correctly
	def setUpClassCourdinates(cls):
	 	cls.test = point.Point(6,8)
	 	cls.assertEquals(cls.test.x,6)
	 	cls.assertEquals(cls.test.y,8)
	#	Tests that you can pass a coincident point to the coincident point checking method and return True, and pass a non-conicident point to return False.
	def test_coincident(cls):
		cls.test1 = point.Point(6,8)
		cls.test2 = point.Point(2,3)
		coincident1 = cls.test1.check_coincident(cls.test1)
		#coincident2 = point.check_coincident(cls.test1, cls.test2)
		cls.assertTrue(coincident1)
		#cls.assertFalse(coincident2)
#	Tests that you can shift the points in some arbitrary direction correctly.
	def test_shift(cls):
		cls.test1 = point.Point(6,8)
		cls.test2 = point.Point(10,12)
		shifted = cls.test1.shift_point(4,4)
		coincident1 = cls.test1.check_coincident(cls.test1)
		#coincident2 = point.check_coincident(shift1, (cls.test1.x+4,cls.test1.x+3))
		#coincident3 = point.check_coincident(cls.test2, (cls.test1.x+4,cls.test1.x+4))
		
		#print(shift1)

		cls.assertTrue(coincident1)
		#cls.assertFalse(coincident2)
		#cls.assertFalse(coincident3)
	
	def test_marked(self):
		#		Seed a random number generator (see the functional test from last week if you are unsure how to do this).
		random.seed(6969)
		#		Create a list of marks, e.g. marks = ['red', 'blue'] (please use something different than red/blue).
		self.marks = ['Bill', 'Ahmad', 'Johnson', 'Something']
		#		Use random.choice to randomly select a mark and instantiate maybe 10 or 20.
		markList = list()
		for x in range(10):
			markList.append(random.choice(self.marks))
		#		Create a list of your points and maybe count the number of times each mark comes up.
		markCounter = dict()
		for x in range(len(markList)):
			i = 1
			for y in range(len(markList)):
				if markList[y] == markList[x]:
					i = i+1
				else:
					continue
			markCounter[markList[x]] = i - 1

		#		Assert that the count is the same every time.
		self.assertTrue(markCounter['Bill'], 3)

	#Be sure to write a test for each magic method that you implement. In fact, write the test first, then write the magic method.
	def test_magic(self):
		p1 = point.Point(6,8)
		p2 = point.Point(10,12)
		self.assertTrue(p1  == p1)
		self.assertFalse(p1  == p2)

		p3 = point.Point(4,4)
		self.assertTrue(p1+p3  == p2)

		p4 = point.Point(-6,-8)
		self.assertTrue(-p1  == p4)