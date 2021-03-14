# api
from forest._importable import LazyImport


newspaper = LazyImport("import newspaper", "PACKAGE newspaper — News, full-text, and article metadata extraction in Python 3, derived from 'import newspaper', from https://github.com/codelucas/newspaper, Documentation: https://newspaper.readthedocs.io/en/latest/")
Article = LazyImport("from newspaper import Article", "CLASS newspaper.Article — Article scraping and curation, derived from 'from newspaper import Article', from https://github.com/codelucas/newspaper, Documentation: https://newspaper.readthedocs.io/en/latest/user_guide/quickstart.html#news-articles")
fulltext = LazyImport("fromn newspaper import fulltext", "FUNCTION newspaper.fulltext — Extract full text from an article, derived from 'from newspaper import fulltext', from https://github.com/codelucas/newspaper, Documentation: https://newspaper.readthedocs.io/en/latest/")
wikipedia = LazyImport("import wikipedia", "PACKAGE wikipedia — A Pythonic wrapper for the Wikipedia API, derived from 'import wikipedia', from https://github.com/goldsmith/Wikipedia, Documentation: https://wikipedia.readthedocs.io/en/latest/")
