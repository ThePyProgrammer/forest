# scrape
from forest._importable import LazyImport


requests = LazyImport("import requests", "PACKAGE requests — A simple, yet elegant HTTP library, derived from 'import requests', from https://github.com/psf/requests, Documentation: https://requests.readthedocs.io/en/master/")
BeautifulSoup = LazyImport("from bs4 import BeautifulSoup", "CLASS bs4.BeautifulSoup — HTML/XML Formatter on Python, derived from 'from bs4 import BeautifulSoup', from https://www.crummy.com/software/BeautifulSoup/, Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/")
scrapy = LazyImport("import scrapy", "PACKAGE scrapy — A fast high-level web crawling & scraping framework for Python, derived from 'import scrapy', from https://github.com/scrapy/scrapy, Documentation: https://docs.scrapy.org/en/latest/index.html")
