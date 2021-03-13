## oop
from forest._importable import LazyImport

numbers = LazyImport("import numbers", "LIBRARY: numbers — Numeric abstract base classes, derived from 'import numbers', part of The Python Standard Library")

decimal = LazyImport("import decimal", "LIBRARY: decimal — Decimal fixed point and floating point arithmetic, derived from 'import decimal', part of The Python Standard Library")
Decimal = LazyImport("from decimal import Decimal", "CLASS: decimal.Decimal(value=0) — Decimal wrapper class, derived from 'from decimal import Decimal', part of The Python Standard Library")

fractions = LazyImport("import fractions", "LIBRARY: fractions — Rational numbers, derived from 'import fractions', part of The Python Standard Library")
Fraction = LazyImport("from fractions import Fraction", "CLASS: Fraction — creates a fraction, derived from 'from fractions import Fraction', part of The Python Standard Library")

operator = LazyImport("import operator", "LIBRARY: operator — Standard operators as functions, derived from 'import operator', part of The Python Standard Library")
