from .point import Point
from . import analytics
import random
import numpy as np


class PointPattern(object):
    def __init__(self):
        self.points = []

    def add_point(self, point):
        self.points.append(point)

    def remove_point(self, index):
        try:
            del(self.points[index])
        except IndexError:
            print('Index {} not in list'.format(index))

    def average_nearest_neighbor_distance(self, mark=None):
        return analytics.average_nearest_neighbor_distance(self.points, mark)

    def count_coincident(self):
        """
        Returns the number of coincident points.
        If two points are at the same spatial location,
        that counts as two coincident points. Three coincident points
        means three points at the same location.
        """
        to_return = 0
        handled_indices = []
        for i, point_a in enumerate(self.points):
            for j, point_b in enumerate(self.points):
                if j in handled_indices:
                    continue
                if i == j:
                    continue
                if point_a.is_coincident(point_b):
                    to_return += 1
                    handled_indices.append(j)
        return to_return

    def list_marks(self):
        marks = []
        for point in self.points:
            if 'color' in point.mark and point.mark['color'] not in marks:
                marks.append(point.mark['color'])
        return marks

    def find_subset_with_mark(self, mark):
        return list(filter(lambda current_point: 'color' in current_point.mark and current_point.mark['color'] == mark, self.points))

    def generate_random_points(self, n=None):
        if n is None:
            n = len(self.points)
        to_return = []
        marks = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

        for i in range(n):
            to_return.append(Point(
                round(random.random(), 2),
                round(random.random(), 2),
                color=random.choice(marks)
            ))
        return to_return

    def generate_realizations(self, k):
        return analytics.permutations(k)

    def get_critical_points(self):
        return analytics.compute_critical(self.generate_realizations(100))

    def compute_g(self, nsteps):
        ds = np.linspace(0, 1, nsteps)
        current_sum = 0
        for i in range(nsteps):
            o_i = ds[i]
            min_distance = None
            for j, d in enumerate(ds):
                if j == i:
                    continue
                if min_distance is None:
                    min_distance = abs(d - o_i)
                else:
                    min_distance = abs(d - o_i) if abs(d - o_i) < min_distance else min_distance
            current_sum += min_distance
        return current_sum / nsteps
