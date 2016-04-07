import math
import statistics
import random

def mean_center(points):
    """
    Given a set of points, compute the mean center

    Parameters
    ----------
    points : list
         A list of points in the form (x,y)

    Returns
    -------
    x : float
        Mean x coordinate

    y : float
        Mean y coordinate
    """
    total = len(points)
    y = 0
    x = 0
    for point in points:
        x += point[0]
        y += point[1]

    x = x/total
    y = y/total
    return x, y

def minimum_bounding_rectangle(points):
    """
    Given a set of points, compute the minimum bounding rectangle.

    Parameters
    ----------
    points : list
             A list of points in the form (x,y)

    Returns
    -------
     : list
       Corners of the MBR in the form [xmin, ymin, xmax, ymax]
    """
    x_list = []
    y_list = []

    for p in points:
        x_list.append(p[0])
        y_list.append(p[1])

    mbr = [0,0,0,0]
    mbr[0] = min(x_list)
    mbr[1] = min(y_list)
    mbr[2] = max(x_list)
    mbr[3] = max(y_list)

    return mbr


def mbr_area(mbr):
    """
    Compute the area of a minimum bounding rectangle
    """
    width = mbr[2] - mbr[0]
    length = mbr[3] - mbr[1]
    area = width * length

    return area


def expected_distance(area, n):
    """
    Compute the expected mean distance given
    some study area.

    This makes lots of assumptions and is not
    necessarily how you would want to compute
    this.  This is just an example of the full
    analysis pipe, e.g. compute the mean distance
    and the expected mean distance.

    Parameters
    ----------
    area : float
           The area of the study area

    n : int
        The number of points
    """

    expected = 0.5 * (math.sqrt( area / n ))
    return expected


"""
Below are the functions that you created last week.
Your syntax might have been different (which is awesome),
but the functionality is identical.  No need to touch
these unless you are interested in another way of solving
the assignment
"""

def manhattan_distance(a, b):
    """
    Compute the Manhattan distance between two points

    Parameters
    ----------
    a : tuple
        A point in the form (x,y)

    b : tuple
        A point in the form (x,y)

    Returns
    -------
    distance : float
               The Manhattan distance between the two points
    """
    distance =  abs(a[0] - b[0]) + abs(a[1] - b[1])
    return distance
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
