from .utils import *

def find_largest_city(gj):
  """
  Iterate through a geojson feature collection and
  find the largest city.  Assume that the key
  to access the maximum population is 'pop_max'.

  Parameters
  ----------
  gj : dict
       A GeoJSON file read in as a Python dictionary

  Returns
  -------
  city : str
         The largest city

  population : int
               The population of the largest city
  """
  city = None
  max_population = 0
  for n in gj["features"]:
      properties = n["properties"]
      if (properties["pop_max"] > max_population):
          max_population = properties["pop_max"]
          city = properties["adm1name"]

  return city, max_population


def alaska_points(gj):
  # Find coordinates from Alaska
  alaska_points = []
  for n in gj["features"]:
      properties = n["properties"]
      state_name = properties["adm1name"]
      if state_name == "Alaska":
          alaska_points.append(n)
      else:
          continue

  return alaska_points


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
  x = 0
  y = 0
  number_of_points = 0

  for p in points: 
      x += p[0]
      y += p[1]
      number_of_points += 1

  x = x / number_of_points
  y = y / number_of_points

  return x, y


def average_nearest_neighbor_distance(points, mark=None):
  """
  Given a set of points, compute the average nearest neighbor.

  Parameters
  ----------
  points : list
           A list of points in the form (x,y)

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
  temp_p = None

  if mark == None:
    for p in points: 
      for q in points: 
        if check_coincident(p, q):
          continue
        cached = euclidean_distance(p, q)
        if temp_p is None: 
          temp_p = cached
        elif temp_p > cached:
          temp_p = cached

      mean_d += temp_p 
      temp_p = None
  else:
    for p in points: 
      if p.mark == mark:
        for q in points: 
          if check_coincident(p, q):
            continue
          cached = euclidean_distance(p, q)
          if temp_p is None: 
            temp_p = cached
          elif temp_p > cached:
            temp_p = cached

      mean_d += temp_p 
      temp_p = None





  return mean_d / len(points)


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

  min_x = 1000000000
  min_y = 1000000000
  max_x = -1
  max_y = -1

  for n in points:
	  if n[0] < min_x:
	      min_x = n[0]
	  if n[0] > max_x:
	      max_x = n[0]
	  if n[1] < min_y:
	      min_y = n[1]
	  if n[1] > max_y:
	      max_y = n[1]
      
  mbr = [min_x, min_y, max_x, max_y]

  return mbr


def mbr_area(mbr):
  """
  Compute the area of a minimum bounding rectangle
  """
  area = ((mbr[2] - mbr[0]) * (mbr[3] - mbr[1]))

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

  expected = (0.5 * (math.sqrt(area/n)))
  return expected


def create_random(n, mark=None):
	random.seed()
	random_points = [(random.randint(0,100), random.randint(0,100), mark) for i in range(n)]
	return random_points


def permutations(p=99, n=100):
	#Compute the mean nearest neighbor distance
	permutationz = []
	for i in range(p):
		permutationz.append(average_nearest_neighbor_distance(create_random(n)))
	return permutationz


def compute_critical(points):
	lower_bound = min(points)
	upper_bound = max(points)
	return lower_bound, upper_bound


def check_significant(lower, upper, observed):
	if observed > upper: 
		return True
	if observed < lower:
		return True