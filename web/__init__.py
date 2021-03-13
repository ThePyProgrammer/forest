# web
from ._importable import LazyImport, _import_statements


## url
from .url import *

## scrape
from .scrape import *

## apis
newspaper = LazyImport("import newspaper", "PACKAGE newspaper — News, full-text, and article metadata extraction in Python 3, derived from 'import newspaper', from https://github.com/codelucas/newspaper, Documentation: https://newspaper.readthedocs.io/en/latest/")
Article = LazyImport("from newspaper import Article", "CLASS newspaper.Article — Article scraping and curation, derived from 'from newspaper import Article', from https://github.com/codelucas/newspaper, Documentation: https://newspaper.readthedocs.io/en/latest/user_guide/quickstart.html#news-articles")
fulltext = LazyImport("fromn newspaper import fulltext", "FUNCTION newspaper.fulltext — Extract full text from an article, derived from 'from newspaper import fulltext', from https://github.com/codelucas/newspaper, Documentation: https://newspaper.readthedocs.io/en/latest/")
wikipedia = LazyImport("import wikipedia", "PACKAGE wikipedia — A Pythonic wrapper for the Wikipedia API, derived from 'import wikipedia', from https://github.com/goldsmith/Wikipedia, Documentation: https://wikipedia.readthedocs.io/en/latest/")


## email
smtplib = LazyImport("import smtplib", "LIBRARY smtplib — SMTP protocol client, derived from 'import smtplib', part of The Python Standard Library")


## browser
webbrowser = LazyImport("import webbrowser", "LIBRARY webbrowser — Convenient Web-browser controller, derived from 'import webbrowser', from The Python Standard Library")
wb = LazyImport("import webbrowser as wb", "LIBRARY wb derived from webbrowser — Convenient Web-browser controller, derived from 'import webbrowser as wb', from The Python Standard Library")
openweb = LazyImport("from webbrowser import open as openweb", "FUNCTION openweb derived from webbrowser.open — Display url using the new default browser, derived from 'from webbrowser import open as openweb', from The Python Standard Library")


## frameworks
fastapi = LazyImport("import fastapi")
FastAPI = LazyImport("from fastapi import FastAPI")
pydantic = LazyImport("import pydantic")
tornado = LazyImport("import tornado")
sanic = LazyImport("import sanic")
Sanic = LazyImport("from sanic import Sanic")