import analytics
import math
import random
import random
import numpy as np


class Point:

    def __init__(self, x = 0, y = 0, mark = ''):
        self.x = x
        self.y = y
        self.mark = mark

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __radd__(self, other):
        return Point(self.x + other, self.y + other)

    def check_coincident(self, b):

        if b.x == self.x and b.y == self.y:
            return True

    def shift_point(self, x_shift, y_shift):

        self.x += x_shift
        self.y += y_shift

class PointPattern(object):
    
    def __init__(self):
        self.points = []
        self.marks = []
        self.length = len(self.points)

    def __len__(self):
        count = 0
        for item in self.points:
            count += 1
        return count

    def add_point(self, point):
        self.points.append(point)

    def remove_point(self, index):
        del(self.points[index])

    def average_nearest_neighor(self, mark=None):
        return analytics.average_nearest_neighbor_distance(self.points, 
                mark)

    def count_coincident(self):
        counted = []
        count = 0
        for index, point in enumerate(self.points):
            for index2, point2 in enumerate(self.points):
                if index != index2:
                    if point.check_coincident(point2) is True:
                        count += 1
        return count

    def list_marks(self):
        marks = []
        for point in self.points:
            if point.mark not in marks and point.mark is not None:
                marks.append(point.mark)
        return marks
                
    def points_by_mark(self, mark):

        points_to_return = []
        for point in self.points:
            if point.mark == mark:
                points_to_return.append(point)
        return points_to_return

    def generate_random_points(self, n = None, marks = None):

        if n is None:
            n = len(self.points)
        point_list = analytics.create_random_marked_points(n, marks)
        return point_list

    def generate_realizations(p = 99, marks = None):
        neighbor_perms = []
        for i in range(p):
            neighbor_perms.append(
                    analytics.average_nearest_neighbor(
                        generate_random_points()))
        return neighbor_perms
           
    def get_critical(neighbor_perms):
        return max(perms), min(perms)

    def comupte_g(self, nsteps):
        ds = np.linspace(0, 1, nsteps)
        dist_counts = []
        for i, d in enumerate(ds):
            min_dist = None
            for n in range(nsteps):
                if n != i:
                    if min_dist is None or min_dist > d:
                        min_dist = d
            dist_counts.append(min_dist)
        return sum(dist_counts)/nsteps

