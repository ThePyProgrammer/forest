# science
from forest._importable import LazyImport


scipy = LazyImport("import scipy", "PACKAGE scipy — open-source software for STEM, derived from 'import scipy', from https://github.com/scipy/scipy, Documentation: https://docs.scipy.org/doc/")
#|----> Internal Scipy ----------------------------------------#
sio = LazyImport("from scipy import io as sio")                #
special = LazyImport("from scipy import special")              #
fftpack = LazyImport("from scipy import fftpack")              #
fft = LazyImport("from scipy import fft")                      #
optimize = LazyImport("from scipy import optimize")            #
op = LazyImport("from scipy import optimize as op")            #
opt = LazyImport("from scipy import optimize as opt")          #
ndimage = LazyImport("from scipy import ndimage")              #
interpolate = LazyImport("from scipy import interpolate")      #
stats = LazyImport("from scipy import stats")                  #
signal = LazyImport("from scipy import signal")                #
integrate = LazyImport("from scipy import integrate")          #
csgraph = LazyImport("from scipy.sparse import csgraph")       #
spatial = LazyImport("from scipy import spatial")              #
#--------------------------------------------------------------#
