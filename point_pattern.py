import math  # I am guessing that you will need to use the math module
import random
import analytics
import point
import numpy as np

from math import sqrt
from test.support import temp_cwd

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
        temp=[]
        if(n==None):
            n=len(self.points);
        
        for i in range(n):
            temp.append(point.Point(random.uniform(0,1),random.uniform(0,1),random.choice(self.marks)));

        return temp
    
    def crit_pts(self):
        return analytics.critical_pts(self.points)
  
    def g_func(self,nsteps):
        
        ds = np.linspace(0,1,nsteps);
        dsum=0;
        
        for i in range(nsteps):
            oi = ds[i]
            dmin=None
            
            for j,k in enumerate (ds):
                
                temp= abs(k-oi)
                
                if k != i:
                    if dmin == None:
                        dmin=temp
                    elif dmin > temp:
                        dmin = temp
                
            dsum += dmin
            
        return dsum/nsteps
        