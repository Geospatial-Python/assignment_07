import json
from urllib.request import urlopen

def read_geojson(input_url):
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
  # I still can't seem to open json locally so going the url route 
  # for now until I figure it out!
  # with open(input_file, 'r') as f:
  #     gj = json.load(f)
  response = urlopen(input_url).read().decode('utf8') #For Testing purposes 
  # response = urlopen("https://api.myjson.com/bins/4587l").read().decode('utf8')
  gj = json.loads(response)

  return gj
