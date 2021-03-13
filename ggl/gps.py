# gps
from forest._importable import LazyImport


geopy = LazyImport("import geopy", "PACKAGE geopy — Geocoding library for Python, derived from 'import geopy', from https://github.com/geopy/geopy, Documentation: https://geopy.readthedocs.io/")
GoogleV3 = LazyImport("from geopy import GoogleV3", "CLASS geopy.GoogleV3 — Geocoder using the Google Maps v3 API, derived from 'from geopy import GoogleV3', from https://github.com/geopy/geopy, Documentation: https://geopy.readthedocs.io/en/stable/#googlev3")
geodesic = LazyImport("from geopy.distance import geodesic", "CLASS geopy.distance.geodesic — Calculate the geodesic distance between two points, derived from 'from geopy.distance import geodesic', from https://github.com/geopy/geopy, Documentation: https://geopy.readthedocs.io/en/stable/#module-geopy.distance")
geodist = LazyImport("from geopy import distance as geodist", "SUBPACKAGE geodist derived from geopy.distance — Calculating distance between two points, derived from 'import geopy.distance as geodist', from https://github.com/geopy/geopy, Documentation: https://geopy.readthedocs.io/en/stable/#module-geopy.distance")
