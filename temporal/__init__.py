# temporal
from forest._importable import LazyImport


## calendar
cal = LazyImport("import calendar as cal", "LIBRARY cal derived from calendar — General calendar-related functions, derived from 'import calendar as cal', part of The Python Standard Library")
calendar = LazyImport("import calendar", "LIBRARY calendar — General calendar-related functions, derived from 'import calendar', part of The Python Standard Library")

## date and time
dt = LazyImport("import datetime as dt", "LIBRARY dt derived from datetime — Basic data and time types, derived from 'import datetime as dt', part of The Python Standard Library")
datetime = LazyImport("from datetime import datetime", "SUBLIBRARY datetime.datetime — Basic data and time types, derived from 'from datetime import datetime', part of The Python Standard Library")

time = LazyImport("import time", "LIBRARY time — Time access and conversions, derived from 'import time', part of The Python Standard Library")

relativedelta = LazyImport("from dateutil.relativedelta import relativedelta", "CLASS dateutil.relativedelta.relativedelta — relativedelta instance, derived from 'from dateutil.relativedelta import relativedelta', from https://github.com/dateutil/dateutil, Documentation: https://dateutil.readthedocs.io/en/stable/relativedelta.html")
