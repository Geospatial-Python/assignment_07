

from point import Point
import analytics
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
        except:
            pass

    def average_nearest_neighbor_distance(self, mark=None):
        return analytics.average_nearest_neighbor_distance(self.points, mark)

    def num_of_coincident(self):
        numCoin = 0
        accounted = []


        for i in range(len(self.points)):
            for j in range(len(self.points)):
                if i in accounted:
                    continue
                if i == j:
                    continue
                if self.points[i] == self.points[j]:
                    numCoin += 1
                    accounted.append(j)

        return numCoin

    def list_marks(self):
        marks = []
        for point in self.points:
            if point.mark != None and point.mark not in marks:
                marks.append(point.mark)
        return marks

    def find_subset_with_mark(self, mark):
        marked_points = []
        for points in self.points:
            if points.mark == mark:
                marked_points.append(points)
        return marked_points

    def generate_random_points(self, n=None):
        if n is None:
            n = len(self.points)
        rndmPoints = []
        self.marks = ['burrito', 'chimichanga', 'steak', 'burger', 'chillidog',
                 'sweetpotatofries', 'beans', 'bacon', 'beijingbeef', 'friedeggs',
                 'icecream', 'brownies', 'cookie', 'bananasplit', 'almondjoy']

        for i in range(n):
            rndmPoints.append(Point(round(random.random(), 2), round(random.random(), 2), random.choice(self.marks)))
        return rndmPoints

    def generate_realizations(self, k):
        return analytics.permutations(k)

    def get_critical_points(self):
        return analytics.compute_critical(self.generate_realizations(100))

    def compute_g(self, nsteps):
        discStep = np.linspace(0, 1, nsteps)
        sum = 0
        for i in range(nsteps):
            i_step = discStep[i]
            minDist = -1
            for j in range(len(discStep)):
                if i == j:
                    continue
                if minDist == -1:
                    minDist = abs(discStep[j] - i_step)
                else:
                    if abs(discStep[j] - i_step) < minDist:
                        minDist = abs(discStep[j] - i_step)
                    else:
                        minDist = minDist
            sum += minDist

        return sum / nsteps
