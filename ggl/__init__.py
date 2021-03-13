# ggl
from forest._importable import LazyImport


## search
from .search import *

## misc
convert = LazyImport("from google_currency import convert", "FUNCTION google_currency.convert(original_currency_type, new_currency_type, original_amount) — simple function to convert the currency of one country to other, derived from 'from google_currency import convert', from https://github.com/om06/google-currency")
Translator = LazyImport("from googletrans import Translator", "CLASS googletrans.Translator — class to imitate Google Translate, derived from 'from googletrans import Translator', from https://github.com/ssut/py-googletrans, Documentation: https://py-googletrans.readthedocs.io/en/latest/")

## gps
from .gps import *

# youtube
from .youtube import *
