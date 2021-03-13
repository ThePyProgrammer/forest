# mathematical
from forest._importable import LazyImport

math = LazyImport("import math", "LIBRARY: math — Mathematical functions, derived from 'import math', part of The Python Standard Library")
cmath = LazyImport("import cmath", "LIBRARY: cmath — Mathematical functions for complex numbers, derived from 'import cmath', part of The Python Standard Library")
statistics = LazyImport("import statistics", "LIBRARY: statistics — Mathematical statistics functions, derived from 'import statistics', part of The Python Standard Library")
random = LazyImport("import random", "LIBRARY: random — Generate pseudo-random numbers, derived from 'import random', part of The Python Standard Library")
choice = LazyImport("from random import choice", "FUNCTION: random.choice(seq) — Returns a random element from seq, derived from 'from random import choice', part of The Python Standard Library")
randint = LazyImport("from random import randint", "FUNCTION: random.randint(a, b) — Computes a random integer between a and b (both inclusive), derived from 'from random import randint', part of The Python Standard Library")
randrange = LazyImport("from random import randrange", "FUNCTION: random.randrange(start, stop[, step=1]) — Returns a randomly selected element from range(start, stop, step), derived from 'from random import randrange', part of The Python Standard Library")
shuffle = LazyImport("from random import shuffle", "FUNCTION: random.shuffle(x) — Shuffle sequence x in place, derived from 'from random import shuffle', part of The Python Standard Library")
