#from utils import check_coincident
import utils
import numpy as np
#from .utils import *

class Point(object):

	#Create a point class with three attributes, x, y, and a keyword argument mark. Please place the point pattern class in point.py.
	def __init__(self, x, y, mark={}):
		self.x = x
		self.y = y
		self.mark = mark

	#Update your Point class to utilize at least 3 magic methods. You are free to choose what magic methods to implement.
	
	#check if the two objects are equal
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	#add the x and y courdinates of both objects
	def __add__(self,other):
		return Point(self.x + other.x,self.y + other.y)
	#negate the x and y courdinates of the point objects
	def __neg__(self):
		return Point(-self.x,-self.y,self.mark)

	#Add a method to the Point class to chec if another point, passed as an argument, is coincident. Remember that you already wrote this logic.
	def check_coincident(self,other):
		return utils.check_coincident((self.x, self.y), (other.x, other.y))

	#Add a method to shift the point in some direction. This logic is also already written.
	def shift_point(self, dx, dy):
		return utils.shift_point((self.x,self.y),dx,dy)

#Create a PointPattern class. This class should be able to compute statistics about your point pattern. It should be able to:
class PointPattern:

	#initialize an array of points as empty
	def __init__(self):
		self.points = []

	#Average nearest neighbor distance (with or without mark specification)
	def average_nearest_neighbor_distance(self, mark=None):
		return utils.average_nearest_neighbor_distance(self.points, mark)

	#Number of coincident points
	def num_coincident(self):
		count = 0
		coincidnet_list = []
		for i in range(len(self.points)):
			for j in range(len(self.points)):
				if i in coincidnet_list or i==j:
					continue
				if self.points[i] == self.points[j]:
					count = count+1
					coincidnet_list.append(j)
		return count
	
	#Add a point to the point list
	def add_point(self,point):
		self.points.append(point)

	#Remove a point from the point list
	def remove_point(self,index):
		del(self.points[index])

	#List the marks, for example if the points are marked 'r' and 'b', this should return ['r', 'b']
	def list_marks(self):
		markList = []
		for point in self.points:
			if point.mark not in markList:
				markList.append(point.mark)
		return markList

	#Return a subset of points by mark type
	def subset_by_mark(self, mark):
		subset = []
		for point in self.points:
			if point.mark == mark:
				subset.append(p)
		return subset

	#Generate n random points where n is either provided by the user or equal to the current size of the point pattern.
	def create_n_random_points(self,n =None):
		randos = create_random_marked_points(n = len(self.points),marks = [])
		return randos
	
	#Generate k realizations of random points. That is, simulate k random point patterns for use in Monte Carlo simulation.
	def create_k_patterns(self,k):
		return analytics.permutations(self.marks,k)

	#Return the critical points from the nearest neighbor simulation
	def critical_points(self):
		return analytics.compute_critical(self.create_k_patterns(99))

	#Add the ability to compute a G function on the point pattern class (more below).
	def compute_g(self, nsteps):
		ds = np.linspace(0, 100, nsteps)
		#nsteps is the number of discrete d that are used to compute G
		g_sum = 0

		for step in range(nsteps):
			o_i = ds[step]
			min_dis = None
			for i, j in enumerate(ds):
				temp = abs(j - o_i)
				if i is step:
					continue
				if min_dis is None:
					min_dis = temp
				elif min_dis > temp:
					min_dis = temp
				else:
					continue
			g_sum = g_sum + min_dis
		return g_sum / nsteps