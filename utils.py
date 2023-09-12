import math
from re import sub
from geopy.distance import geodesic

# Usage of a proper library for calculating distance
def compute_distance_geopy(coord1, coord2):
    return geodesic(coord1[::-1], coord2[::-1]).kilometers

# Haversine calculates distance on a sphere, apporximation
def compute_distance_haversine(coord1, coord2):
    R = 6371.0 # Radius of the Earth in kilometers
    
    lat1 = math.radians(coord1[1])
    lon1 = math.radians(coord1[0])
    lat2 = math.radians(coord2[1])
    lon2 = math.radians(coord2[0])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c

def snake_case(s):
  return '_'.join(
    sub('([A-Z][a-z]+)', r' \1',
    sub('([A-Z]+)', r' \1',
    s.replace('-', ' '))).split()).lower()