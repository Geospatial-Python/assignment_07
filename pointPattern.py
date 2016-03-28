import random
from . import point
from . import analytics
import numpy as np


class PointPattern(object):
    #initialize to list of points
    def __init__(self):
        self.points = []
        self.marks = ['lavender','orange','rose','ash','violet','magenta','cerulean']

    def add_point(self,point):
        self.points.append(point)

    def remove_point(self,index):
        del(self.points[index])

    def average_nearest_neighbor(self,mark=None):
        return analytics.average_nearest_neighbor_distance(self.points,mark)

    #find the number of coincident points
    def coin_count(self):
        count = 0
        clist = []
        for num1, point1 in enumerate(self.points):
            for num2, point2 in enumerate(self.points):
                #check that you're not comparing the same point
                if num1 != num2 and num2 not in clist: # if they are not the same point, and already counted
                    if point1 == point2:
                        count = count +1
                        clist.append(num2)
        return count


    #list all the different marks
    def mark_list(self):
        markList = []

        #go through each point and add a new mark to the mark listss
        for point in self.points:
            if point.mark not in markList:
                markList.append(point.mark)
        return markList

    #return a subset of point by mark type
    def mark_subset(self,mark):
        subset = []
        for p in self.points:
            if p.mark == mark:
                subset.append(p)
        return subset

    #where n is either provided by the user or equal to the current size of pointPattern
    def create_n_random_points(self,n =None):
        randomPoints = []
        if(n is None):
            n = len(self.points)

        for i in range(n):
            randomPoints.append(point.Point(random.randint(1,100),random.randint(1,100),random.choice(self.marks)))

        return randomPoints

    #simulate k random points patterns for Monte Carlo
    def create_k_patterns(self,k):
        return analytics.permutation_nearest_distance(self.marks,k)

    def critical_points(self):
        return analytics.critical_points(self.create_k_patterns(99))

    def compute_g(self,nsteps):
        """

        Parameters
        ----------
        nsteps: The numer of discrete d that are used to compute G(d)

        Returns
        -------

        """
        ds = np.linspace(0,1,nsteps)
        sums = 0

        for s in range(nsteps):
            oi = ds[s]
            minDist = None

            for a,b in enumerate(ds):
                temp = abs(b - oi)

                if a is not s:
                    if minDist is None: #for the first value
                        minDist = temp
                    elif minDist > temp: # if its less then the minDist, update
                        minDist = temp

            sums = sums + minDist

        g = sums/nsteps
        return g






