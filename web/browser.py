# browser
from ._importable import LazyImport, _import_statements


webbrowser = LazyImport("import webbrowser", "LIBRARY webbrowser — Convenient Web-browser controller, derived from 'import webbrowser', from The Python Standard Library")
wb = LazyImport("import webbrowser as wb", "LIBRARY wb derived from webbrowser — Convenient Web-browser controller, derived from 'import webbrowser as wb', from The Python Standard Library")
openweb = LazyImport("from webbrowser import open as openweb", "FUNCTION openweb derived from webbrowser.open — Display url using the new default browser, derived from 'from webbrowser import open as openweb', from The Python Standard Library")
