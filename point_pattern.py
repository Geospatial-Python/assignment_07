import math  # I am guessing that you will need to use the math module
import analytics
import point
import numpy as numpy_use

from math import sqrt

class PointPattern(object):

    def __init__(self):
        self.points = []

    def add_pt (self,point):
        self.points.append(point)
        
    def remove_pt (self,index):
        del(self.points[index])
        
    def average_nearest_neighbor_distance(self, marks=None):
        return analytics.average_nearest_neighbor_distance(self.points,marks)
    
    def number_coincident_points(self):
        num=0;
        coincident_list=[]
        for i, p1 in enumerate(self.points):
            for j, p2 in enumerate(self.points):
                if i!=j:
                    if p2 not in coincident_list:
                        if p1==p2:
                            num+=1
                            coincident_list.append(p2)
        return num
    
    def list_marks(self):
        mark_list=[]
        for i in self.points:
            if i.mark not in mark_list:
                mark_list.append(i.mark)
        return mark_list
    
    def points_by_mark(self):
    #return a subset of points by the mark
        return 0;
    
    def n_rand_pts(self,n=None,marks=None):
        if(n==None):
            n=self.points.__len__();
            self.points.append(utils.create_marked_rand_pts(n, marks));

    
    
    
    
    def g_func(self,numsetps):
        
        
        sum=0;
        for i in range(numsteps)
        