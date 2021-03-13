# search
from forest._importable import LazyImport


google = LazyImport("import googlesearch as google", "PACKAGE google derived from googlesearch — The google package, derived from 'import googlesearch as google', from https://github.com/MarioVilas/googlesearch, Documentation: https://python-googlesearch.readthedocs.io/en/latest/")
googlesearch = LazyImport("import googlesearch", "PACKAGE googlesearch — The google package, derived from 'import googlesearch', from https://github.com/MarioVilas/googlesearch")

gsearch = LazyImport("from googlesearch import search as gsearch")
gimages = LazyImport("from googlesearch import search_images as images as gimages")
gnews = LazyImport("from googlesearch import search_news as gnews")
gvideos = LazyImport("from googlesearch import search_videos as gvideos")
gshop = LazyImport("from googlesearch import search_shop as gshop")
gbooks = LazyImport("from googlesearch import search_books as gbooks")
gapps = LazyImport("from googlesearch import search_apps as gapps")
glucky = LazyImport("from googlesearch import lucky as glucky")
ghits = LazyImport("from googlesearch import hits as ghits")
gngd = LazyImport("from googlesearch import ngd as gngd")
