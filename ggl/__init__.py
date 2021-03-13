# ggl
from forest._importable import LazyImport


## search
from .search import *

# mic
convert = LazyImport("from google_currency import convert", "FUNCTION google_currency.convert(original_currency_type, new_currency_type, original_amount) — simple function to convert the currency of one country to other, derived from 'from google_currency import convert', from https://github.com/om06/google-currency")
Translator = LazyImport("from googletrans import Translator", "CLASS googletrans.Translator — class to imitate Google Translate, derived from 'from googletrans import Translator', from https://github.com/ssut/py-googletrans, Documentation: https://py-googletrans.readthedocs.io/en/latest/")

# gps
geopy = LazyImport("import geopy", "PACKAGE geopy — Geocoding library for Python, derived from 'import geopy', from https://github.com/geopy/geopy, Documentation: https://geopy.readthedocs.io/")
GoogleV3 = LazyImport("from geopy import GoogleV3", "CLASS geopy.GoogleV3 — Geocoder using the Google Maps v3 API, derived from 'from geopy import GoogleV3', from https://github.com/geopy/geopy, Documentation: https://geopy.readthedocs.io/en/stable/#googlev3")
geodesic = LazyImport("from geopy.distance import geodesic", "CLASS geopy.distance.geodesic — Calculate the geodesic distance between two points, derived from 'from geopy.distance import geodesic', from https://github.com/geopy/geopy, Documentation: https://geopy.readthedocs.io/en/stable/#module-geopy.distance")
geodist = LazyImport("from geopy import distance as geodist", "SUBPACKAGE geodist derived from geopy.distance — Calculating distance between two points, derived from 'import geopy.distance as geodist', from https://github.com/geopy/geopy, Documentation: https://geopy.readthedocs.io/en/stable/#module-geopy.distance")

# youtube
youtube_dl = LazyImport("import youtube_dl", "PACKAGE youtube_dl — Command-line program to download videos from YouTube.com and other video sites, derived from 'import youtube_dl', from https://github.com/ytdl-org/youtube-dl")
YouTube = LazyImport("from pytube import YouTube", "CLASS pytube.YouTube(url) — A lightweight YouTube wrapper for downloading YouTube videos, derived from 'from pytube import YouTube', from https://github.com/nficano/pytube, Documentation: https://python-pytube.readthedocs.io/en/latest/api.html#youtube-object")
pafy = LazyImport("import pafy", "PACKAGE pafy — Python library to download YouTube content and retrieve metadata, derived from 'import pafy', from https://github.com/mps-youtube/pafy, Documentation: https://pythonhosted.org/pafy/")
