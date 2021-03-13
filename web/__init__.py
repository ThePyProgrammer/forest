# web
from ._importable import LazyImport, _import_statements


## url
from .url import *

## scrape
from .scrape import *

## api
from .api import *

## email
smtplib = LazyImport("import smtplib", "LIBRARY smtplib — SMTP protocol client, derived from 'import smtplib', part of The Python Standard Library")


## browser
from .browser import *

## frameworks
from .frameworks import *
