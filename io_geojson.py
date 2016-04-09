import json

def read_geojson(input_file):
    """
    Read a geojson file

    Parameters
    ----------
    input_file : str
                 The PATH to the data to be read

    Returns
    -------
    gj : dict
         An in memory version of the geojson
    """
    # Please use the python json module (imported above)
    # to solve this one.

    with open(input_file, 'r') as f:
        gj = json.load(f)
    return gj


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
    max_population = 0
    city = None
    features_list = gj.get('features')
    x = 0

    for f in features_list:
        if f['properties']['pop_max'] > max_population:
            max_population = f['properties']['pop_max']
            city = f['properties']['name']

    return city, max_population


def write_your_own(gj):
    """
    Here you will write your own code to find
    some attribute in the supplied geojson file.

    Take a look at the attributes available and pick
    something interesting that you might like to find
    or summarize.  This is totally up to you.

    Do not forget to write the accompanying test in
    tests.py!
    """
    #find the largest city west of the Mississippi River

    largest_western_city = None
    features_list = gj.get('features')
    for f in features_list:
        if f['properties']['longitude'] < -95.202:
            largest_western_city = f['properties']['longitude']


    return largest_western_city
