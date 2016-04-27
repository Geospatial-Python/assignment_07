import math

from .point import Point

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
    x = None
    y = None
    sum_x=[]
    sum_y=[]
    for x_tmp,y_tmp in points:
        sum_x.append(x_tmp)
        sum_y.append(y_tmp)

    x=float(sum(sum_x)/len(sum_x))
    y=float(sum(sum_y)/len(sum_y))

    return x, y

def euclidean_distance(a, b):
    """
    Compute the Euclidean distance between two points

    Parameters
    ----------
    a : tuple
        A point in the form (x,y)

    b : tuple
        A point in the form (x,y)

    Returns
    -------

    distance : float
               The Euclidean distance between the two points
    """
    distance = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    return distance

def average_nearest_neighbor_distance(points,mark=None):
    """
    Given a set of points, compute the average nearest neighbor.

    Parameters
    ----------
    points : list
             A list of points
    mark   : str

    Returns
    -------
    mean_d : float
             Average nearest neighbor distance

    References
    ----------
    Clark and Evan (1954 Distance to Nearest Neighbor as a
     Measure of Spatial Relationships in Populations. Ecology. 35(4)
     p. 445-453.
    """
    mean_d = 0
    if mark==None:
        points_tmp=points
    else:
        points_tmp=[ point for point in points if point.mark==mark]

    length=len(points_tmp)
    nearest_distances=[]
    for i in range(length):
        distance=[]
        for j in range(length):
            if i==j:
                continue
            else:
                distance.append(euclidean_distance((points_tmp[i].x,points_tmp[i].y),(points_tmp[j].x,points_tmp[j].y)))
        nearest_distances.append(min(distance))

    mean_d=float(sum(nearest_distances)/len(nearest_distances))
    return mean_d


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

    mbr = [0,0,0,0]

    x_list=[]
    y_list=[]
    for x,y in points:
        x_list.append(x)
        y_list.append(y)
    mbr=[min(x_list),min(y_list),max(x_list),max(y_list)]

    return mbr


def mbr_area(mbr):
    """
    Compute the area of a minimum bounding rectangle
    """
    area = 0
    area=(mbr[2]-mbr[0])*(mbr[3]-mbr[1])
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

    expected = 0
    expected =float((math.sqrt(area/n))/2)
    return expected
