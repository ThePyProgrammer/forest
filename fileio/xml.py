## xml
from forest._importable import LazyImport


lxml = LazyImport("import lxml", "PACKAGE lxml — The lxml XML toolkit for Python, derived from 'import lxml', from https://github.com/lxml/lxml, Documentation: https://lxml.de/")
etree = LazyImport("from lxml import etree", "SUBPACKAGE lxml.etree — The ElementTree API, derived from 'from lxml import etree', from https://github.com/lxml/lxml, Documentation: https://lxml.de/")
