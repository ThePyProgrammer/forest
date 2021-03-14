# astro
from forest._importable import LazyImport


astropy = LazyImport("import astropy")

sunpy = LazyImport("import sunpy")

heliopy = LazyImport("import heliopy")
ParkerSpiral = LazyImport("from heliopy import ParkerSpiral")

galpy = LazyImport("import galpy")
MiyamotoNagaiPotential = LazyImport("from galpy.potential import MiyamotoNagaiPotential")
NFWPotential = LazyImport("from galpy.potential import NFWPotential")
HernquistPotential = LazyImport("from galpy.potential import HernquistPotential")
MWPotential = LazyImport("from galpy.potential import MWPotential")
MWPotential2014 = LazyImport("from galpy.potential import MWPotential2014")
Orbit = LazyImport("from galpy.orbit import Orbit")





