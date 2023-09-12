
# Getting Started with Geospatial

Welcome to this introductory repository on geospatial data processing in Python! The primary aim here is to bridge the gap between geospatial professionals and the world of Python programming, empowering them with tools and scripts to enhance their workflow and efficiency.

## Motivation

The geospatial industry is vast and continuously evolving. With the increasing availability of data, there's a growing need to process, analyze, and visualize this information effectively. Python, with its rich ecosystem of libraries, offers an ideal platform for these tasks. This repository aims to provide a starting point for those in the geospatial industry to leverage Python's capabilities for their data processing needs.

## Repository Overview

The `inclusion_count.py` script in this repository demonstrates how to:

1. Load geospatial data into a DataFrame.
2. Compute distances between various points of interest and the loaded data.
3. Determine the ideal point that includes the maximum number of properties within a specified radius.

## Getting Started

Before running any included scripts, you'll need data. You can downlod the data from [OpenAddresses.io](https://openaddresses.io/), which may require signup. Once done, you can navigate to the [download section](https://batch.openaddresses.io/data#map=0/0/0) and download **us-northest**, extract it and find the file `us/pa/york-address-county.geojson` and put it in the root of this folder named `york_county.geojson`.

To run the `inclusion_count.py` script, ensure you have Python3 and the required libraries installed:

```bash
python3 -m pip install pandas geopy
```

Then, execute the script:

```bash
python3 inclusion_count.py
```

## Expected Output

Upon running the script, you should see the following output:
This might take a while since we're processing a decent size dataset.

```
Loading data into DataFrame...
Computing distances of points for properties...
Computing inclusion count per point...
Ideal Points for Max Inclusion
{'york_city_fire_station': 511, 'west_york_fire_station': 801, 'lurel_rex_fire_station': 1509}
```

## Future Directions

This repository is just the beginning. As time permits, we hope to expand on this foundation, adding more functionalities, tools, and tutorials to further assist the geospatial community. Your contributions and feedback are always welcome!
