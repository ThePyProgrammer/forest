# youtube
from forest._importable import LazyImport


youtube_dl = LazyImport("import youtube_dl", "PACKAGE youtube_dl — Command-line program to download videos from YouTube.com and other video sites, derived from 'import youtube_dl', from https://github.com/ytdl-org/youtube-dl")
YouTube = LazyImport("from pytube import YouTube", "CLASS pytube.YouTube(url) — A lightweight YouTube wrapper for downloading YouTube videos, derived from 'from pytube import YouTube', from https://github.com/nficano/pytube, Documentation: https://python-pytube.readthedocs.io/en/latest/api.html#youtube-object")
pafy = LazyImport("import pafy", "PACKAGE pafy — Python library to download YouTube content and retrieve metadata, derived from 'import pafy', from https://github.com/mps-youtube/pafy, Documentation: https://pythonhosted.org/pafy/")
