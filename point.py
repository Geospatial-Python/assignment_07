import math
import random


class Point:

    def __init__(self, x = 0, y = 0, mark = []):
        self.x = x
        self.y = y
        self.mark = mark

    def check_coincident(self, b):

        if b.x == self.x and b.y == self.y:
            return True

    def shift_point(self, x_shift, y_shift):

        self.x += x_shift
        self.y += y_shift

def create_random_marked_points(n, marks = None):
    point_list = []
    rand = random.Random()
    for i in range(n):
        rand_x = round(rand.uniform(0,1),2)
        rand_y = round(rand.uniform(0,1),2)
        if marks is None:
            point_list.append(Point(rand_x, rand_y))
        else:
            rand_mark = random.choice(marks)
            point_list.append(Point(rand_x, rand_y, rand_mark))
    return point_list
def euclidean_distance(a, b):

    distance = math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
    return distance


def average_nearest_neighbor_distance(points, mark = None):

    new_points = []
    if mark is None:
        new_points = points
    else:
        for point in points:
            if point.mark is mark:
                new_points.append(point)

    dists = []
    for num1, point in enumerate(new_points):
        dists.append(None) 
        for num2, point2 in enumerate(new_points):
            if num1 is not num2:
                new_dist = euclidean_distance(point, point2)
                if dists[num1] == None:
                    dists[num1] = new_dist
                elif dists[num1] > new_dist:
                    dists[num1] = new_dist

    return sum(dists)/len(points)

def permutations(p=99, n=100, marks=None):

    neighbor_perms = []
    for i in range(p):
        neighbor_perms.append(average_nearest_neighbor_distance(create_random_marked_points(n),
            marks))
    return neighbor_perms

def compute_critical(perms):
    return max(perms), min(perms)

def check_significant(lower, upper, observed):
    return(lower <= observed or observed <= upper)
