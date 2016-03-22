#Point class
import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from . import utils


class Point(object):

	def __init__(self, x, y, mark={}):
		self.x = x
		self.y = y
		self.mark = mark

	def __str__(self):
		return ("({0}, {1}").format(self.x, self.y)

	def check_coincident(self, test):
		return utils.check_coincident((self.x, self.y), test)

	def shift_point(self, x_shift, y_shift):
		point = (self.x, self.y)
		self.x, self.y = utils.shift_point(point, x_shift, y_shift)
