import math
import random
from .analytics import average_nearest_neighbor_distance
from .point import Point

def generate_random_points(n):
    """
    Return n random points.

    Parameters
    ----------
    n : integer

    Returns
    -------
    points_list : list
           The random points list

    """
    return [Point(random.uniform(0,1), random.uniform(0,1)) for i in range(n)]


def create_random_marked_points(n, marks=[]):

    points_list=[]
    for i in range(n):
        points_list.append(Point(random.uniform(0,1), random.uniform(0,1),random.choice(marks)))

    return points_list



def  permutation(p=99, n=100):
    """
    Return the mean nearest neighbor distance of p permutations.

    Parameters
    ----------
    p : integer
    n : integer

    Returns
    -------
    permutations : list
            the mean nearest neighbor distance list.

    """
    permutation_list=[]
    for i in range(p):
        permutation_list.append(average_nearest_neighbor_distance(generate_random_points(n)))
    return permutation_list


def  permutation_mark(p=99, n=100 ,marks=None,mark=None):
    """
    Return the mean nearest neighbor distance of p permutations.

    Parameters
    ----------
    p : integer
    n : integer
    marks : list

    Returns
    -------
    permutations : list
            the mean nearest neighbor distance list.

    """
    permutation_list=[]
    for i in range(p):
        permutation_list.append(average_nearest_neighbor_distance(create_random_marked_points(n,marks),mark))
    return permutation_list

def  critical_points(permutations):
    """
    Return the mean nearest neighbor distance of p permutations.

    Parameters
    ----------
    permutations : list
        the mean nearest neighbor distance list.
    Returns
    -------
    smallest  : float
    largest   : float

    """

    return min(permutations),max(permutations)


def  is_observed_distance_significant(smallest,largest,observed_distance):
    """
    Returns True is the observed distance is significant.

    Parameters
    ----------
    smallest : float
    largest  : float

    Returns
    -------
    bool

    """

    if observed_distance>=smallest and observed_distance<=largest:
        return  False
    else:
        return True




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


def shift_point(point, x_shift, y_shift):
    """
    Shift a point by some amount in the x and y directions

    Parameters
    ----------
    point : tuple
            in the form (x,y)

    x_shift : int or float
              distance to shift in the x direction

    y_shift : int or float
              distance to shift in the y direction

    Returns
    -------
    new_x : int or float
            shited x coordinate

    new_y : int or float
            shifted y coordinate

    Note that the new_x new_y elements are returned as a tuple

    Example
    -------
    >>> point = (0,0)
    >>> shift_point(point, 1, 2)
    (1,2)
    """
    x = getx(point)
    y = gety(point)

    x += x_shift
    y += y_shift

    return x, y


def check_coincident(a, b):
    """
    Check whether two points are coincident
    Parameters
    ----------
    a : tuple
        A point in the form (x,y)

    b : tuple
        A point in the form (x,y)

    Returns
    -------
    equal : bool
            Whether the points are equal
    """
    return a == b


def check_in(point, point_list):
    """
    Check whether point is in the point list

    Parameters
    ----------
    point : tuple
            In the form (x,y)

    point_list : list
                 in the form [point, point_1, point_2, ..., point_n]
    """
    return point in point_list


def getx(point):
    """
    A simple method to return the x coordinate of
     an tuple in the form(x,y).  We will look at
     sequences in a coming lesson.

    Parameters
    ----------
    point : tuple
            in the form (x,y)

    Returns
    -------
     : int or float
       x coordinate
    """
    return point[0]


def gety(point):
    """
    A simple method to return the x coordinate of
     an tuple in the form(x,y).  We will look at
     sequences in a coming lesson.

    Parameters
    ----------
    point : tuple
            in the form (x,y)

    Returns
    -------
     : int or float
       y coordinate
    """
    return point[1]
