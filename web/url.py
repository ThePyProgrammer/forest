# url
from ._importable import LazyImport, _import_statements


urllib = LazyImport("import urllib", "LIBRARY urllib — URL handling modules, derived from 'import urllib', from The Python Standard Library")
request = LazyImport("from urllib import request", "LIBRARY urllib.request — Extensive library for opening URLs, derived from 'from urllib import request', from The Python Standard Library")
urllib2 = LazyImport("import urllib.request as urllib2", "LIBRARY urllib2 derived from urllib.request — Extensive library for opening URLs, derived from 'import urllib.request as urllib2', from The Python Standard Library")
urlopen = LazyImport("from urllib.request import urlopen", "FUNCTION urllib.request.urlopen(url...) — Opens the URL url which can be either a string or a Request object, derived from 'from urllib.request import urlopen', from The Python Standard Library")
