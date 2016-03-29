from .point import Point
from . import analytics
import random
import numpy as np

def PointPattern(object):
    def __init__(self):
        self.points = []

    def average_nearest_neighbor_distance(self, mark=None):
        return analytics.average_nearest_neighbor_distance(self.points, mark)

    def add_point(self, point):
        self.points.append(point)

    def remove_point(self, index):
        del(self.points[index])

    def count_coincident_points(self):
        count = 0
        coincidnet_list = []

        for i, point in enumerate(self.points):
            for j, point2 in enumerate(self.points):
                if i is j:
                    continue
                if j in coincident_list:
                    continue
                #Should use the magic method in point class
                if point == point2:
                    count += 1
                    coincident_list.append(j)
        return count

    def list_marks(self):
        marks = []

        for point in self.points:
            if point.mark is not None and point.mark not in marks:
                marks.append(point.mark)

    def return_subset(self, mark):
        #creates a list of points that have the same mark as passed
        return [i for i in self.points if i == mark]

    def create_random_points(self, n=None):
        rand_points = []
        rand = random.Random()
        marks = ['North', 'East', 'South', 'West']

        if n is None:
            n = len(self.points)

        for i in range(n):
            rand_points.append(point.Point(rand.randint(1,100), rand.randint(1,100), mark=rand.choice(marks)))

        return rand_points

    def create_realizations(self, k):
        return analytics.permutations(k)

    def critical_points(self):
        return analytics.find_criticals(self.create_realizations(99))

    def compute_g(self, nsteps):
        ds = np.linspace(0, 100, nsteps)
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
            g_sum += min_dis
        return g_sum / nsteps



