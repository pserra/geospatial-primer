import json
import pandas as pd
from utils import compute_distance_geopy, compute_distance_haversine, snake_case

def inclusions_per_point(df, point_keys, radius):
    """
    Count the amount of included entries for each point key.
    :param df: DataFrame containing property data with coordinates.
    :param point_key: List of keys on the df representing distances.
    :param radius: Radius, in same unit as point_key values.
    :return: Dict returning point_key and inclusion count.
    """
    results = {}
    max_included = 0
    for point_key in point_keys:
        # Lets remove the "distance_from_key" part of the key for readability
        base_point_key = point_key.replace("distance_from_", "")
        # Lets sum up all the properties within the radius
        results[base_point_key] = sum(1 for _, row in df.iterrows() if row[point_key] <= radius)
    return results

# Function to determine distance from a list of provided points
def distances_from_points(df, points, method):
    results = []

    # For each point, lets calculate the distance
    for point in points.items():
        df[snake_case(f"distanceFrom{point[0]}")] = df.apply(
            lambda row: method(row['geometry']['coordinates'], point[1]),
            axis=1
        )
    return df

# Assume we're looking for the best point to place a fire station

# Convert the provided location data into a DataFrame
# Since this geojson isn't properly formatted, we'll load it line by line
properties = []
print("Loading data into DataFrame...")
data = open('./york-county.geojson', 'r').readlines()
for line in data:
    properties.append(json.loads(line))

# Convert to DataFrame
properties = pd.DataFrame(properties)

# Define our possible stations
points = {
    "York City Fire Station": [-76.6888542, 39.9759451],
    "West York Fire Station": [-76.7582413, 39.9541531],
    "Lurel Rex Fire Station": [-76.7251432, 39.9620295]
}

# Determien the distance of each property to each point
# Store the distance for each on the property
print("Computing distances of points for properties...")
distances = distances_from_points(properties, points, compute_distance_geopy)

# Lets get the full key names for each station
point_keys = list(map(lambda p: snake_case(f"distanceFrom{p}"), points.keys()))

# Lets find the ideal point for the most inclusions
print("Computing inclusion count per point...")
inclusions = inclusions_per_point(distances, point_keys, 0.5)

# Lets print out all of the points with a count
print("Ideal Points for Max Inclusion")
print(inclusions)