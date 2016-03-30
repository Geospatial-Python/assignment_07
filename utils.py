import math
import random
import point


def create_n_rand_pts(n):
    n_pts = [(random.uniform(0,1), random.uniform(0,1)) for i in range(n)]
    return n_pts

def create_marked_rand_pts(n,marks=None):
    n_pts=[]
    for i in range(n):
        chosen_mark=random.choice(marks)
        temppt=point.Point(random.uniform(0,1), random.uniform(0,1),chosen_mark)
        #print(temppt.x)
        n_pts.append(temppt)
    return n_pts

def critical_pts(distances):
    return min(distances), max(distances)
    
def euclidean_distance(a, b):
    distance = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    return distance

def shift_point(point, x_shift, y_shift):
    x = getx(point)
    y = gety(point)
    x += x_shift
    y += y_shift
    return (x, y)

def expected_distance(area, n):
    return 0.5*(math.sqrt(area/n))
    
def check_coincident(a, b):
    return (a[0] == b[0]) and (a[1]==b[1])    

def check_in(point, point_list):
    return point in point_list

def getx(point):
    return point[0]

def gety(point):
    return point[1]
    
def mbr_area(mbr):
    return (mbr[3]-mbr[1])*(mbr[2]-mbr[0])
    
def manhattan_distance(a, b):
    distance =  abs(a[0] - b[0]) + abs(a[1] - b[1])
    return distance

